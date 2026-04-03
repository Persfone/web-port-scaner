#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include "tcp.h"

void scan_tcp(char *ip, int port, float timeout) {

    int sock;
    struct sockaddr_in target;

    sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock < 0) {
        printf("%d TCP error\n", port);
        return;
    }

    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr(ip);

    int result = connect(sock, (struct sockaddr *)&target, sizeof(target));

    if (result == 0)
        printf("%d TCP open\n", port);
    else
        printf("%d TCP closed\n", port);

    close(sock);
}