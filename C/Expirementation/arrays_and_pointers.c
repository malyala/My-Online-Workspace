#include <stdio.h>



int main(){
    int x[3] = {1,2,3};
    printf("%d\n", *(x + 1)); // this returns 2!!!

    return 0;
}




