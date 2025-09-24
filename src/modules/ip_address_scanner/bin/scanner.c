#define ADR_SIZE 15

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ping.c"

int main(int argc, char * argv[])
{
    unsigned char ip_address_musor[16];
    int i = 0;
    char c;
    while ((c = getchar()) != EOF){
        ip_address_musor[i] = c;
        i++;
    }
    ip_address_musor[i] = '\0';

    int ping_result = ping(&ip_address_musor);

    if (ping_result == 0) printf("[+] %s\n", ip_address_musor);


    return 0;
}
