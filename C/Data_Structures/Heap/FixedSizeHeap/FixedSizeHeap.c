#include "FixedSizeHeap.h"
#include <stdio.h>
#include <stdlib.h>

// Declarations

void swap(Heap *heap, int i, int j)
void maxHeapify(Heap *heap, int index, comparer comp);
int left(int);
int right(int);
int parent(int);
int HeapSize(Heap *heap);

// End of declarations

struct Heap{
	int length;
	int maxLength;
	void **heapArray;
};


Heap * CreateHeap(int length){
	Heap *NewHeap = (Heap *) malloc(sizeof(Heap));
	NewHeap->length = 0;
	NewHeap->maxLength = length;
	NewHeap->heapArray = (void **) malloc(length * sizeof(void *));
	return NewHeap;
}

void * HeapMaxPeek(Heap * heap){
	return HeapSize(heap) ? (heap->heapArray)[0] : NULL;
}

void * HeapMaxPop(Heap *heap, comparer comp){
	void **arr = heap->heapArray;
	max = arr[0];
	if(HeapSize(heap)){
		arr[0] = arr[heap->length - 1];
		(heap->length) -= 1;
		maxHeapify(heap, 0, comp);
		return max;
	}else{
		return NULL;
	}

}

int HeapInsert(Heap *heap, void *val, comparer comp){
	assert(val != NULL);
	if(HeapSize(heap) != heap->maxLength){
		(heap->length) += 1;
		void **arr = heap->heapArray;
		arr[length] = val;
		int currentIndex = length;
		int parentIndex = parent(length);
		while(comp(arr[parentIndex], arr[currentIndex])){
			swap(heap, currentIndex, parentIndex);
			currentIndex = parentIndex;
			parentIndex = parent(currentIndex);
		}
		return 1;
	}else{
		return 0;
	}
}

int HeapSize(Heap *heap){
	return heap->length;
}



// Helper functions ---------------------------------------
int inRange(Heap *heap,  int i){
	return i >=0 && i < (heap->length);
}


void swap(Heap *heap, int i, int j){
	assert(inRange(heap, i) && inRange(heap, j));
	void **arr = heap->heapArray;
	void *temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}


void maxHeapify(Heap *heap, int index, comparer comp){
	int maybeLeft = left(index);
	int maybeRight = right(index);
	int left = inRange(heap, maybeLeft) ? maybeLeft : index;
	int right = inRange(heap, maybeRight) ? maybeRight : index;
	void **arr = heap->heapArray;
	void *current = arr[index];
	void *leftChild = arr[left];
	void *rightChild = arr[right];
	if(comp(leftChild, rightChild) && comp(current, rightChild)){
		swap(heap, index, right);
		maxHeapify(heap, right);
	}else if(comp(current, leftChild)){
		swap(heap, index, left);
		maxHeapify(heap, left);
	}
}
//To reason about the above lines, observe that 
//if current is the max, neither cases run.
//So, assume that current < leftChild or
//current < rightChild


//These are the index computations in the heap array
int left(int i){
	return (i<<1) + 1;
}
int right(int i){
	return (i<<1) + 2;
}
int parent(int i){
	return i>>1;
}

// Testing---------------------------------

int compare(void *a, void *b){
	return *((int *) a) < *((int *) b);
}

int view(void *a){
	return *((int *) a);
}

int main(){
	Heap *test = CreateHeap(6);
	int elems[6] = {2,34,1,67,32,5};
	for(int i=0; i<6; ++i){
		HeapInsert(test, elems + i, compare);
	}
	for(int i=0; i<6; ++i){
		printf("%d, ", view(HeapMaxPop(test, comp)));
		// This should be in sorted order
	}
	putchar('\n');
	return 0;
}






