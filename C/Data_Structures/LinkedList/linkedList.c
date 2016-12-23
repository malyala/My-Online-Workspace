#include "linkedList.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct Node{
	void *val;
	struct Node *next;
} Node;


typedef struct linkedList{
	int len;
	Node *head;
	Node *tail;
} LL;
//Invariants: if len==0, head and tail are NULL
//Otherwise, the next of tail is NULL.


LL *CreateLL(){
	LL *ret = (LL *) malloc(sizeof(LL));
	if(ret != NULL){
		ret->len = 0;
		ret->head = ret->tail = NULL;
	}
	return ret; //this is NULL if malloc fails
}

Node *llIndexNode(LL *list, int index){
	assert((list->len)); //list must be non-empty to index
	assert((index > -1) && (index < (list->len)));
	Node *ret = list->head;
	for(int i = 0; i < index; ++i){
		ret = ret->next;
	}
	return ret;
}

void *llIndex(LL *list, int i){
	return llIndexNode(list, i)->val;
}

int llInsert(LL *list, void *val, int index){
	//We insert before the element at index index
	assert((index > -1) && (index <= (list->len)));
		//1. Make the node to insert
	Node *ret = (Node *) malloc(sizeof(Node));
	if(ret == NULL){
		return 1;
	}else{
		ret->val = val;
		ret->next = NULL;
	}
		//2. Insert that node properly
	if(list->len != 0){
		//Insert before the node at index index.
		//Append by inserting at index == list->len
		if(index==0){
			ret->next = list->head;
			list->head = ret;
		}else if(index==(list->len)){
			list->tail->next = ret;
			list->tail = ret;
		}else{
			Node *insertAfter = llIndexNode(list, index -1);
			ret->next = insertAfter->next;
			insertAfter->next = ret;
		}

	}else{
		list->head = ret;
		list->tail = ret;
	}
	list->len += 1;
	return  0;
}

int llAppend(LL *list, void *val){
	return llInsert(list, val, list->len);
}

int llLen(LL *list){
	return list->len;
}

void *llPop(LL *list, int index){
	assert(list->len); //Can't remove from an empty list
	assert((index > -1) && (index < list->len));
	void *ret;
	if(index==0){
		Node *hold = list->head;
		list->head = list->head->next; // This could be NULL
		ret = hold->val;
		free(hold);
		if(list->len == 1){
			list->tail = NULL;
		}
	}else{ 
		//a non-empty list with index>0
		//has 2 or more elems
		Node *hold = llIndexNode(list, index -1);
		Node *toFree = hold->next;
		ret = toFree->val;
		hold->next = toFree->next; //Could be NULL
		free(toFree);
		if (list->len==2){
			list->tail = list->head;
		}else if (index == (list->len)-1){
			list->tail = hold;
		}
	}
	list->len -= 1;
	return ret;
}



// --------------Testing------------------------


void print(LL *list){
	putchar('{');
	Node *start = list->head;
	for(int i = 0; i< llLen(list); ++i){
		printf("%d, ",*((int *) start->val) );
		start = start->next;
	}
	printf("}\n");
}

int main(){
	int x[4] = {1,2,3,4};
	int y[7] = {1,2,3,4,5,6,7};
	LL *test = CreateLL();
	LL *test2 = CreateLL();
	print(test2);
	//for(int i = 0; i<4; ++i){
	//	llAppend(test, x + i);
	//}
	for(int j=0; j<7; ++j){
		llAppend(test2, y+j);
		//print(test2);
		//printf("tail %p\n",test2->tail);
		//printf("tail val %d\n", *((int *) test2->tail)  );
	}

	//for(int i =0; i<4; ++i){
	//	printf("%d ", *((int *) llIndex(test, i )));
	//}
	//putchar('\n');
	//for(int i =0; i<4; ++i){
	//	printf("%d ", *((int *) llPop(test, llLen(test) - 1)));
	//}

	putchar('\n');
	printf("Misc testing of insert and pop.\nI trust index and len are fine.\n");
	printf("Original: ");
	print(test2);
	printf("tail val %d\n", *((int *) test2->tail->val)  );
	llPop(test2, 2);
	puts("llPop(test2, 2);\n");
	print(test2);
	printf("tail val %d\n", *((int *) test2->tail->val)  );
	llPop(test2, 0);
	puts("llPop(test2, 0);\n");
	print(test2);
	printf("tail val %d\n", *((int *) test2->tail->val)  );
	llPop(test2, 4);
	puts("llPop(test2, 4);\n");
	print(test2);
	printf("tail val %d\n", *((int *) test2->tail->val)  );
	int a = 24, b = 25, c = 26;
	llInsert(test2, &a, 0);
	puts("llInsert(test2, &a, 0);\n");
	print(test2);
	printf("tail val %d\n", *((int *) test2->tail->val)  );
	llInsert(test2, &b, 5);
	llInsert(test2, &c, 3);
	puts("llInsert(test2, &b, 5);\nllInsert(test2, &c, 3);\n");
	print(test2);
	printf("tail val %d\n", *((int *) test2->tail->val)  );
	return 0;
}




