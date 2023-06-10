#include <stdint.h>
#include <mysql/mysql.h>
#include <string>
#include <list>
#include <map>
#include "Thread.h"

#define MAX_ESCAPE_STRING_LEN 10240

using namespace std;

class CResultSet {
public:
    CResultSet(MYSQL_RES* res);  // MYSQL_RES表示查询结果集
    virtual ~CResultSet();

    bool Next();
    int GetInt(const char* key);
    char* GetString(const char* key);
private:
    int _GetIndex(const char* key);
    void freeMysqlRow(MYSQL_ROW row);

    MYSQL_RES*          m_res;
    MYSQL_ROW           m_row;  // MYSQL_ROW表示查询结果集中的一行数据
    map<string, int>    m_key_map;
};

/*
 * TODO:
 * 用MySQL的prepare statement接口来防止SQL注入
 * 暂时只用于插入IMMessage表，因为只有那里有SQL注入的风险，
 * 以后可以把全部接口用这个来实现替换
 */

class CPrepareStatement {
public:
    CPrepareStatement();
    virtual ~CPrepareStatement();

    bool Init(MYSQL* mysql, string& sql);  // MYSQL表示MySQL连接的句柄

    void SetParam(uint32_t index, int& value);
    void SetParam(uint32_t index, uint32_t& value);
    void SetParam(uint32_t index, string& value);
    void SetParam(uint32_t index, const string& value);

    bool ExecuteUpdate();
    uint32_t GetInsertId();

private:
    MYSQL_STMT* m_stmt;  // MYSQL_STMT表示一条预处理 SQL 语句的句柄
    MYSQL_BIND* m_param_bind;  // MYSQL_BIND表示数据绑定的相关信息
    uint32_t    m_param_cnt;
};

class CDBPool;

class CDBConn {
public:
    CDBConn(CDBPool* pDBPool);
    virtual ~CDBConn();
    int Init();

    CResultSet* ExecuteQuery(const char* sql_query);
    bool ExecuteUpdate(const char* sql_query);
    char* EscapeString(const char* content, uint32_t content_len);

    uint32_t GetInsertId();

    const char* GetPoolName();
    MYSQL* mJ_mysql;
    char m_escape_string[MAX_ESCAPE_STRING_LEN + 1];
};

class CDBPool {
public:
    CDBPool(const char* pool_name, const char* db_server_ip, uint16_t db_server_port, \
            const char* username, const char* password, const char* db_name, int max_conn_cnt);
    virtual ~CDBPool();

    int Init();
    CDBConn* GetDBConn();
    void RelDBConn(CDBConn* pConn);

    const char* GetPoolName() {}
private:
    string m_pool_name;
    string m_db_server_ip;
    uint16_t m_db_server_port;
    string m_username;
    string m_password;
    string m_db_name;
    int m_db_cur_conn_cnt;
    int m_db_max_conn_cnt;
    list<CDBConn*>  m_free_list;
    CThreadNotify   m_free_notify;
};

class CDBManager {
public:
    virtual ~CDBManager();
    static CDBManager* getInstance();

    int Init();

    CDBConn* GetDBConn(const char* dbpool_name);
    void RelDBConn(CDBConn* pConn);
private:
    CDBManager();

private:
    static CDBManager* s_db_manager;
    map<string, CDBPool> m_dbpool_map;
};