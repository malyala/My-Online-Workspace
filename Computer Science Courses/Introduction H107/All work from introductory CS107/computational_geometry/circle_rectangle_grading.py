"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        center_x,center_y,radius,xmin,xmax,ymin,ymax
        
Samples:
# can't have a circle with negative radius
>>> circle_rectangle_overlap_samples(5,8,-6, 12,18, 16,19)
Traceback (most recent call last):
...
PreconditionException

# An obvious overlap:
>>> circle_rectangle_overlap_samples(100,20,8, 80,120, 18,25)
True

# An obvious miss:
>>> circle_rectangle_overlap_samples(100,20,8, 180,220, 18,25)
False

################################################################
#"Corner Cases"-These are to see if it catches the corner of the 
# rectangle within the circle
#upper left corner
>>> circle_rectangle_overlap_samples(100, 150, 40, 100, 400, 150, 350)
True

#upper right corner
>>> circle_rectangle_overlap_samples(400, 150, 40, 100, 400, 150, 350)
True

#lower left corner
>>> circle_rectangle_overlap_samples(100, 350, 40, 100, 400, 150, 350)
True

#lower right corner
>>> circle_rectangle_overlap_samples(400, 350, 40, 100, 400, 150, 350)
True

#"Peg in the square hole" This is to check putting the circle completely within the rectangle
>>> circle_rectangle_overlap_samples(250, 250, 40, 100, 400, 150, 350)
True

##################################################################
#These next few tests are to make sure that range_overlap was not just used
# and if it was, make sure that it is a bi-directional overlap and not just
# checking the range of x or just the range of y, but both

# "Circle completely to the left of the rectangle"
>>> circle_rectangle_overlap_samples(50, 250, 30, 100, 400, 150, 350)
False

# "Circle completely above the rectangle"
>>> circle_rectangle_overlap_samples(250, 100, 30, 100, 400, 150, 350)
False

# "Circle completely to the right of the rectangle"
>>> circle_rectangle_overlap_samples(450, 250, 30, 100, 400, 150, 350)
False

# "Circle completely below the rectangle"
>>> circle_rectangle_overlap_samples(250, 400, 30, 100, 400, 150, 350)
False

#"1-edge intersection": This tests an overlap of a cirlce with just one
# edge of the rectanlge. This is the positive test of above. This would 
# show that bi-directional range overlaps work

# "Circle intersects left edge of rectangle"
>>> circle_rectangle_overlap_samples(100, 250, 50, 100, 400, 150, 350)
True

# "Circle intersects the top edge of the rectangle"
>>> circle_rectangle_overlap_samples(250, 150, 50, 100, 400, 150, 350)
True

# "Circle intersects the right edge of the rectangle"
>>> circle_rectangle_overlap_samples(400, 250, 50, 100, 400, 150, 350)
True

# "Circle intersects the bottom edge of the rectangle"
>>> circle_rectangle_overlap_samples(250, 350, 50, 100, 400, 150, 350)
True

#"1-edge touching": This test is to see if it catches the case where
# the edge of the rectangle and the edge of the circle share one
# one point exactly

# "Circle is touching the top edge"
>>> circle_rectangle_overlap_samples(250, 100, 50, 100, 400, 150, 350)
True

# "Circle is touching the right edge"
>>> circle_rectangle_overlap_samples(450, 250, 50, 100, 400, 150, 350)
True

# "Circle is touching the bottom edge"
>>> circle_rectangle_overlap_samples(250, 400, 50, 100, 400, 150, 350)
True

# "Circle is touching the right edge"
>>> circle_rectangle_overlap_samples(50, 250, 50, 100, 400, 150, 350)
True

##################################################################
#"Square around the circle" These last 4 tests are to catch the more
# subtle case where the square around the circle is used and the square
# around the circle intersects the rectangle, but the circle actually does not
>>> circle_rectangle_overlap_samples(107, 149, 26, 130, 397, 169, 360)
False

>>> circle_rectangle_overlap_samples(405, 169, 21.1896, 133, 388, 187, 359)
False

>>> circle_rectangle_overlap_samples(391, 360, 29.529, 113, 369, 169, 335)
False

>>> circle_rectangle_overlap_samples(131, 368, 33.24, 161, 417, 168, 344)
False
"""

import sys
sys.path.append("/home/courses/python")

from math import *
from logic import *

from circle_rectangle import circle_rectangle_overlap    

# import circle_rectangle


circle_rectangle_overlap_samples = circle_rectangle_overlap

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed the test!"
    else:
        print "Rats!"

if __name__ == "__main__":
    _test()
