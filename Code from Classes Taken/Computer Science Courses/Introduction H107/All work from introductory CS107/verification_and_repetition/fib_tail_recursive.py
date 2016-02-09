"""

>>> fib(5)
5

>>> fib(1)
1

>>> fib(2)
1

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


# original fibonacci function for use in assertions, postconditions, preconditions, etc.
def orig_fib(n):
    precondition(is_integer(n) and n>=1)
    # postcondition: gives the Nth number of the Fibonacci sequence
    if n == 1 or n == 2:
        return 1
    else:
        return orig_fib(n-1) + orig_fib(n-2)


def tr_fib(n, term, one_before, current):
    if (n == term):
        return current
    else:
        return tr_fib(n, term+1, current, current+one_before)

def fib(n):
    precondition(isinstance(n, int) and n>=1)
    if (n == 1):
        postcondition(1 == orig_fib(n)) # i.e., we're about to return the 1st number in the Fibonacci sequence                                                         # Nth number in the Fibonacci sequence
        return 1
    else:
        postcondition(tr_fib(n, 2, 1, 1) == orig_fib(n)) # i.e., we're about to return the
                                                         # Nth number in the Fibonacci sequence
        return tr_fib(n, 2, 1, 1)

#
#  PUT YOUR PROOF OF CORRETNESS HERE OR HAND IT IN ON PAPER
#

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all fib() tests"
        
n = input("Which element of the Fibonacci sequence? ")
if isinstance(n, int) and n > 0:
    print fib(n)
else:
    print "oh, come on!"
