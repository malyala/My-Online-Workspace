"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        center_x,center_y,radius,xmin,xmax,ymin,ymax
        
some examples:

# Got 3,4,5 | Inside | An obvious overlap:
>>> circle_rectangle_overlap(100,20,8, 80,120, 18,25)
True
 
# Got - | Left Side | An obvious miss:
>>> circle_rectangle_overlap(100,20,8, 180,220, 18,25)
False
 
(Note we can't have a circle with negative radius)

##############################################################################
#
#        REPLACE THIS COMMENT WITH THE REST OF YOUR TEST SUITE,
#        HOPEFULLY DISTINGUISHING GOOD FROM BAD SAMPLE ANSWERS
#
##############################################################################

 All Notable Cases (I think...):
=================================
Given that if a circle center coord is 'within' the rect it is centered along that axis edge
  and that if not otherwise stated, the case should return True
=================================

- 4 | both circle center coordinates within rect
    - radius <= min_side_length/2 or radius >= max_side_length/2 (4)
      (can be 3 if min_side_length/2 == max_side_length/2 (i.e. a square))

- 36 | one circle center coordinate within rect (i.e. covering, touching, or not contacting an edge)
    - location (4), radius </=/> side_length/2 (3), the other coordinate </=/> a radius-length away frm its edge (3)
      (if other coordinate > radius-length, return False)
- 12 | one circle center coordinate within rect, one lying on its edge (i.e. centered on a edge)
    - location (4), radius </=/> side_length/2 (3)

- 16 | no circle center coordinates within rect (i.e. covering, touching, aligned w/ and not contacting, or totally not contacting a corner)
    - location (4), radius </= sqrt(distance_from_corner^2 / 2) or radius =/> distance_from_corner (4)
      (if radius < distance_from_corner, return False)
- 24 | only one circle center coordinate lying on its edge (i.e. lying past but even w/ one edge - covering, touching, or not contacting that corner)
    - location (8), radius </=/> distance_from_corner (3)
      (if radius < distance_from_corner, return False)
- 16 | both circle center coordinates lying on their edges (i.e. centered on a corner)
    - location (4), radius <= min_side_length/2 or radius >= max_side_length/2 (4)
      (can be 3 if min_side_length/2 == max_side_length/2 (i.e. a square))

- 108 cases total (too much!)

Weeding out: limited to one location each
- 27 cases total (still too much...?)

>>> circle_rectangle_overlap(  200, 200,  49,  100,300,150,250)
True
>>> circle_rectangle_overlap(  200, 200,  50,  100,300,150,250)
True
>>> circle_rectangle_overlap(  200, 200, 100,  100,300,150,250)
True
>>> circle_rectangle_overlap(  200, 200, 101,  100,300,150,250)
True

>>> circle_rectangle_overlap(   52, 200,  49,  100,300,150,250)
True
>>> circle_rectangle_overlap(   51, 200,  49,  100,300,150,250)
True
>>> circle_rectangle_overlap(   50, 200,  49,  100,300,150,250)
False
>>> circle_rectangle_overlap(   51, 200,  50,  100,300,150,250)
True
>>> circle_rectangle_overlap(   50, 200,  50,  100,300,150,250)
True
>>> circle_rectangle_overlap(   49, 200,  50,  100,300,150,250)
False
>>> circle_rectangle_overlap(   50, 200,  51,  100,300,150,250)
True
>>> circle_rectangle_overlap(   49, 200,  51,  100,300,150,250)
True
>>> circle_rectangle_overlap(   48, 200,  51,  100,300,150,250)
False

>>> circle_rectangle_overlap(  100, 200,  49,  100,300,150,250)
True
>>> circle_rectangle_overlap(  100, 200,  50,  100,300,150,250)
True
>>> circle_rectangle_overlap(  100, 200,  51,  100,300,150,250)
True

>>> circle_rectangle_overlap(   50, 100,  49,  100,300,150,250)
False
>>> circle_rectangle_overlap(   50, 100,  50,  100,300,150,250)
False
>>> circle_rectangle_overlap(   50, 100,  70.710678119,  100,300,150,250)
True
>>> circle_rectangle_overlap(   50, 100,  71.710678119,  100,300,150,250)
True

>>> circle_rectangle_overlap(   50, 150,  49,  100,300,150,250)
False
>>> circle_rectangle_overlap(   50, 150,  50,  100,300,150,250)
True
>>> circle_rectangle_overlap(   50, 150,  51,  100,300,150,250)
True

>>> circle_rectangle_overlap(  100, 150,  49,  100,300,150,250)
True
>>> circle_rectangle_overlap(  100, 150,  50,  100,300,150,250)
True
>>> circle_rectangle_overlap(  100, 150, 100,  100,300,150,250)
True
>>> circle_rectangle_overlap(  100, 150, 101,  100,300,150,250)
True

"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *



# ======================
#  Algorithm of Choice:
# ======================

# Returns 0 if center_z is within range, else returns the minimum of the center's squared distances to each end-point
def minDistanceSqrd(center_z,zmin,zmax):
    return 0 if zmin <= center_z <= zmax else min((center_z-zmin)**2,(center_z-zmax)**2)

# A much better algorithm for the problem
def my_circle_rectangle_overlap_simpler(center_x,center_y,radius,xmin,xmax,ymin,ymax):
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes s.t.
    # - the point (x,y) lies within or on a circle centered at (center_x,center_y) and of the given radius
    # - the point (x,y) lies within or on a rectangle spanning over the ranges [xmin,xmax] in the x-direction, and [ymin,ymax] in the y-direction
    return minDistanceSqrd(center_x,xmin,xmax) + minDistanceSqrd(center_y,ymin,ymax) <= radius**2




# A working algorithm for the problem
def my_circle_rectangle_overlap_simple(center_x,center_y,radius,xmin,xmax,ymin,ymax):
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes s.t.
    # - the point (x,y) lies within or on a circle centered at (center_x,center_y) and of the given radius
    # - the point (x,y) lies within or on a rectangle spanning over the ranges [xmin,xmax] in the x-direction, and [ymin,ymax] in the y-direction
    if xmin <= center_x <= xmax and ymin <= center_y <= ymax: return True
    elif xmin <= center_x <= xmax: return min(abs(center_y-ymin),abs(center_y-ymax)) <= radius
    elif ymin <= center_y <= ymax: return min(abs(center_x-xmin),abs(center_x-xmax)) <= radius
    else: return min(abs(center_x-xmin),abs(center_x-xmax))**2 + min(abs(center_y-ymin),abs(center_y-ymax))**2 <= radius*radius



# A non-working!!! but interesting approach to the problem
def my_circle_rectangle_overlap_proj(center_x,center_y,radius,xmin,xmax,ymin,ymax):
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # NOTE: postcondition not always met! (see test cases)
    # postcondition: return true iff there exists x, y in both shapes s.t.
    # - the point (x,y) lies within or on a circle centered at (center_x,center_y) and of the given radius
    # - the point (x,y) lies within or on a rectangle spanning over the ranges [xmin,xmax] in the x-direction, and [ymin,ymax] in the y-direction
    
    axis = [(xmin+xmax)/2.0 - center_x, (ymin+ymax)/2.0 - center_y]
    
    cntr = center_x*axis[0] + center_y*axis[1]
    radp = cntr + radius*sqrt(axis[0]*axis[0] + axis[1]*axis[1])
    
    pt_lh = xmin*axis[0] + ymax*axis[1] #dp(axis,[xmin,ymax])
    pt_hl = xmax*axis[0] + ymin*axis[1] #dp(axis,[xmax,ymin])
    pt_ll = xmin*axis[0] + ymin*axis[1] #dp(axis,[xmin,ymin])
    pt_hh = xmax*axis[0] + ymax*axis[1] #dp(axis,[xmax,ymax])

     # 2 Range Checks: [cntr,radp] in [pt_lh,pt_hl] or in [pt_ll,pt_lh]
    return (cntr <= max(pt_lh,pt_hl) and radp >= min(pt_lh,pt_hl)) or (cntr <= max(pt_ll,pt_hh) and radp >= min(pt_ll,pt_hh))



def circle_rectangle_overlap(center_x,center_y,radius,xmin,xmax,ymin,ymax):
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes...
    MODE='mine'  # set to 'test samples', 'answer key', 'code review', or 'mine'
    
    if MODE=='mine':
        return my_circle_rectangle_overlap_simpler(center_x,center_y,radius,xmin,xmax,ymin,ymax) 
    elif MODE=='code review':
        import circle_rectangle_to_review as review
        return review.circle_rectangle_overlap(center_x,center_y,radius,xmin,xmax,ymin,ymax)
    elif MODE=='answer key':
        print 'DAVE NEEDS TO FINISH THIS!'
    elif MODE=='test samples':
        from sample_answers.cs105.intersect.circle_rectangle_sample import circle_rectangle_overlap_samples
        answer = circle_rectangle_overlap_samples(center_x,center_y,radius,xmin,xmax,ymin,ymax)
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
