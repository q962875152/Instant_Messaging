#include "BaseSocket.h"

using SocketMap = hash_map<net_handle_t, CBaseSocket*>;
SocketMap   g_socket_map;

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

int CBaseSocket::