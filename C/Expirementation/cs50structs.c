#include <stdio.h>
#include <stdlib.h>

struct student
{
    int age;
    char *name;
};


void main()
{
    struct student s1;
    struct student s2 = {3, "s2"};

    s1=s2;
    printf("&s1:%ld\n&s2: %ld\n",
    &s1,
    &s2);
    
    printf("&(s1.age): %ld\n&(s2.age)%ld\n",
    &(s1.age),
    &(s2.age));

}
