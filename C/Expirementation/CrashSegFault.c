#include <stdio.h>

int main(){
    int *x;
    
    while(1){
        int *y = x;
        y += 100000000;
        x = (int *) 0;
        x = y;
    }
    
    return 0;
}