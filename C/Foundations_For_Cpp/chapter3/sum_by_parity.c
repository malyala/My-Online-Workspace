#include <stdio.h>
#include <stdlib.h>
int main()
{
    /*
    This works assuming that we don't get too large 
    inputs or anything messy
    with the integer storage...
    */
    long int SumOfOdds =0, SumOfEvens=0;
    int AmtOfInts, temp;
    printf("How many integers would you like to give me?");
    scanf("%d", &AmtOfInts);
    AmtOfInts = abs(AmtOfInts); // I don't care if the user gives a negative
    for (AmtOfInts; AmtOfInts > 0; AmtOfInts--)
    {
        printf("Give me an integer: ");
        scanf("%d", &temp);
        if ((temp % 2))
        {
            SumOfOdds += temp;
        } else
        {
            SumOfEvens += temp;
        }
    }

    printf("SumOfEvens = %ld and SumOfOdds = %ld\n",
    SumOfEvens,
    SumOfOdds);
    return 0;
}
