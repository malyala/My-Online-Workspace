/* Employee.h  */
#include <stdio.h>
#include <stdlib.h>
#include "employee.h"
#define MAX_EMP 4
#define NAMESIZE 30

// ask heman about stupid io issues in C later



typedef struct employee
{
    char last[NAMESIZE];
    char first[NAMESIZE];
    int salary;
} employee;


static int NumEmployees = 0;
static employee Workers[MAX_EMP];

int addEmployee(void)
{
    char c;
    while((c = getchar()) != '\n' && c != EOF)
               /* discard the character */;
 
    if (NumEmployees == MAX_EMP)
        return -1;
    printf("First Name: ");
    fgets(Workers[NumEmployees].first, NAMESIZE - 1, stdin); 
    printf("Last Name: ");
    fgets(Workers[NumEmployees].last, NAMESIZE - 1, stdin); 
    printf("Salary: ");
    scanf("%d", &(Workers[NumEmployees].salary)); 
    NumEmployees += 1;
    return NumEmployees -1;
}

int printEmployee(int i)
{
    if (i >= NumEmployees)
        return -1;
    puts(Workers[i].first);
    return i;
}


int numEmployees(void)
{
    return NumEmployees;
}



