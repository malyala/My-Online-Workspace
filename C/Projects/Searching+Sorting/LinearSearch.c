#include <stdio.h>
typedef enum bool {false, true} bool;

bool LinearSearch(int * array, int len, int item)
{
	for (int i=0; i < len; ++i)
	{
		if (array[i]==item)
			return true;
	}
	return false;
}

int main()
{
	int *arr = malloc(4 * sizeof(int));
	arr[0] = 1; arr[1] = 2; arr[2] = 3; arr[3] = 4;
	printf("Search test 1: %d\n", LinearSearch(arr, 4,4));
	printf("Search test 0: %d\n", LinearSearch(arr, 4,0));
	return 0;
}
