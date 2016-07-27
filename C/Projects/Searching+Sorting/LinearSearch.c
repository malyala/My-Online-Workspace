#include <stdio.h>
#include <stdlib.h>

enum boolean {False, True};

boolean LinearSearch(int * array, int len, int item)
{
	for (int i=0; i < len; ++i)
	{
		if (array[i]==item)
			return True;
	}
	return False;
}

int main()
{
	int *arr = (int *) malloc(4 * sizeof(int));
	arr[0] = 1; arr[1] = 2; arr[2] = 3; arr[3] = 4;
	printf("Search test 1: %d\n", LinearSearch(arr, 4,4));
	printf("Search test 0: %d\n", LinearSearch(arr, 4,0));
	free(arr);
	return 0;
}
