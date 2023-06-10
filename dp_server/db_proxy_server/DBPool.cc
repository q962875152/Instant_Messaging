#include "DBPool.h"

CResultSet::CResultSet(MYSQL_RES* res) {
    m_res = res;

    int num_fields = mysql_num_fields(m_res); //获取结果集中每一行数据所包含的字段数
    MYSQL_FIELD* fields = mysql_fetch_fields(m_res); //获取结果集中每个字段的详细信息，例如字段名、数据类型、长度等等。

    for (int i = 0; i < num_fields; i++) {
        m_key_map.insert(make_pair(fields[i].name, i));
    }
    free(fields); // 需要问下老师，这个需不需要释放
    m_row = nullptr;
}

CResultSet::~CResultSet() {
    if (nullptr != m_res) {
        mysql_free_result(m_res);
        m_res = nullptr;
    }
    freeMysqlRow(m_row);
}

bool CResultSet::Next() {
    freeMysqlRow(m_row); // 这个也需要问下老师，这个需不需要释放
    m_row = mysql_fetch_row(m_res);
    if (nullptr == m_row) {
        return false;
    } else {
        return true;
    }
}

int CResultSet::_GetIndex(const char* key) {
    auto it = m_key_map.find(key);
    if (it == m_key_map.end()) {
        return -1;
    } else {
        return it->second;
    }
}

int CResultSet::GetInt(const char* key) {
    int idx = _GetIndex(key);
    if (-1 == idx) {
        return 0; // 为什么要返回0呢？
    } else {
        return atoi(m_row[idx]);
    }
}

char* CResultSet::GetString(const char* key) {
    int idx = _GetIndex(key);
    if (-1 == idx) {
        return nullptr;
    } else {
        return m_row[idx];
    }
}

void CResultSet::freeMysqlRow(MYSQL_ROW row) {
    if (nullptr == m_res || nullptr == m_row) {
        return;
    }

    int num_fields = mysql_num_fields(m_res);
    for (int i = 0; i < num_fields; i++) {
        free(row[i]);
    }
}

//********************CPrepareStatement*************************//
CPrepareStatement::CPrepareStatement() \
            : m_stmt(nullptr), m_param_bind(nullptr), m_param_cnt(0) {
}

CPrepareStatement::~CPrepareStatement() {
    if (nullptr != m_stmt) {
        mysql_stmt_close(m_stmt);
        m_stmt = nullptr;
    }

    if (nullptr != m_param_bind) {
        delete [] m_param_bind;
        m_param_bind = nullptr;
    }
}

