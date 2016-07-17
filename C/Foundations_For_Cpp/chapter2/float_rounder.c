#include <stdio.h>

int main(){
    float inp;
    printf("give me a float: ");
    scanf("%f", &inp);
    float given = inp;
    if (inp >= 0){
        inp += 0.5;    
    } 
    else{
        inp -= 0.5;
    }
    printf("Rounded %f to %d\n", given, (int) inp);
}
