#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *x;
    x = malloc(3 * sizeof(int));
    printf("sizeof(x): %lu\n", sizeof(x)); // this prints 8
    
    int y[2][3] = {{1,2,3}, {4,5,6}};
    printf("sizeof(y): %ld\n", sizeof(y));
    
    return 0;
}
