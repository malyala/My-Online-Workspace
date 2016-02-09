"""
Test Cases for fib()

>>> fib(5)
5
>>> fib(1)
1
>>> fib(2)
1
>>> fib(1) + fib(2)
2
>>> fib(10)
55

"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)

# Hopefully the following will stop any infinite loops without killing anything correct
import resource
resource.setrlimit(resource.RLIMIT_CPU, [3, 5])


def fib(n):
    precondition(is_integer(n) and n>=1)
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all fib() tests"
