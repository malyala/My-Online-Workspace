#include <stdio.h>

int main(){
    float inp;
    puts("give me a float: ");
    scanf("%f", &inp);
    if (inp >= 0){
        inp += 0.5;    
    } 
    else{
        inp -= 0.5;
    }
    printf("Rounded: %d\n",(int) inp);
}