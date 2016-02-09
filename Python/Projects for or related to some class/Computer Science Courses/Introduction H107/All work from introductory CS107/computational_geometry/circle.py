"""
Here are some examples of the circle-overlap problem,
in which we give the "x", "y", and radius for one circle and then the other,
and need to know if there are any points that line in/on both circles.
(Note that we don't allow a circle with negative radius.)


# An obvious overlap (Sample answer #3 got this wrong):
>>> circle_overlap(100,100,30, 125,100,30)
True

# An obvious non-overlap (Sample answer #1 gets this one wrong):
>>> circle_overlap(100,100,30, 225,100,30)
False

# An example copied from the "Console" window during a run of overlap-test-graphics
>>> circle_overlap( 160 ,  152 ,  82.8070045346 ,  198 ,  167 ,  93.813645063 )
True


##############################################################################
#
#        REPLACE THIS COMMENT WITH MORE EXAMPLES TO CREATE A FULL TEST-SUITE,
#        PREFERABLY IN TESTS THAT IDENTIFY THE GOOD VS. BAD SAMPLE ANSWERS
#
##############################################################################
"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *
    
def circle_overlap(x1,y1,r1,x2,y2,r2):
    precondition(r1 >= 0 and r2 >= 0)
    # postcondition: return true if there exists x,y in both circular regions, including being on the edge

    MODE='test samples'  # set to 'test samples' or 'mine'
    
    if MODE=='mine':
        return True  # REPLACE THIS WITH YOUR ALGORITHM
    elif MODE=='test samples':
        from sample_answers.cs105.intersect.circle_samples import circle_overlap_samples
        answer = circle_overlap_samples(x1,y1,r1,x2,y2,r2)
        return answer
    else:
        print 'ERROR: You need to set MODE correctly in circle_rectangle_overlap in circle_rectangle.py'


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
