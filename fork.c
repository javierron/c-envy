#include <stdio.h>

int very_important_function(char data[], int length){
    printf("performing very important operation on data!\n");
printf(" PWND! ");
    printf("data: %s | length: %d \n", data, length);
    return 0;
}

int main(){
    very_important_function("Hello World!", 12);
}