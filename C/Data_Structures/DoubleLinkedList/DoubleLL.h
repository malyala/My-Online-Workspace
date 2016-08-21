/*
List implemeneted with double linked list.
Notes:
	1) Accessing at index 0 is O(1)
	2) Accessing elsewhere (and changing at index i) is O(i)

*/
typedef struct DoubleLL DoubleLL;
typedef void (*DeallocFn)(void *);

//Constructors
DoubleLL *CreateDLL();
void InsertVal(DoubleLL *, void *, int); // the int is the index.

//Deconstructors
void DeleteIndex(DoubleLL *, DeallocFn, int);
void DeleteDLL(DoubleLL *, DeallocFn);

//Accessors
void *IndexValue(DoubleLL *, int);
int GetLen(DoubleLL *);

//Misc:
void PrintIntList(DoubleLL *);

