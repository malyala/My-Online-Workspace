#include <stdio.h>
#include <stdlib.h>
#include "Stack.h"
#include "BF_Array.h"
#define MAX_INPUT 41

typedef struct LoopStart{
	int BF_cell_pointer; //pointer in BF_Array object
	int input_pointer;
} LoopStart;

//Declarations:
void BF_repl();
void take_input(char *);


int main(){
	char test[50];
	take_input(test);
	return 0;
}

void print_startmessage(){
	printf("Welcome to Divesh's BrainF REPL.\n");
	printf("This is version 1.0.\n");
	printf("Input can be up to %d characters.\n", MAX_INPUT - 1);
}

void take_input(char *target){
	printf(">>> ");
	fgets(target, MAX_INPUT - 1, stdin);
}

void ExecuteCommand(BF_Array *, char);

void BF_repl(){
	int repl_status = 1;
	char input[MAX_INPUT];
	print_startmessage();
	while(repl_status){
		BF_Array *Array = CreateBF_Array();
		take_input(&input);
		if(input[0] == '*'){
			repl_status = 0;
			continue;
		}
		int InputPointer = 0;
		Stack *LoopStack = CreateStack();
		while(input[InputPointer] != '\0'){
			char current_char = input[InputPointer];
			if(current_char == '['){
				LoopStart *x = (LoopStart *) malloc(sizeof(LoopStart));
				x->input_pointer = InputPointer + 1;
				x->BF_cell_pointer = GetPtr(Array);
				// If we did not malloc above, we would change the value
				//of the variable x and mess up the stack
				Push(LoopStack, x);
				InputPointer++;
			}else if(current_char == ']'){
				LoopStart most_recent_loop = *((LoopStart *) Top(LoopStack));
				int cellPtr = most_recent_loop.BF_cell_pointer;
				int cellVal = IndexVal(Array, cellPtr);
				if(cellVal == 0){
					Pop(LoopStack, free);
					InputPointer++;
				}else{
					InputPointer = most_recent_loop.input_pointer;
				}
			}else{
				ExecuteCommand(Array, current_char); //To implement
				InputPointer++;
			}	
		}
		DeleteBF_Array(Array);
	}
}



