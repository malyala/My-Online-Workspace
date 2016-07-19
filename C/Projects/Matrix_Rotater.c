/*
In this file I solve the problem of rotating an N x N matrix pi/4 rad clockwise (90 degrees clockwise)



*/

#include <stdio.h>
#include <stdlib.h>


static int Matrix_dimension;


int main()
{
    
    int  **matrix;
    printf("What is the matrix dim?: \n");
    scanf("%d", &Matrix_dimension);
    matrix =  (int **) malloc(Matrix_dimension * sizeof(int *)); 
    for (int i = 0; i < Matrix_dimension; ++i)
    {
        for(int j = 0; j < Matrix_dimension; ++j)
        {
            printf("What goes in cell with row %d and col %d\n", i, j);
            matrix[i] = (int *) malloc(Matrix_dimension * sizeof(int));
            scanf("%d", &(matrix[i][j]) );
        }
    }



    return 0;
}


