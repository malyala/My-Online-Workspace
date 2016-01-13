"""
##############################################################################
#
#        LAB 2 QUESTION 1 PART A --- REPLACE THIS WITH YOUR TEST-SUITE
#
##############################################################################

##############################################################################
#
#        Lab 3, Question 2A --- REPLACE THIS COMMENT WITH A "DESIGN COMMENT"
#
##############################################################################

"""

from math import *
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

def fib(n):
    # LAB 2 QUESTION 1 PART B --- provide precondition

    #
    # LAB 3, Question 2B --- REPLACE LINE BELOW AND THIS COMMENT WITH YOUR ALGORITHM
    #
    
    answer = 8   # This is wrong for all questions except fib(6)
    
    # LAB 2 QUESTION 1 PART C --- provide postcondition
    
    return answer

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
