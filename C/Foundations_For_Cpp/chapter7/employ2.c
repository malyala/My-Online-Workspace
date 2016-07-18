/* employ2.c */

#include <stdio.h>
#include <stdlib.h>
#include "employ2.h"


struct Employee* createEmployee(char* first, char* last, char* title, int sal)
{
    Employee *toRet;
    toRet = malloc(sizeof(Employee));
    toRet->first= *first;
    toRet->last= *last;
    toRet->title= *title;
    toRet->salary= sal;
    return toRet;
}

char* getLast(struct Employee *emp)
{
    return emp->last;
}

char* getFirst(struct Employee* emp)
{
    return emp->first;
}
char* getTitle(struct Employee* emp)
{
    return emp->title;
}
int getSalary(struct Employee* emp)
{
    return emp->salary;
}
void setLast(struct Employee* emp, char* last)
{
    emp->last = last;
}
void setFirst(struct Employee* emp, char* first)
{
    emp->first=first;
}
void setTitle(struct Employee* emp, char* title)
{
    emp->title = title;
}
void setSalary(struct Employee* emp, int sal)
{
    emp->salary = sal;
}
void printEmployee(struct Employee* emp)
{
    printf("Name: %s, %s\n",
    emp->last,
    emp->first);
    printf("Title %s\n", emp->title);
    printf("Salary: %d", emp->salary);
}




