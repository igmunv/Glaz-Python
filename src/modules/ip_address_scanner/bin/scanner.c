#define ADR_SIZE 15

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char * argv[])
{
    // if (argc < 2+1){
    //     printf("[!] argc is null\n");
    //     return -1;
    // }

    unsigned char ip_address_musor[ADR_SIZE+1];
    unsigned char mask_musor[ADR_SIZE+1];
    char c;
    char i, j;
    char f = 0;
    while ((c = getchar()) != EOF){
        if (c == '-'){
            f = 1;
            ip_address_musor[i] = '\0';
            i = 0;
        }
        else{
            if (f) mask_musor[i] = c;
            else ip_address_musor[i] = c;
            i++;
            j++;
        }
    }
    mask_musor[i] = '\0';

    printf("ip_m: %s\n", ip_address_musor);
    printf("ms_m: %s\n", mask_musor);

    char ip_address[4];
    char mask[4];

    char byte[4]  = {0,0,0,0};
    char byte_i = 0;
    f = 0;
    for (short i = 0; i < ADR_SIZE; i++){
        char b = ip_address_musor[i];

        if (b != 0x2e){ // != .
            byte[byte_i] = b;
            byte_i++;
        }
        else if (b == 0x2e || (b == '\0' )){
            byte[byte_i] = '\0';


            ip_address[f] = atoi(byte);
            printf("%04X\n", ip_address[f]);

            f++;
            byte_i = 0;
            memset(byte, 0, sizeof(byte));
        }
    }




    // 2d

    return 0;
}
