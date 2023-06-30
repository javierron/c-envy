#include <stdio.h>

int very_important_function(char data[], int length){
    printf("performing operation of high relevance on data!\n");
    printf("data: %s | length: %d \n", data, length);
    return 0;
}int main(){
    very_important_function("Hello World!", 12);
}