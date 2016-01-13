"""
##############################################################################
#
#        LAB 2 QUESTION 3 PART A --- REPLACE THIS WITH YOUR TEST SUITE
#
##############################################################################


##############################################################################
#
#        Lab 3, Question 2A --- REPLACE THIS COMMENT WITH A "DESIGN COMMENT"
#
##############################################################################

"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from logic import *

def is_palindrome(letters):
    # LAB 2 QUESTION 4 PART B --- add a precondition for the function
    

#  Lab 3, Question 2b --- REPLACE THE REST OF THIS FUNCTION WITH YOUR ANSWER


    # LAB 2 QUESTION 4 PART C --- add a postcondition for the function
    return False   # Well, sometimes it's right...



# User interface for the palindrome function
def palindrome_ui():
    if __name__ == "__main__":
        print "Type 1 to run your test-suite, press 2 to type in your own tests:"
        answer = raw_input()
        if answer in ['1']:  
            _test()
        else:
            print "Please input a possible palindrome: "
            trial_text = raw_input()
            letters_only = lower_case_letters(trial_text)
            if is_palindrome(letters_only):
                print "The text '"+letters_only+"' is a palindrome"
            else:
                print "The text '"+letters_only+"' is not a palindrome."

"""
    make something all lower case letters, e.g.

>>> lower_case_letters('kayak')
'kayak'
>>> lower_case_letters('A man, a plan, a canal: Panama!')
'amanaplanacanalpanama'
"""

def lower_case_letters(text):
    if text == '':
        return ''
    else:
        first = text[0]
        rest  = text[1:len(text)]
        if first in 'abcdefghijklmnopqrstuvwxyz':  # already lower case
            return first + lower_case_letters(rest)
        elif first in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # upper-case
            # lower(first) turns, for example, "D" into "d"
            from string import lower
            return lower(first) + lower_case_letters(rest)
        else:   # otherwise skip first element, as it's not a letter
            return lower_case_letters(rest)

# mostly copied from  http://docs.python.org/lib/module-doctest.html

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

# tests may or may not be chosen by the user interface...
if __name__ == "__main__": palindrome_ui()

