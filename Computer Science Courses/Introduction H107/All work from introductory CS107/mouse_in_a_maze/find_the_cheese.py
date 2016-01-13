"""

The main algorithm for the mouse in the maze should be written in this file

"""
# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')
from logic import *
from graphics import move_forward, turn_left, turn_right, look_ahead, look_left, look_right, eat_cheese, maze_debug_on, maze_debug_off


def one_step_to_cheese():
    if look_ahead() == 'c':
        eat_cheese()
    elif look_left() != 'w':
            turn_left()
    elif look_right() != 'w':
        turn_right()
    elif look_ahead() != 'w':
            move_forward()
    elif look_ahead() == 'w':
        turn_left()
        


def move_to_cheese():
    while look_ahead() != 'c':
        if look_left() != 'w':
            turn_left()
            move_forward()
            #move_to_cheese()
        elif look_ahead() != 'w':
            move_forward()
            #move_to_cheese()
        elif look_ahead() == 'w':
            turn_right()
            #move_to_cheese()
    eat_cheese()
            
def move_to_cheese2():
    while look_ahead() != 'c':
        if look_left() != 'w':
            turn_left()
            move_forward()
        elif look_right() != 'w':
            turn_right()
            move_forward()
        elif look_ahead() != 'w':
            move_forward()
        elif look_ahead() == 'w':
            turn_left()
    eat_cheese()
            
    

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
