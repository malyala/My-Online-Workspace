/* Just a generic swap between 2 variables
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void swap(void *a,void *b, size_t size){
    char *temp;
    temp = malloc(size);
    (*temp) = *((char *) a);
    memcpy(a, b, size);
    memcpy(b, temp, size);
}

int main(){
    int a = 3, b = 4;
    swap(&a,&b, sizeof(int));
    printf("a is %d and b is %d \n", a, b);
    return 0;
}
