#include "CachePool.h"
#include "ConfigFileReader.h"
#include "util.h"

std::mutex CacheManager::mutex;
CacheManager::s_cache_manager = nullptr;//静态成员需要初始化
#define MIN_CACHE_CONN_CNT	2

CacheManager::CacheManager() {
}

CacheManager::~CacheManager() {

}

CacheManager* CacheManager::getInstance() {
    if (nullptr == s_cache_manager) {
        std::lock_guard<std::mutex> lock(mutex);
        if (nullptr == s_cache_manager) {
            s_cache_manager = new CacheManager();
            if (s_cache_manager->Init()) {
                delete s_cache_manager;
                s_cache_manager = nullptr;
            }
            atexit(Destructor);
        }
    }

    return s_cache_manager;
}

int CacheManager::Init() {
    CConfigFileReader config_file("dbproxyserver.conf");
    
    char* cache_instanches = config_file.GetConfigName("CacheInstances");
    if (nullptr == cache_instanches) {
        log("not configure CacheIntance");
        return 1;
    }

    char host[64];
    char port[64];
    char db[64];
    char maxconnect[64];

    CStrExplode instances_name(cache_instanches, ',');
    for (uint32_t i = 0; i < instances_name.GetItemCnt(); i++) {
        char* pool_name = instances_name.GetItem(i);
        snprintf(host, 64, "%s_host", pool_name);
        snprintf(port, 64, "%s_port", pool_name);
        snprintf(db, 64, "%s_db", pool_name);
        snprintf(maxconnect, 64, "%s_maxconnect", pool_name);

        char* cache_host = config_file.GetConfigName(host);
        char* str_cache_port = config_file.GetConfigName(port);
        char* str_cache_db = config_file.GetConfigName(db);
        char* str_max_conn_cnt = config_file.GetConfigName(maxconnect);
        if ((nullptr == cache_host) || (nullptr == str_cache_port) || \
            (nullptr == str_cache_db) || (nullptr == str_max_conn_cnt)) {
                log("not configure cache instance: %s", pool_name);
                return 2;
        }

        CachePool* pCachePool = new CachePool(pool_name, cache_host, atoi(str_cache_port), \
                    atoi(str_cache_db), atoi(str_max_conn_cnt));
        if (pCachePool->Init()) {
            log("Init cache pool failed");
            return 3;
        }

        m_cache_pool_map.insert(make_pair(pool_name, pCachePool));
        
    }

    return 0;
}

CacheConn* CacheManager::GetCacheConn(const char* pool_name) {
    auto it = m_cache_pool_map.find(pool_name);
    if (it != m_cache_pool_map.end()) {
        return *it->second->GetCacheConn();
    } else {
        return nullptr;
    }
}

//******************************CachePool***********************************//
CachePool::CachePool(const char* pool_name, const char* server_ip, int server_port, int db_num, int max_conn_cnt) {
    m_pool_name = pool_name;
    m_server_ip = server_ip;
    m_server_port = server_port;
    m_db_num = db_num;
    m_max_conn_cnt = max_conn_cnt;
    m_cur_conn_cnt = MIN_CACHE_CONN_CNT;
}

CachePool::~CachePool() {
    m_free_notify.Lock();
    for (list<CacheConn*>::iterator it = m_free_list.begin(); it != m_free_list.end(); it++) {
        CacheConn* pConn = *it;
        delete pConn;
    }

    m_free_list.clear();
    m_cur_conn_cnt = 0;
    m_free_notify.Unlock();
}

CachePool::Init() {
    for (int i = 0; i < m_cur_conn_cnt; i++) {
        CacheConn* pConn = new CacheConn(this);
        if (pConn->Init()) {
            delete pConn;
            return 1;
        }

        m_free_list.push_back(pConn);
    }

    log("cache pool:: %s, list size: %lu", m_pool_name.c_str(), m_free_list.size());
    return 0;
}

CacheConn* CachePool::GetCacheConn() {
    m_free_notify.Lock();

    while (m_free_list.empty()) {
        if (m_cur_conn_cnt >= m_max_conn_cnt) {
            m_free_notify.Wait();
        } else {
            CacheConn* pCacheConn = new CacheConn(this);
            int ret = pCacheConn->Init();
            if (ret) {
                log("Init CacheConn failed");
                delete pCacheConn;
                m_free_notify.Unlock();
                return nullptr;
            } else {
                m_free_list.push_back(pCacheConn);
                m_cur_conn_cnt++;
                log("new cache connection: %s, conn_cnt: %d", m_pool_name.c_str(), m_cur_conn_cnt);
            }
        }
    }

    CacheConn* pConn = m_free_list.front();
    m_free_list.pop_front();

    m_free_notify.Unlock();
    return pConn;
}

void CachePool::RelCacheConn(CacheConn* pCacheConn) {
    m_free_notify.Lock();

    list<CacheConn*>::iterator it = m_free_list.begin();
    for (; it != m_free_list.end(); it++) {
        if (*it == pCacheConn) {
            break;
        }
    }

    if (it == m_free_list.end()) {
        m_free_list.push_back(pCacheConn);
    }

    m_free_notify.Signal();
    m_free_notify.Unlock();
}

//************************************************CacheConn****************************************************//
CacheConn::CacheConn(CachePool* pCachePool) {
    m_pCachePool = pCachePool;
    m_pContext = nullptr;
    m_last_connect_time = 0;
}

CacheConn::~CacheConn() {
    if (nullptr != m_pContext) {
        redisFree(m_pContext);
        m_pContext = nullptr;
    }
}

/*redis初始化连接和重连操作， 类似于mysql_ping()*/
int CacheConn::Init() {
    if (nullptr != m_pContext) {
        return 0;
    }

    // 四秒 尝试重连一次
    uint64_t cur_time = (uint64_t)time(nullptr);
    if (cur_time < m_last_connect_time + 4) {
        return 1;
    }
    m_last_connect_time = cur_time;

    // 200ms超时
    struct timeval timeout = {0, 200000};
    m_pContext = redisConnectWithTimeout(m_pCachePool->GetServerIP(), m_pCachePool->GetServerPort(), timeout);
    if (nullptr == m_pContext || m_pContext->err) {
        if (nullptr != m_pContext) {
            log("redisConnect failed: %s", m_pContext->errstr);
            redisFree(m_pContext);
            m_pContext = nullptr;
        } else {
            log("redisConnect failed");
        }

        return 1;
    }

    redisReply* reply = (redisReply *)redisCommand(m_pContext, "SELECT %d", m_pCachePool->GetDBNum());
    if (reply && (reply->type == REDIS_REPLY_STATUS) && (strncmp(reply->str, "OK", 2) == 0)) {
        freeReplyObject(reply);
        return 0;
    } else {
        log("select cache db failed");
        return 2;
    }
}

const char* CacheConn::GetPoolName() {
    return m_pCachePool->GetPoolName();
}

string CacheConn::get(string key) {
    string value;

    if (Init()) {
        return value;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "GET %s", key.c_str());
    if (nullptr == reply) {
        log("redisCommand failed:%s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
    }

    if (REDIS_REPLY_STRING == reply->type) {
        value.append(reply->str, reply->len);
    }

    freeReplyObject(redisReply);
    return value;
}

string CacheConn::setex(string key, int timeout, string value) {
    string ret_value;

    if (Init()) {
        return ret_value;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "SETEX %s %d %s", key.c_str(), timeout, value.c_str());
    if (nullptr == reply) {
        log("redisCommand failed:%s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
    }

    ret_value.append(reply->str, reply->len);
    freeReplyObject(reply);

    return value;
}

string CacheConn::set(string key, string value) {
    string ret;

    if (Init()) {
        return ret;
    }

    redisReply* reply = redisCommand(m_pContext, "SET %s %s", key.c_str(), key.c_str());
    if (nullptr == reply) {
        log("redisCommand failed:%s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return ret;
    }

    ret.append(reply->str, reply->len);
    freeReplyObject(reply);
    
    return ret;
}

bool CacheConn::mget(const vector<string>& keys, map<string, string>& ret_value) {
    if (Init()) {
        return false;
    }

    if (keys.empty()) {
        return false;
    }

    string strKey;
    bool bFirst = true;
    for (auto it = keys.cbegin(); it != keys.cend(); ++it) {
        if (bFirst) {
            bFirst = false;
            strKey = *it;
        } else {
            strKey += " " + *it;
        }
    }

    if (strKey.empty()) {
        return false;
    }

    strKey = "MGET " + strKey:
    redisReply* reply = (redisReply*) redisCommand(m_pContext, "%s", strKey);
    if (nullptr == reply) {
        log("redisCommand failed:%s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return false;
    }

    if (REDIS_REPLY_ARRAY == reply->type) {
        for (auto i = 0; i < reply->elements; ++i) {
            redisReply* child_reply = reply->element[i];
            ret_value.insert(std::make_pair(keys[i], child_reply->str));
        }
    }

    freeReplyObject(reply);
    return true;
}

bool CacheConn::isExists(string &key) {
    if (Init()) {
        return false;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "EXISTS %s", key.c_str());

    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return false;
    }

    if (REDIS_REPLY_INTEGER == reply->type) {
        if (1 == reply->integer) {
            freeReplyObject(reply);
            return true;
        }
    }

    return f
    
    return false;
}

long CacheConn::hdel(string key, stirng field) {
    if (Init()) {
        return 0;
    }

    redisReply* reply = (redisReply*) rediscommend(m_pContext, "hdel %s %s", key, field);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
    }

    long ret_value = reply->integer;
    freeReplyObject(reply);

    return ret_value;
}

string CacheConn::hget(string key, string field) {
    string ret_value;
    if (Init()) {
        return 0;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pCachePool, "hget %s %s", key, field);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pCachePool);
        m_pCachePool = nullptr;
        return 0;
    }

    if (REDIS_REPLY_STRING == reply->type) {
        ret_value.append(reply->str, reply->len);
    }

    freeReplyObject(reply);
    return ret_value;
}

bool CacheConn::hgetAll(stirng key, map<string, string> ret_value) {
    if (Init()) {
        return false;
    }

    string value;

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "hgetall %s", key);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return false;
    }

    if ((REDIS_REPLY_ARRAY == reply->type) && (reply->elements % 2 == 0)) {
        for (auto i = 0; i < reply->elements; i += 2) {
            redisReply* field_reply  = reply->element[i];
            redisReply* value_reply =  reply->element[i+1];
            ret_value.insert(std::make_pair(field_reply, value_reply));
        }
    } else {
        freeReplyObject(reply);
        return false;
    }

    freeReplyObject(reply);
    return true;
}

long CacheConn::hset(string key, string value) {
    if (Init()) {
        return -1;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "hset %s %s", key, value);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return false;
    }

    long ret_value = reply->integer;
    return ret_value;
}

long CacheConn::hincrBy(string key, string field, long value) {
    if (Init()) {
        return -1;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "HINCRBY %s %s %d", key, field, value);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return -1;
    }

    long ret_value = reply->integer;

    freeReplyObject(reply);
    return ret_value;
}

long CacheConn::incrBy(string key, long value) {
    if (Init()) {
        return -1;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "incrby %s, %ld", key, value);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        return -1;
    }

    long ret_value = reply->integer;
    freeReplyObject(reply);
    return ret_value;
}

string CacheConn::hmset(string key, map<string, string>& hash) {
    string ret_value;
    if (Init()) {
        return ret_value;
    }
    int argc = hash.size() * 2 + 2;
    const char ** argv = new const char* [argc];

    argv[0] = "hmset";
    argv[1] = key.c_str();
    int i = 2;
    for (const auto& pair : hash) {
        argv[i++] = pair.first.c_str();
        argv[i++] = pair.second.c_str();
    }

    redisReply* reply = (redisReply*) redisCommandArgv(m_pContext, argc, argv, nullptr);
    
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        delete [] argv;
        return ret_value;
    }

    ret_value.append(reply->str, reply->len);
    delete [] argv;
    return ret_value;
}

bool CacheConn::hmget(string key, list<string>& fields, list<string>& ret_value) {
    if (Init()) {
        return false;
    }

    auto argc = fields.size() + 2;
    const char** argv = new char[argc];

    auto i = 0;
    argv[i++] = "hmget";
    argv[i++] = key.c_str();

    for (auto str : fields) {
        argv[i++] = str.c_str();
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, argc, argv, nullptr);
    if (nullptr == reply) {
        log("redisCommend failed %s", m_pContext->errstr);
        redisFree(m_pContext);
        m_pContext = nullptr;
        delete [] argv;
        return false;
    }

    if (REDIS_REPLY_ARRAY == reply->type) {
        for (auto i = 0; i < reply->elements; i++) {
            redisReply* ret_reply = reply->element[i];
            ret_value.push_back(ret_reply->integer);
        }
        freeReplyObject(reply);
        delete [] argv;
        return true;
    }
    
    delete [] argv;
    freeReplyObject(reply);
    return false;
}

long CacheConn::incr(string key) {
    if (Init()) {
        return -1;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "INCR %s", key.c_str());
    if (nullptr == reply) {
        redisFree(m_pContext);
        m_pContext = nullptr;
        return -1;
    }

    long ret_value = -1;

    if (REDIS_REPLY_INTEGER == reply->type) {
        ret_value = reply->integer;
    } else if (REDIS_REPLY_ERROR == reply->type) {
        log("redisCommend failed %s", reply->str);
    }

    freeReplyObject(reply);
    return ret_value;
}

long CacheConn::decr(string key) {
    if (Init()) {
        return -1;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "DECR %s", key.c_str());
    if (nullptr == reply) {
        redisFree(m_pContext);
        m_pContext = nullptr;
        return -1;
    }

    long ret_value = -1;

    if (REDIS_REPLY_INTEGER == reply->type) {
        ret_value = reply->integer;
    } else if (REDIS_REPLY_ERROR == reply->type) {
        log("redisCommend failed %s", reply->str);
    }

    freeReplyObject(reply);
    return ret_value;
}

long CacheConn::lpush(string key, string value) {
    if (Init()) {
        return 0;
    }

    redisReply* reply = (redisReply*) redisCommand(m_pContext, "");
}