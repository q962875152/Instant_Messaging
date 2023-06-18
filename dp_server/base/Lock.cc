#include "Lock.h"

CLock::CLock() {
    pthread_mutex_init(&m_lock, nullptr);
}

CLock::~CLock() {
    pthread_mutex_destroy(&m_lock);
}

void CLock::lock() {
    pthread_mutex_lock(&m_lock);
}

void CLock::unlock() {
    pthread_mutex_unlock(&m_lock);
}

bool CLock::try_lock() {
    return pthread_mutex_trylock(&m_lock) == 0;
}

CRWLock::CRWLock() {
    pthread_rwlock_init(&m_lock, nullptr);
}

CRWLock::~CRWLock() {
    pthread_rwlock_destroy(&m_lock);
}

void CRWLock::rlock() {
    pthread_rwlock_rdlock(&m_lock);
}

void CRWLock::wlock() {
    pthread_rwlock_wrlock(&m_lock);
}

void CRWLock::unlock() {
    pthread_rwlock_unlock(&m_lock);
}

bool CRWLock::try_rlock() {
    return pthread_rwlock_tryrdlock(&m_lock) == 0;
}

bool CRWLock::try_wlock() {
    return pthread_rwlock_trywrlock(&m_lock) == 0;
}

CAutoRWLock::CAutoRWLock(CRWLock* pLock, bool bRLock) {
    m_pLock = pLock;
    if (nullptr != m_pLock) {
        if (bRLock) {
            m_pLock->rlock();
        } else {
            m_pLock->wlock();
        }
    }
}

CAutoLock::~CAutoLock() {
    if (nullptr != m_pLock) {
        m_pLock->unlock();
    }
}

CAutoLock::CAutoLock(CLock* pLock) {
    m_pLock = pLock;
    if (nullptr != m_pLock) {
        m_pLock->lock();
    }
}

CAutoLock::~CAutoLock() {
    if (nullptr != m_pLock) {
        m_pLock->unlock();
    }
}