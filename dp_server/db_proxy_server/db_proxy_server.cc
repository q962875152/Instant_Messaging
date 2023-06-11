#include <cstring>
#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <stdlib.h>
#include "CachePool.h"
#include "DBPool.h"
#include "version.h"
#include "ConfigFileReader.h"
#include "EncDec.h"

string strAudioEnc;
int main(int argc, char * argv[]) {
    if ((argc == 2) && (strcmp(argv[1], "-v") == 0)) {
        printf("Server Version: DBProxyServer/%ss\n", VERSION);
        printf("Server Build: %s %s\n", __DATE__, __TIME__);
    }

    signal(SIGPIPE, SIG_IGN);
    srand(time(NULL));

    CacheManager* pCacheManager = CacheManager::getInstance();
    if (!pCacheManager) {
        log("CacheManager init failed");
        return -1;
    }

    CDBManager* pCDBManager = CDBManager::getInstance();
    if (!pCDBManager) {
        log("CDBManager init failed");
        return -1;
    }

    puts("db init success");
    // 主线程初始化单例，不然在工作线程可能会出现多次初始化
    //...

    CConfigFileReader config_file("dbproxyserver.conf");

    char* listen_ip = config_file.GetConfigName("ListenIP");
    char* str_listen_port = config_file.GetConfigName("ListenPort");
    char* str_thread_num = config_file.GetConfigName("ThreadNum");
    char* str_file_site = config_file.GetConfigName("MsfsSite");
    char* str_aes_key = config_file.GetConfigName("aesKey");

    if (!listen_ip || !str_listen_port || !str_thread_num || !str_file_site || !str_aes_key) {
        log("missing ListenIp/ListenPort/ThreadNum/MsfsSite/aesKey, exit...");
        return -1;
    }

    if (strlen(str_aes_key) != 32) {
        log("aes key is invalied");
        return -2;
    }

    string strAesKey(str_aes_key, 32);
    CAes cAes = CAes(strAesKey);  // aes是一种对称加密算法
    string strAudio = "[语音]";
    char* pAudioEnc;
    uint32_t nOutLen;
    if (cAes.Encrypt(strAudio.c_str(), strAudio.length(), &pAudioEnc, nOutLen) == 0) {
        strAudioEnc.clear();
        strAudioEnc.append(pAudioEnc, nOutLen);
        cAes.Free(pAudioEnc);
    }

    uint16_t listen_port = atoi(str_listen_port);
    uint32_t thread_num = atoi(str_thread_num);

    string strFileSite(str_file_site);
    CAudioModel::getInstance()->setUrl(strFileSite);  // 未实现

    int ret = netlib_init();



    return 0;
}