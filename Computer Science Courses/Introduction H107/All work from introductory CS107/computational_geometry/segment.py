"""
Test suite goes here, as usual. You could improve this comment, while you're at it.
"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from logic import *
from math import *    
            
def segment_overlap(x1, y1, x2, y2, x3, y3, x4, y4):

    ##########################################################
    # REPLACE THIS COMMENT AND THE THREE LINES BELOW WITH YOUR SOLUTION

    from sample_answers.cs105.intersect.segment_sample import segment_overlap_samples
    answer = segment_overlap_samples(x1, y1, x2, y2, x3, y3, x4, y4)
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
