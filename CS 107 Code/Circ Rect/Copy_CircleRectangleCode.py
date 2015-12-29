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

#No overlap but shared x values
>>> circle_rectangle_overlap( 191 ,  341 ,  28.6530975638 ,  81 ,  364 ,  131 ,  288 )
False

#No overlap but shared y values
>>> circle_rectangle_overlap( 288 ,  197 ,  29.0688837075 ,  150 ,  235 ,  141 ,  303 )
False

#No Overlap and no shared x or y values
>>> circle_rectangle_overlap( 50 ,  92 ,  36.3593179254 ,  195 ,  394 ,  197 ,  254 )
False


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
    MODE= 'mine'  # set to 'test samples', 'answer key', 'code review', or 'mine'
    
    if MODE=='mine':
        #Define the center of the rectangle:
        rect_x = abs(xmax - xmin)/2.0
        rect_y = abs(ymax - ymin)/2.0
        # Define a list that stores the intersections
        isects = []
    
#Part 1: Test if the center of each shape is inside the other
#return true if so   
        if center_x >= xmin and center_x <= xmax and center_y >= ymin and center_y <= ymax:
            return True
        elif ((rect_x - center_x)**2 + (rect_y - center_y)**2) <= radius**2:
            return True
            
#Part 2: Count the number of intersections
        
#Start with the sides of the rectangle defined by equations
# x = some constant
        for xval in [xmin, xmax]:
            if abs(xval - center_x) <= radius:
                #If the rectangle's lines on x values (the sides) are close enough
                #to the circle's farthest x-value to touch
                #calculate the potential intersection points:
                y_a = center_y + (radius**2 - (xval-center_x)**2)**0.5
                y_b = center_y - (radius**2 - (xval-center_x)**2)**0.5
                
                #If these intersection points are unique and are in the
                #range of the rectangle, add them to the list of intersections
                if y_a >= ymin and y_a <= ymax:
                    isects.append((xval, y_a))
                if y_b != y_a and y_b >= ymin and y_b <= ymax:
                    isects.append((xval, y_b))
    
#Repeat the same process for the intersections to the 
#top or bottom of the rectangle (sides defined by y = some constant)
#I did it this way for readability        
        for yval in [ymin,ymax]:
            if abs(yval-center_y) <= radius:
                x_a = center_x + (radius**2 - (yval-center_y)**2)**0.5
                x_b = center_x - (radius**2 - (yval-center_y)**2)**0.5
                if x_a >= xmin and x_a <= xmax:
                    isects.append((x_a, yval))        
                if x_b != x_a and x_b >= xmin and x_b <= xmax:
                    isects.append((x_b, yval))    
    
#If there is more than one intersection, return True
#Otherwise False
#Important Note: this means for exactly one intersection,
#we consider this to not be overlapping 
        if len(isects) > 1:
            return True
        else:
            return False
        
        
        
        # REPLACE THIS WITH YOUR ALGORITHM
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

## I am stopping tesing for a moment!!:
##

if __name__ == "__main__": _test()





