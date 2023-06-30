#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int length;
    char** params;
    char* method;
} config;

int main(){
    config *conf = malloc(sizeof(config));
    conf->length = 1;
    conf->params = malloc(sizeof(char*) * conf->length);
    conf->method = malloc(sizeof(char) * 10);
    conf->method = "sendfrom";
    conf->params[1] = malloc(sizeof(char) * 100);
    conf->params[1] = "tb1qq0r36alhargdp8z7caz8r0zxnlm7w758mzc7m5";
    int i;

    for (i = 0; i < conf->length; i++) {
        //do something
    }

    printf("Hello World!\n");
    return 0;
}