#include <cstring>
#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <stdlib.h>
#include "CachePool.h"
#include "version.h"

int main(int argc, char * argv[]) {
    if ((argc == 2) && (strcmp(argv[1], "-v") == 0)) {
        printf("Server Version: DBProxyServer/%ss\n", VERSION);
        printf("Server Build: %s %s\n", __DATE__, __TIME__);
    }

    signal(SIGPIPE, SIG_IGN);
    srand(time(NULL));

    CacheManager* pCacheManager = CacheManager::getInstance();

    return 0;
}