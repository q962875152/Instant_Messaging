#include "BaseSocket.h"
#include "EventDispatch.h"

using SocketMap = hash_map<net_handle_t, CBaseSocket*>;
SocketMap   g_socket_map;

void AddBaseSocket(CBaseSocket* pSocket) {
    g_socket_map.insert(make_pair((net_handle_t)pSocket->GetSocket(), pSocket));
}

void RemoveBaseSocket(CBaseSocket* pSocket) {
    g_socket_map.erase((net_handle_t)pSocket->GetSocket());
}

CBaseSocket* FindBaseSocket(net_handle_t fd) {
    CBaseSocket* pSocket = nullptr;
    auto iter = g_socket_map.find(fd);
    if (iter != g_socket_map.end()) {
        pSocket = iter->second;
        pSocket->AddRef();
    }

    return pSocket;
}

CBaseSocket::CBaseSocket() : m_socket(INVALID_SOCKET), m_state(SOCKET_STATE_IDLE){
}

CBaseSocket::~CBaseSocket() {
}

void CBaseSocket::SetSendBufSize(uint32_t send_size) {
    int ret = setsockopt(m_socket, SOL_SOCKET, SO_SNDBUF, &send_size, 4);
    if (ret == SOCKET_ERROR) {
        log_error("set SO_SNDBUF failed for fd=%d", m_socket);
    }

    socklen_t len = 4;
    int size = 0;
    getsockopt(m_socket, SOL_SOCKET, SO_SNDBUF, &size, &len);
    log_debug("socket=%d send_buf_size=%d", m_socket, size);
}

void CBaseSocket::SetRecvBufSize(uint32_t recv_size) {
    int ret = setsockopt(m_socket, SOL_SOCKET, SO_RCVBUF, &recv_size, 4);
    if (SOCKET_ERROR == ret) {
        log_error("set SO_RCVBUF failed for fd=%d", m_socket);
    }

    socklen_t len = 4;
    int size = 0;
    getsockopt(m_socket, SOL_SOCKET, SO_RCVBUF, &size, &len);
    log_debug("socket=%d, recv_buf_size=%d", m_socket, size);
}

int CBaseSocket::Listen(const char* server_ip, uint16_t port, callback_t callback, void* callback_data) {
    m_local_ip = server_ip;
    m_local_port = port;
    m_callback = callback;
    m_callback_data = callback_data;

    m_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (INVALID_SOCKET == m_socket) {
        log_error("socket failed, err_code=%d, server_ip=%s, port=%u", _GetErrorCode(), server_ip, port);
        return NETLIB_ERROR;
    }

    _SetReuseAddr(m_socket);
    _SetNonblock(m_socket);

    sockaddr_in serv_addr;
    _SetAddr(server_ip, port, &serv_addr);
    int ret = ::bind(m_socket, (sockaddr*)&serv_addr, sizeof(serv_addr));
    if (SOCKET_ERROR == ret) {
        log_error("bind failed, err_code=%d, server_ip=%s, port=%u", _GetErrorCode(), server_ip, port);
        closesocket(m_socket);
        return NETLIB_ERROR;
    }

    ret = listen(m_socket, 64);
    if (SOCKET_ERROR == ret) {
        log_error("listen failed, err_code=%d, server_ip=%s, port=%u", _GetErrorCode(), server_ip, port);
        closesocket(m_socket);
        return NETLIB_ERROR;
    }

    m_state = SOCKET_STATE_LISTENING;

    log_debug("CBaseSocket::Listen on %s:%d", server_ip, port);

    AddBaseSocket(this);
    CEventDispatch::Instance()->AddEvent(m_socket, SOCKET_READ | SOCKET_EXCEP);
    return NETLIB_OK;
}

net_handle_t CBaseSocket::Connect(cosnt char* server_ip, uint16_t port, callback_t callback, void* callback_data) {
    log_debug("CBaseSocket::Connect, server_ip=%s, port=%d", server_ip, port);

    m_remote_ip = server_ip;
    m_remote_port = port;
    m_callback = callback;
    m_callback_data = callback_data;

    m_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (INVALID_SOCKET == m_socket) {
        log_error("socket failed, err_code=%d, server_ip=%d, port=%u", _GetErrorCode(), server_ip, port);
        return NETLIB_INVALID_HANDLE;
    }

    _SetNonblock(m_socket);
    _SetNoDelay(m_socket);
    sockaddr_in serv_addr;
    _SetAddr(server_ip, port, &serv_addr);
    int ret = connect(m_socket, (sockaddr*)&serv_addr, sizeof(serv_addr));
    if ((SOCKET_ERROR == ret) && (!_IsBlock(_GetErrorCode()))) {
        log_error("connect failed, err_code=%d, server_ip=%s, port=%u", _GetErrorCode(), server_ip, port);
        closesocket(m_socket);
        return NETLIB_INVALID_HANDLE;
    }
    m_state = SOCKET_STATE_CONNECTING;
    AddBaseSocket(this);
    CEVentDispatch::Instance()->AddEvent(m_socket, SOCKET_ALL);

    return (net_handle_t)m_socket;
}

int CBaseSocket::Send(void* buf, int len) {
    if (m_state != SOCKET_STATE_CONNECTED) {
        return NETLIB_ERROR;
    }

    int ret = send(m_socket, (char*)buf, len, 0);
    if (SOCKET_ERROR == ret) {
        int err_code = _GetErrorCode();
        if (_IsBlock(err_code)) {
            #if ((defined _WIN32) || (defined __APPLE__))
                CEventDispatch::Instance()->AddEvent(m_socket, SOCKET_WRITE);
            #endif
                ret = 0;
        } else {
            log_error("send failed, err_code=%d, len=%d", err_code, len);
        }
    }

    return ret;
}

int CBaseSocket::Recv(void* buf, int len) {
    return recv(m_socket, (char*)buf, len, 0);
}

int CBaseSocket::Close() {
    CEventDispatch::Instance()->RemoveEvent(m_socket, SOCKET_ALL);
    RemoveBaseSocket(this);
    closesocket(m_socket);
    ReleaseRef();

    return 0;
}

void CBaseSocket::OnRead() {
    if (SOCKET_STATE_LISTENING == m_state) {
        _AcceptNewSocket();
    } else {
        u_long avail = 0;
        int ret = ioctlsocket(m_socket, FIONREAD, &avail);
        if ((SOCKET_ERROR == ret) || (0 == avail)) {
            m_callback(m_callback_data, NETLIB_MSG_CLOSE, (net_handle_t)m_socket, nullptr);
        } else {
            m_callback(m_callback_data, NETLIB_MSG_READ, (net_handle_t)m_socket, nullptr);
        }
    }
}

void CBaseSocket::Onwrite() {
#if ((defined _WIN32) || (defined __APPLE__))
    CEventDispatch::Instance()->RemoveEvent(m_socket, SOCKET_WRITE);
#endif

    if (SOCKET_STATE_CONNECTING == m_state) {
        int error = 0;
        socklen_t len = sizeof(error);
#ifndef _WIN32
        getsockopt(m_socket, SOL_SOCKET, SO_ERROR, (char*)&error, &len);
#else
        getsockopt(m_socket, SOL_SOCKET, SO_ERROR, (void*)&error, &len);
#endif
        if (error) {
            m_callback(m_callback_data, NETLIB_MSG_CLOSE, (net_handle_t)m_socket, nullptr);
        } else {
            m_state = SOCKET_STATE_CONNECTED;
            m_callback(m_callback_data, NETLIB_MSG_CONFIRM, (net_handle_t)m_socket, nullptr);
        }
    } else {
        m_callback(m_callback_data, NETLIB_MSG_WRITE, (net_handle_t)m_socket, nullptr);
    }
}

void CBaseSocket::OnClose() {
    m_state = SOCKET_STATE_CLOSING;
    m_callback(m_callback_data, NETLIB_MSG_CLOSE, (net_handle_t)m_socket, nullptr);
}



void CBaseSocket::_SetReuseAddr(SOCKET fd) {
    int reuse = 1;
    int ret = setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, (char*)&reuse, sizeof(reuse));
    if (SOCKET_ERROR == ret) {
        log_error("_SetReuseAddr failed, err_code=%d, fd=%d", _GetErrorCode(), fd);
    }
}

void CBaseSocket::_SetNoDelay(SOCKET fd) {
    int nodelay = 1;
    int ret = setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, (char*)nodelay, sizeof(nodelay)); // 金庸nagle算法
    if (SOCKET_ERROR == ret) {
        log_error("_SetNoDely failed, err_code=%d, fd=%d", _GetErrorCode(), fd);
    }
}

void CBaseSocket::_SetNonblock(SOCKET fd) {
#ifdef _WIN32
    u_long nonblock = 1;
    int ret = ioctlsocket(fd, FIONBIO, &nonblock);
#else
    int ret = fcntl(fd, F_SETFL, O_NONBLOCK | fcntl(fd, F_GETFL));
#endif
    if (SOCKET_ERROR == ret) {
        log_error("_SetNonblock failed, err_code=%d, fd=%d", _GetErrorCode(), fd);
    }
}

void CBaseSocket::_SetAddr(const char* ip, const uint16_t port, sockaddr_in* pAddr) {
    memset(pAddr, 0, sizeof(sockaddr_in));
    pAddr->sin_family = AF_INET;
    pAddr->sin_port = htons(port);
    pAddr->sin_addr.s_addr = inet_addr(ip);
    if (INADDR_NONE == pAddr->sin_addr.s_addr) {
        hostent* host = gethostbyname(ip);
        if (nullptr == host) {
            log_error("gethostbyname failed, ip=%s, port=%u", ip, port);
            return;
        }

        Addr->sin_addr.s_addr = *(uint32_t*)host->h_addr;
    }
}

void CBaseSocket::_GetErrorCode() {
#ifdef_WIN32
    return WSAGetLastError();
#else
    return errno;
#endif
}

void CBaseSocket::_IsBlock(int error_code) {
#ifdef _WIN32
    return ((WSAEINPROGRESS == error_code) || (WSAEWOULDBLOCK == error_code));
#else
    // EINPROGRESS 表示 I/O 操作正在进行中，不能立即完成。这个错误码通常在进行非阻塞的连接或者发送操作时出现，
    // 表示连接或者发送操作正在进行中，但是还没有完成。
    // EWOULDBLOCK 表示 I/O 操作不能立即完成，需要等待。这个错误码通常在进行非阻塞式的读取操作时出现，
    // 表示当前没有可读数据，需要等待数据到达才能进行读取操作。
    return ((EINPROGRESS == error_code) || (EWOULDBLOCK == error_code));
#endif
}

void CBaseSocket::_AcceptNewSocket() {
    SOCKET fd = 0;
    sockaddr_in peer_addr;
    socklen_t addr_len = sizeof(sockaddr_in);
    char ip_str[64];
    while ((fd = accept(m_socket, (sockaddr*)&peer_addr, &addr_len)) != INVALID_SOCKET) {
        CBaseSocket* pSocket = new CBaseSocket();
        uint32_t ip = ntohl(peer_addr.sin_addr.s_addr);
        uint16_t port = ntohs(peer_addr.sin_port);

        snprintf(ip_str, sizeof(ip_str), "%d.%d.%d.%d", ip >> 24, (ip >> 16) & 0xFF, (ip >> 8) & 0xFF, ip & 0xFF);

        log_debug("AcceptNewSocket, socket=%d from %s:%d", fd, ip_str, port);

        pSocket->SetSocket(fd);
        pSocket->SetCallback(m_callback);
        pSocket->SetCallbackData(m_callback_data);
        pSocket->SetState(SOCKET_STATE_CONNECTED);
        pSocket->SetRemoteIP(ip_str);
        pSocket->SetRemotePort(port);

        _SetNoDelay(fd);
        _SetNonblock(fd);
        AddBaseSocket(pSocket);
        CEventDispatch::Instance()->AddEvent(fd, SOCKET_READ | SOCKET_EXCEP);
        m_callback(m_callback_data, NETLIB_MSG_CONNECT, (net_handle_t)fd, nullptr);
    }
}