#include <stdio.h>
#include <stdlib.h>

struct Person
{
    char *name;
    int age;
    int college_year;

};

void printperson(struct Person aperson)
{
    printf("Random guy information %s %d %d\n",
    aperson.name,
    aperson.age,
    aperson.college_year);

}

int main()
{
    
    struct Person Divesh, Bob;
    struct Person *Rando;

    Bob = {"Bob Mcphereson", 22, 3};
    Divesh = Bob;
    puts("Divesh:");
    printperson(Divesh);
    puts("Bob:");
    printperson(Bob);
    printf("Divesh Pointer: %p\n",
    &Divesh);
    printf("Bob Pointer: %p\n",
    &Bob);


    Rando = malloc(sizeof(struct Person));
    *Rando = {"Random Guy", 35, 2};
    printperson(Rando);


}














