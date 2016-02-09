from fib_time import *
import time

for i in range(5, 100, 5):
    print("[At time " + str(time.clock()) + " finding fib(" + str(i) + ")...]")
    t=fib_time(i)
    print("Finding fib(" + str(i) + ") took "+str(t)+"s")
    print("")
