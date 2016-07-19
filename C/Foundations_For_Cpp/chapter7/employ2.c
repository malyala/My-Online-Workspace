/* employ2.c */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "employ2.h"




struct Employee* createEmployee(char *first, char *last, char *title, int sal)
{
    Employee *toRet;
    toRet = (Employee *) malloc(sizeof(Employee));
    memcpy(toRet->first, first, sizeof(first));
    memcpy(toRet->last, last, sizeof(last));
    memcpy(toRet->title, title, sizeof(title));
    toRet->salary = sal;
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
    memcpy(emp->last, last, sizeof(last));
}
void setFirst(struct Employee* emp, char* first)
{
    memcpy(emp->first, first, sizeof(first));
}
void setTitle(struct Employee* emp, char* title)
{
    memcpy(emp->title, title, sizeof(title));
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




