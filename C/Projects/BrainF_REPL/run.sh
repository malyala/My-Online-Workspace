#!/bin/bash

g++ -std=gnu++11 -c DoubleLL.c Stack.c BF_Array.c interpreter.c 

g++ -std=gnu++11 Stack.o BF_Array.o interpreter.o 
./a.out


