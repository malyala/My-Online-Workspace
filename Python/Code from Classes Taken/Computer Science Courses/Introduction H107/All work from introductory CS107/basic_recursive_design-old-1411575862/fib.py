"""
##############################################################################
#
#        LAB 2 QUESTION 3 PART A --- REPLACE THIS WITH YOUR TEST-SUITE
#
##############################################################################

##############################################################################
#
#        Lab 3, Question 1A --- REPLACE THIS COMMENT WITH A "DESIGN COMMENT"
#
##############################################################################

"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *

def fib(n):
    # LAB 2 QUESTION 3 PART B --- provide precondition

    #
    # LAB 3, Question 1B --- REPLACE LINE BELOW AND THIS COMMENT WITH YOUR ALGORITHM
    #
    
    answer = 8   # This is wrong for all questions except fib(6)
    
    # LAB 2 QUESTION 3 PART C --- provide postcondition
    
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

#######################################################################################
#
# LAB 4 PART 2: Proof of fib()
#
#   REPLACE WITH PROOF _OR_
#     (INDICATE "submitted on paper" _AND_ PLACE PROOF ON PAPER IN THE DROP BOX IN H110)
#        _OR_
#            Indicate that you wrote a proof for the other problem
