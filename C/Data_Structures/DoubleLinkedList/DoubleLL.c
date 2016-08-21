#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	void *value;
	struct Node *next = NULL;
	struct Node *prev = NULL;
} Node;

typedef struct DoubleLL{
	Node *head;
	int length = 0;
} DoubleLL;


DoubleLL *CreateDLL(){
	DoubleLL *ret = (DoubleLL *) malloc(sizeof(DoubleLL));
	return ret;
}

int GetLen(DoubleLL *list){
	return list->length;
}

void PrintIntList(DoubleLL *list){
	Node *currentNode = list->head;
	printf("{");
	int len = list->length;
	for(int i = 0;i < len; i++){
		printf("%d", *((int *) currentNode->value));
		printf(", ");
		currentNode = currentNode->next;
	}
	printf("}\n");
}

//Note: getting to the head is easy. Use this in stack implementation.
Node *IndexNode(DoubleLL *list, int i){
	//Precond: Non-empty list and 0 <= i <= len
	Node *ret = list->head;
	for(i;i > 0;--i){
		ret = ret->next;
	}
	return ret;
}

void *IndexValue(DoubleLL *list, int i){
	//Precond: Non-empty list and 0 <= i <= len
	return IndexNode(list, i)->value;
}

DoubleLL *InsertVal(DoubleLL *list, void *val, int i){
	//if empty list, i is 0, else 0 <= i <= len
	if(!(list->length)){
		list->head = (Node *) malloc(sizeof(Node));
		list->head->value = val;
		list->length = 1;
	}else{
		Node *ToInsert = (Node *) malloc(sizeof(Node));
		ToInsert->value = val;
		Node *CurrentNode = IndexNode(list, i);
		Node *PrevNode = CurrentNode->prev;
		CurrentNode->prev = ToInsert;
		PrevNode->next = ToInsert;
		ToInsert->next = CurrentNode;
		ToInsert->prev = PrevNode;
		list->length += 1;
	}
}


/* Testing */
int main(){
	int a=1, b=2, c=3, d=4, e=5;
	DoubleLL *test = CreateDLL();
	InsertVal(test, &a, 0);
	InsertVal(test, &b, 1);
	PrintIntList(test);
	return 0;
}
/*    */

