#include "EventDispatch.h"
#include "BaseSocket.h"

#define MIN_TIMER_DURATION  100  // 100 miliseconds

static CEventDispatch*	m_pEventDispatch = nullptr;

CEventDispatch::CEventDispatch() {
    running = false;

    m_epfd = epoll_create(1024);
    if (-1 == m_epfd) {
        log_error("epoll_create failed");
    }
}

CEventDispatch::~CEventDispatch() {
    close(m_epfd);
}

CEventDispatch* CEventDispatch::Instance() {
    if (nullptr == m_pEventDispatch) {
        std::lock_guard<std::mutex> lck(mutex);
        if (nullptr == m_pEventDispatch) {
            m_pEventDispatch = new CEventDispatch();
            atexit(Destructor);
        }
    }

    return m_pEventDispatch;
}

void CEventDispatch::AddTimer(callback_t callback, void* user_data, uint64_t interval) {
    // list<TimerItem*>::assign
    for (auto it : m_timer_list) {
        auto pTtem = *it;
        if (pItem->callback == callback && pItem->user_data == user_data) {
            pItem->interval = interval;
            pItem->next_tick = get_tick_count() + interval;
            return;
        }
    }

    TimerItem* pItem = new TimerItem;
    pItem->callback = callback;
    pItem->user_data = user_data;
    pItem->interval = interval;
    pItem->next_tick = get_tick_count() + interval;
    m_timer_list.push_back(pItem);
}

void CEventDispatch::RemoveTimer(callback_t callback, void* user_data) {
    for (auto it : m_timer_list) {
        auto pItem = *it;
        if (pItem->callback == callback && pItem->user_data == user_data) {
            m_timer_list.erase(it);
            delete pItem;
            return;
        }
    }
}

void CEventDispatch::_CheckTimer() {
    uint64_t curr_tick = get_tick_count();
    for (auto it : m_timer_list) {
        auto pItem = *it;
        if (curr_tick >= pItem->next_tick) {
            pItem->next_tick += pTtem->interval;
            pItem->callback(pItem->user_data, NETLIB_MSG_TIMER, 0, nullptr);
        }
    }
}

void CEventDispatch::AddLoop(callback_t callback, void* user_data) {
    auto pTtem = new TimerItem;
    pItem->callback = callback;
    pItem->user_data = user_data;
    m_loop_list.push_back(pItem);
}

void CEventDispatch::_CheckLoop() {
    for (auto it : m_loop_list) {
        auto pItem = *it;
        pItem->callback(pItem->user_data, NETLIB_MSG_LOOP, 0, nullptr);
    }
}

void CEventDispatch::AddEvent(SOCKET fd, uint8_t socket_event) {
    struct epoll_event ev;
    ev.events = EPOLLIN | EPOLLOUT | EPOLLET | EPOLLPRI | EPOLLERR | EPOLLHUP; 
    ev.data.fd = fd;
    if (epoll_ctl(m_epfd, EPOLL_CTL_ADD, fd, &ev) != 0) {
        log_error("epoll_ctl() failed, errno=%d", errno);
    }
}

void CEventDispatch::RemoveEvent(SOCKET fd, uint8_t socket_event) {
    if (epoll_ctl(m_epfd, EPOLL_CTL_DEL, fd, nullptr) != 0) {
        log_error("epoll_ctl failed, errno=%d", errno);
    }
}

void CEventDispatch::StartDispatch(uint32_t wait_timeout) {
    struct epoll_event events[1024];
    int nfds = 0;

    if (running)
        return;
    running = true;

    while (running) {
        nfds = epoll_wait(m_epfd, events, 1024, wait_timeout);
        for (int i = 0; i < nfds; i++) {
            int ev_fd = events[i].data.fd;
            CBaseSocket* pSocket = FindBaseSocket(ev_fd);
            if (!pSocket) {
                continue;
            }

            if (events[i].events & EPOLLRDHUP) {  // 对端连接关闭或版关闭
                pSocket->OnClose();
            }

            if (events[i],events & EPOLLIN) {  // 可读事件标志位
                pSocket->OnRead();
            }

            if (events[i].events & EPOLLOUT) {
                pSocket->OnWrite();
            }

            if (events[i].events & (EPOLLPRI | EPOLLERR | EPOLLHUP)) {
                pSocket->OnClose();
            }

            pSocket->ReleaseRef();
        }

        _CheckTimer();
        _CheckLoop();
    }
}

void CEventDispatch::StopDispatch() {
    running = false;
}

#endif