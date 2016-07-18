#include <stdio.h>
/*

*/
int main()
{
    int a = 3;
    if(1)
    {
        printf("a is %d\n", a);
        int a = 4, b;
        printf("a is %d\n", a);

        printf("b is default val %d\n", b);
    }
    printf("a is %d\n",a);
    return 0;
}
