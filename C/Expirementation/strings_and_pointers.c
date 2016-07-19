#include <stdlib.h>
#include <stdio.h>


int main()
{
    char x[4]= "abc";
    char *y;
    y = (char *) malloc(4 * sizeof(char));
    y[0] = 'a';
    y[1] = 'b';
    y[2] = 'c';
    y[3] = '\0';
    printf("X is: %s, Y is %s\n",x,y);
    
    //Let's assign y differently!
    y = "def";
    printf("After y='def'; y is %s\n", y);



    //Also
    char *z;
    z = malloc(6);
    z ="hello";
    printf("Z is %s\n",z);
    printf("Sizeof(z): %d\n", sizeof(z));
    


    return 0;
}





