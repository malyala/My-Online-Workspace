"""
This should not be visible to students.
"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *

# strange_fib: compute fib(n) in a strange way
#  This may be faster than the obvious recursive approach,
#  though as we'll see later, there are several ways that are much faster
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


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
