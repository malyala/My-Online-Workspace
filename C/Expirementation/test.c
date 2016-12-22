#include <stdio.h>

int main(){
	int *y;
	int z[2] = {4,5};

	int x[2] = {1,2};
	printf("%p\n", &y);
	printf("%p\n", &x);
	
	x = z;

}


