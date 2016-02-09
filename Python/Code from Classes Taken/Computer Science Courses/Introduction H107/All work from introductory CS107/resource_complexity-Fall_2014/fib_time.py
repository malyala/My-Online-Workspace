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
from fib import *
from strange_fib import *

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




def print_fib_time(n, repeats):
    print("Time to find fib(",n,") was ", fib_time(n, repeats), "seconds")





def fib_time(n, repeats=0):
    def fib_n(): return strange_fib(n)
    return func_time(fib_n, repeats)

for i in range(5,60,5):
    print "The time for strange_fib of ",i," is this: ", fib_time(i)


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

