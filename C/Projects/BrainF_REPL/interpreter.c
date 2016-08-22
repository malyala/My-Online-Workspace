#include <stdio.h>
#include <stdlib.h>
#include "Stack.h"
#include "BF_Array.h"
#define MAX_INPUT 41

//Declarations:
void BF_repl();
void take_input(char *);


int main(){
	BF_repl();
	return 0;
}

void print_startmessage(){
	printf("Welcome to Divesh's BrainF REPL.\n");
	printf("This is version 1.0.\n");
	printf("Input can be up to %d characters.\n", MAX_INPUT - 1);
	printf("Give a * to end the repl.\n");
}

void take_input(char *target){
	printf ("\e[1;34m>>> \e[0m");
	fgets(target, MAX_INPUT - 1, stdin);
}

void ExecuteCommand(BF_Array *arr, char command){
	switch(command){
		case '+':
			Increment(arr);
			break;
		case '-':
			Decrement(arr);
			break;
		case '>':
			MoveRight(arr);
			break;
		case '<':
			MoveLeft(arr);
			break;
		case '.':
			PrintValue(arr);
			break;
		case ',':
			StoreValue(arr);
			break;
	}
}

void BF_repl(){
	int replStatus = 1;
	char *input = (char *) malloc(MAX_INPUT);
	BF_Array *Array = CreateBF_Array();
	print_startmessage();
	while(replStatus){
		take_input(input);
		if(input[0] == '*'){
			replStatus = 0;
			continue;
		}
		int InputPointer = 0;
		Stack *LoopStack = CreateStack();
		while(input[InputPointer] != '\0'){
			char CurrentChar = input[InputPointer];
			if(CurrentChar == '['){
				int *x= (int *) malloc(sizeof(int));
				(*x) = InputPointer + 1;
				// If we did not malloc above, we would change the value
				//of the variable x and mess up the stack
				Push(LoopStack, x);
				InputPointer++;
			}else if(CurrentChar == ']'){
				if(GetVal(Array) == 0){
					Pop(LoopStack, free);
					InputPointer++;
				}else{
					InputPointer = *((int *) Top(LoopStack));
				}
			}else{
				ExecuteCommand(Array, CurrentChar);
				InputPointer++;
			}	
		}
		DeleteStack(LoopStack, free);
	}
	DeleteBF_Array(Array);
	free(input);
}


