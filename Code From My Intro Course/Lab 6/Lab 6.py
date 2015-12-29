# -*- coding: utf-8 -*-


def adds(n):
    rt_5 = 5**0.5
    ret = ((1.0/rt_5) * (((1+rt_5)/2.0)**n-((1-rt_5)/2.0)**n)) -1
    return int(ret)

def old(n):
    return adds(n) / 1000000.0
    
def new(n):
    return adds(n) / 3000000.0

"""
    func_time(function, repeats):
      Run the function _function_ for _repeats_ iterations,
      then return the average elapsed time.

Note that "function" must take zero parameters, e.g.
    
>>> def sample_fib(): return fib(14)

Something too fast to measure easily, e.g. 100 microseconds,
will need to be run repeatedly. If you run it only once, as
in the example below, you'll get 0.0 most of the time, and
occasionally get the minimum measurable amount of time (0.001s?).
>>> func_time(sample_fib, 1)
0.0

Running a 100 microsecond function 10000 times should take about 0.1 second,
and 0.1s is short enough to not be tedious, but long enough to measure.
>>> func_time(sample_fib, 1000)   # doctest: +ELLIPSIS




"""

import time



def fib(n):
    # precondition(n is a positive integer)
    # postcondition(fib(n) is the nth element of the Fibonacci sequence
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def func_time(function, repeats=0, min_time=0.250):
    """
        Run FUNCTION for REPEATS repetitions,
         and return the average time taken.
        If REPEATS is 0 or missing,
         run for MIN_TIME (default 1/4sec) consecutive calls
    """
    r = repeats if repeats != 0 else 1
    done = False
    while not done:
        start = time.clock()
        for i in range(0,r):
            function()
        end = time.clock()
        if repeats>0 or end-start>min_time:
            done=True
        else:
            r = r*2
#    print("     R was "+str(r))
    return (end-start)/(r*1.0)

def times():
    for i in range(5,60,5):
        def sf():
            strange_fib(i)
        print "the time for " + str(i) +" s_fib is: ",  (func_time(sf))






def fib_time(n, repeats=0):
    def fib_n(): return strange_fib(n)
    return func_time(fib_n, repeats)

def print_fib_time(n, repeats):
    print("Time to find fib(",n,") was ", fib_time(n, repeats), "seconds")

# copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    # print "Result of doctest is:", result
    if result[0] == 0:
        print("Wahoo! Passed all " +str(result[1])+ " tests!")
    else:
        print("Rats!")

if __name__ == "__main__":
    _test()
    def nothing(): return
    print("Note: calling nothing seems to take about " + str(func_time(nothing, 1000000)) + " seconds on this computer")

def strange_fib(n):
    # precondition: same as fib(n) precondition
    # postcondition: returns the same thing as fib(n)
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        # The following line deserves a better comment than this:
        return 2*strange_fib(n-1) - strange_fib(n-3)


def operations_strange_fib(n):
    if n<4:
        return 0
    else:
        start = [0,0,2]
        for i in range(n-4):
            save = start[0]
            start[0] = start[1]
            start[1] = start[2]
            start[2] = 2 + start[1] + save
        
        return start[2]
        
        
for i in range(5,60,5):
    print operations_strange_fib(i)
