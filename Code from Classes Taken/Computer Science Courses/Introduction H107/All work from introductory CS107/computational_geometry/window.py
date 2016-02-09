"""
Find out whether two rectangular computer "windows" overlap,
In other words, find out whether there is any point on the screen that
is used by both.

Examples (courtesy of Andrew Wonnacott):

>>> window_overlap(50,300,50,350, 100,500,100,500)
True

>>> window_overlap(100,399.99,100,401, 400,600,100,400)
False

>>> window_overlap(100,400.001,100,401, 400.0001,600,100,400)
True

>>> window_overlap( 62 ,  179 ,  96 ,  192 ,  226 ,  346 ,  98 ,  208 )
False

>>> window_overlap( 31 ,  173 ,  45 ,  227 ,  142 ,  292 ,  39 ,  240 )
True

>>> window_overlap( 228 ,  390 ,  102 ,  222 ,  32 ,  150 ,  77 ,  215 )
False

>>> window_overlap( 130 ,  221 ,  90 ,  181 ,  121 ,  278 ,  199 ,  364 )
False

>>> window_overlap( 75 ,  424 ,  216 ,  488 ,  225 ,  240 ,  168 ,  179 )
False

>>> window_overlap( 182 ,  389 ,  165 ,  277 ,  105 ,  197 ,  180 ,  232 )
True

>>> window_overlap( 80 ,  244 ,  88 ,  198 ,  127 ,  159 ,  169 ,  237 )
True

>>> window_overlap( 126 ,  262 ,  268 ,  409 ,  156 ,  186 ,  213 ,  302 )
True

Here, #2 is touching but to the right of, #1 --- this should count as overlap!
>>> window_overlap( 100, 600, 10, 500,   600, 800, 200, 300)
True

Note that this sort of thing, with minx2 > maxx2, is not allowed!
### >>> window_overlap( 100, 600, 10, 500,   600, 500, 200, 300)
"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from logic import *
from range import *

# The following comes from Dave Wonnacott's Wednesday lecture.
# See also window_overlap_from_course_notes below for another approach
    
def window_overlap(minx1,maxx1,miny1,maxy1,minx2,maxx2,miny2,maxy2):
    if minx2 > maxx1:    # 2 to the right of 1
        return False
    elif maxy1 < miny2:  # 2 above 1
        return False
    elif maxx2 < minx1:
        return False
    elif maxy2 < miny1:
        return False
    else:
        return True


def window_overlap_from_course_notes(minx1,maxx1,miny1,maxy1,minx2,maxx2,miny2,maxy2):
    precondition(minx1 <= maxx1 and minx2 <= maxx2 and miny1 <= maxy1 and miny2 <= maxy2)
    """postcondition: return true iff there exists x,y in both windows, i.e. minx1 <= x <= maxx1 and miny1 <= y <= maxy1 etc """
    return range_overlap(minx1, maxx1, minx2, maxx2) and range_overlap(miny1, maxy1, miny2, maxy2)


# copied from  http://docs.python.org/lib/module-doctest.html
# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
