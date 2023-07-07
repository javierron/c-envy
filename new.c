#include <stdio.h>

int original(char data[], int length){
    printf("performing very important operation on data!\n");
    printf("data: %s | length: %d \n", data, length);
    return 0;
}

int variant(char data[], int length){
    printf("performing operation of high relevance on data!\n");
    printf("data: %s | length: %d \n", data, length);
    return 0;
}
int main(){
    original("Hello World!", 12);
	int x1 =     variant("Hello World!", 12);
}