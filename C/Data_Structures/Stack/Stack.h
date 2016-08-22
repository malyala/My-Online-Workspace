
typedef void (*DeallocFn)(void *);
typedef DoubleLL Stack;
Stack *CreateStack();
void Push(Stack *, void *value);
void *Top(Stack *);
void Pop(Stack *, DeallocFn);

//The DeallocFn frees the memory of *value when it takes in the pointer, value.


