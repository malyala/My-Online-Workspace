#include <stdlib.h>
#include <stdio.h>


int main()
{
    char x[4]= "abc";
    char *y;
    y = malloc(4);
    *y = "abc";
    printf("X is: %s, Y is %s\n",
    x,
    y);

    return 0;
}





