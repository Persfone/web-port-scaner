#include <stdio.h>
#include <stdlib.h>

void scan_tcp(char *ip, int port, float timeout);

int main(int argc, char *argv[]) {

    if (argc < 5) {
        printf("Usage: ./scanner <ip> <protocol> <start> <end>\n");
        return 1;
    }

    char *ip = argv[1];
    char *protocol = argv[2];
    int start = atoi(argv[3]);
    int end = atoi(argv[4]);

    for (int port = start; port <= end; port++) {
        scan_tcp(ip, port, 0.5);
    }

    return 0;
}