"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        center_x,center_y,radius,xmin,xmax,ymin,ymax
        
some examples:

# An obvious overlap:
>>> circle_rectangle_overlap(100,20,8, 80,120, 18,25)
True

# An obvious miss:
>>> circle_rectangle_overlap(100,20,8, 180,220, 18,25)
False



(Note we can't have a circle with negative radius)

##############################################################################


#Circle inside rectangle
>>> circle_rectangle_overlap( 240,234,35.4682957019, 149,335 ,143,314 )
True

#Rectangle inside circle
>>> circle_rectangle_overlap( 222 ,  218 ,  63.1347764707 ,  207 ,  235 ,  205 ,  230 )
True

#8 Points of intersection-  circle inside ish rectangle
>>> circle_rectangle_overlap( 265 ,  250 ,  78.4346862045 ,  203 ,  331 ,  190 ,  310 )
True

#4 points of intersection with circle's left side in rect.
>>> circle_rectangle_overlap( 225 ,  246 ,  62.4339651152 ,  194 ,  214 ,  74 ,  462 )
True

#Top left corner, center of circ inside rect
>>> circle_rectangle_overlap( 174 ,  148 ,  47.2016948848 ,  161 ,  368 ,  136 ,  281 )
True

#Top left corner, center of circ outside rect
>>> circle_rectangle_overlap( 130 ,  154 ,  45.2769256907 ,  147 ,  384 ,  169 ,  342 )
True

#Bottom left corner, center of circ inside rect
>>> circle_rectangle_overlap( 147 ,  295 ,  46.7546789102 ,  135 ,  364 ,  188 ,  310 )
True

#Bottom left corner, center of circ outside rect
>>> circle_rectangle_overlap( 136 ,  316 ,  62.4259561401 ,  145 ,  395 ,  179 ,  306 )
True

#no overlap, shared y vals
>>> circle_rectangle_overlap( 95 ,  224 ,  27.8028775489 ,  203 ,  424 ,  150 ,  313 )
False

#no overlap, no shared vals, circ top left- already included in the examples
circle_rectangle_overlap( 117 ,  134 ,  39.1152144312 ,  327 ,  447 ,  351 ,  437 )
False

#A  circle point on a horiontal line 
>>> circle_rectangle_overlap( 150 ,  87 ,  0.0 ,  100 ,  200 ,  87 ,  87 )
True

# line pokes circle
>>> circle_rectangle_overlap( 200 ,  226 , 15 ,  215 ,  473 ,  226 ,  226 )
True

#Circle point on corner of rectangle
>>> circle_rectangle_overlap( 212 ,  212 ,  0.0 ,  212 ,  337 ,  212 ,  425 )
True

#Rectangle point on circle's "edge"
>>> circle_rectangle_overlap( 178 ,  130 ,  30 ,  178 ,  178 ,  160 ,  160 )
True

#Circle touches side of rectangle
>>> circle_rectangle_overlap( 120 ,  240 ,  70 ,  190 ,  347 ,  136 ,  353 )
True

#Circle very close to bottom right corner
 >>> circle_rectangle_overlap( 337 ,  382 ,  72.470683728 ,  160 ,  288 ,  221 ,  321 )
 False
 
#Circle very close to top of rect.
>>> circle_rectangle_overlap( 238 ,  134 ,  82.7647267862 ,  145 ,  327 ,  221 ,  347 )
False
 
#point on point
>>> circle_rectangle_overlap( 195 ,  179 ,  0.0 ,  195 ,  195 ,  179 ,  179 )
True



##############################################################################

"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *


def circle_rectangle_overlap(center_x,center_y,radius,xmin,xmax,ymin,ymax):
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true if there exists x, y in both shapes...
    MODE='code review'  # set to 'test samples', 'answer key', 'code review', or 'mine'
    
    if MODE=='mine':
#Start of algorithm

        rect_x = abs(xmax - xmin)/2.0 #Define the center of the rectangle- done for readibility:
        rect_y = abs(ymax - ymin)/2.0

        
        
#Part 1: Test if the center of each shape is inside/touching the other
#return true if so

        if center_x >= xmin and center_x <= xmax and center_y >= ymin and center_y <= ymax:
            return True
        elif ((rect_x - center_x)**2 + (rect_y - center_y)**2) <= radius**2:
            return True
            
#Part 2: Check if there are any intersections- if any return true
        for xval in [xmin, xmax]:
            if abs(xval - center_x) <= radius:
                #If the rectangle's lines on x values (the sides) are close enough
                #to the circle's farthest x-value to touch
                #calculate the potential intersection points:
                y_a = center_y + sqrt(radius**2 - (xval-center_x)**2)
                y_b = center_y - sqrt(radius**2 - (xval-center_x)**2)
                
                #If these intersection points are unique and are in the
                #range of the rectangle, return true because an intersection exists
                if y_a >= ymin and y_a <= ymax:
                    return True
                if y_b != y_a and y_b >= ymin and y_b <= ymax:
                    return True
       
#Repeat the same process for the intersections to the 
#top or bottom of the rectangle (sides defined by y = some constant)
        
        for yval in [ymin,ymax]:
            if abs(yval-center_y) <= radius:
                x_a = center_x + (radius**2 - (yval-center_y)**2)**0.5
                x_b = center_x - (radius**2 - (yval-center_y)**2)**0.5
                if x_a >= xmin and x_a <= xmax:
                    return True        
                if x_b != x_a and x_b >= xmin and x_b <= xmax:
                    return True  
    
#At this point, we've established there are no intersections and
#The center of either shape is not inside the other
#Thus- they must not overlap- return false
        return False

#End of algorithm        
        
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
