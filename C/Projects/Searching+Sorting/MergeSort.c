/*
This is a generic merge sort that takes
	1) An array
	2) The length of the array
	3) Size of each element
	4) A function that takes pointers to elements p1, p2
		and returns 1 iff *p1 < *p2
		and 0 otherwise

	and returns a sorted array (ascending order) with no side effects performed.

For now, memory efficency is not considered. This is a project to be returned to.

*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "../swap.c" // probably repeats some libraries, fix this later
void printIntArr(int *, int);
void Merge (void *, void *, int, int, size_t, int(*fn)(void *, void*));

void * MergeSort(void *arr, int len, size_t elem_sz, int (*fn)(void *, void *)){
	void *ret = malloc( len * elem_sz );
	if (len == 2){
		if (!fn(arr, arr + elem_sz))
			swap(arr, arr + elem_sz, elem_sz);
		return arr;
	} else if (len ==1 ){
		return arr;
	} else {
		int split = len / 2;
		void *first_half = MergeSort(arr, split, elem_sz, fn);
		void *second_half = MergeSort((arr + (split * elem_sz)),len - split, elem_sz, fn);
		ret = Merge(first_half, second_half,split, len - split, elem_sz, fn);
		free(first_half);
		free(second_half);
		return ret; // whatever calls this should eventually free ret
	}


//call from merge should be freed
}

void * Merge (void *arr1, void *arr2, int len1, int len2, size_t size, int (*fn)(void *, void *)){
	char *ret = (char *) malloc((len1 + len2)* size);
	int retPtr = 0;
	int p1 = 0, p2 = 0;
	while (p1 != len1 && p2 != len2){
		int check = fn((arr1 + (p1 * size)), (arr2 + (p2 * size)));
		if (check){
			memcpy((ret + (retPtr * size)), (arr1 + (p1 * size)), size);
			p1++;
		} else{
			memcpy((ret + (retPtr * size)), (arr2 + (p2 * size)), size);
			p2++;
		}
	retPtr++;
	}
	void *RemainderArr = p1 == len1 ? arr2 : arr1;
	int RemainderPtr = p1 == len1 ? p2 : p1;
	int RemainderLen = p1 == len1 ? len2 : len1;
	memcpy((ret + (retPtr * size)), (RemainderArr + (size * RemainderPtr)), (size * (RemainderLen - RemainderPtr)));
	return (void *) ret;
}

int IntComp(void *, void *);
void printIntArr(int *arr, int len){
	printf("{");
	for (int i = 0; i< len; ++i)
		printf("%d, ", arr[i]);
	printf("}\n");
}

int main(){
	int *a = (int *) malloc(2*sizeof(int));
	int *b = (int *) malloc(4 * sizeof(int));
	a[0] = 1; a[1] = 6; b[0] = 2; b[1] = 3; b[2]=8; b[3]=12;
	int *merge = (int *) Merge(a, b, 2, 4, sizeof(int), IntComp);
	printIntArr(merge, 6);
	return 0;
}

int IntComp(void *a, void *b){
	int x = *((int *) a), y = *((int *) b);
	return x < y;
}



