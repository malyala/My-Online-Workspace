"""
    
This should find a real-number solution to the equation a*x*x + b*x + c = 0
   if one exists.
   
Test suite:

When a==1, b==0, and c==-4, we have 1*x*x + 0*x + -4, or x*x = 4, i.e. x=2 (or -2)
>>> equation_solver(1.0, 0.0, -4.0)    # or -2.0 is also a good answer
2.0

When a==1, b==0, and c==-2, we have 1*x*x + 0*x + -2, or x*x = 2, i.e. x=sqrt(2) (or -sqrt(2))
>>> equation_solver(1.0, 0.0, -2.0)      # doctest: +ELLIPSIS
1.4142135......

Note that an alternate way to describe that test would be to use about_equal,
which is perhaps appealing as the answer is closer to 1.4142136 than 1.4142135:
>>> about_equal(equation_solver(1.0, 0.0, -2.0), 1.4142136)
True

or, even better, we could say
>>> about_equal(equation_solver(1.0, 0.0, -2.0), sqrt(2.0))
True

Since equation_solver (and perhaps even sqrt) could return -1.41..., we could use
>>> about_equal(abs(equation_solver(1.0, 0.0, -2.0)), abs(sqrt(2.0)))
True

One more option would be to say something like this...
>>> equation_solver(1.0, 0.0, -2.0) * equation_solver(1.0, 0.0, -2.0)      # doctest: +ELLIPSIS
2.00000...




Note that we cannot solve a problem like x*x + 1 == 0, i.e.
THIS IS ILLEGAL >>> equation_solver(1.0, 0.0, 1.0)
(note that the above is not detected by DocTest; it's just a comment).


Some people like to take advantage of the fact that our precondition system
currently creates a "PreconditionException" by writing something like this:
>>> equation_solver(1.0, 0.0, 1.0)
Traceback (most recent call last):
...
PreconditionException


However, other people note that this last test would be broken by changes to the
logic.py system, and prefer to use only the comment-only approach shown above it.




##############################################################################
#
#        Lab 2, Question 2, Part a: REPLACE THIS COMMENT WITH YOUR TEST SUITE
#
##############################################################################

"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *


# Testing two "real numbers" for equality can be tricky
#   so we'll use the "about_equal" function below to
#   see if two numbers are close enough for the purposes of this lab.
def about_equal(x, y):
    difference=abs(x-y)
    size = abs(x)+abs(y)
    allowed_difference = size/1000.0 + 0.00001
    return difference <= allowed_difference

def equation_solver(a, b, c):
    precondition(True)  #Part b --- edit this

    ###################################################################
    # Part d
    #
    #
    # REPLACE THE REST OF THIS FUNCTION WITH YOUR ANSWER
    #
    
    
    """ Call all of the instructor sample answers, see what answers we get ... """
    from sample_answers.cs105.specifications.equation_sample import equation_solver_samples
    answer = equation_solver_samples(a, b, c)
    
    #
    #
    ####################################################################
    
    postcondition(True) #Part c --- edit this
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
        
########################################################################################
# Lab 4 Part 1
#
#    REPLACE THIS WITH YOUR PROOF OF THE EQUATION_SOVLER
#                    _OR_
#    SAY THAT YOU DID IT ON PAPER AND HAND IT IN THE DROPBOX IN H110
########################################################################################
        
    
