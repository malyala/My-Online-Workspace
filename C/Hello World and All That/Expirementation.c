#include <stdio.h>

int main(){
    char astr[5];
    printf("give me you name: ");
    scanf("%s", &astr);
    printf("you gave me %s\n", astr);
    return 0;
}
/*
 * gcc allocates an extra spot for the string
 * other than that, this can accept 4 chars (with the terminator char \0 this makes 5 )
 */