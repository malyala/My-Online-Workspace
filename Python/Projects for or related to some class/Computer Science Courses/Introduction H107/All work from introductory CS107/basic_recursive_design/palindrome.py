"""
##############################################################################
#        LAB 2 QUESTION 2 PART A --- REPLACE THIS WITH YOUR TEST SUITE


#obvious palindrome 1
>>> is_palindrome('racecar')
True

#obvious palindrome 2 -courtesy of textbook
>>> is_palindrome('A man, a plan, a canal: Panama')
True

#obvious palindrome 3 -courtesy of textbook
>>> is_palindrome('Lived on decaf, faced no devil')
True

#Repeated letter with varying upper lowercases
>>> is_palindrome('aaaaaAaAAaaaa')
True

#Obvious not pal 1
>>> is_palindrome('abc def gh')
False

#Obvious not pal 2
>>> is_palindrome('I like apples.')
False

#close pal 1
>>> is_palindrome('racecars')
False

#Close pal 2
>>> is_palindrome('aababbaa')
False

#Close pal 3- notice the 'g' after canal
>>> is_palindrome('A man, a plan, a canal g: Panama')
False

#first string of length one:
>>> is_palindrome('r')
True

#second string of length one:
>>> is_palindrome('a')
True

#String of length 2 that is a pal
>>> is_palindrome('rr')
True

#String of length 2 that is not a pal
>>> is_palindrome('ab')
False

#A palindrome with a lot of punctuation/spaces
>>> is_palindrome('r@  a/ ?  ?c..ec#$a    r')
True

#A palindrome with upper and lowercase mix letters
>>> is_palindrome('RacECaR')
True


##############################################################################


##############################################################################
#
#        Lab 3, Question 1A --- REPLACE THIS COMMENT WITH A "DESIGN COMMENT"

1. We can check if the first and last letter are the same, if so, we can
remove those and end up asking if the remaining string is a palindrome. 


2. The solution to the problem is the logical combination
of whether the first and last letters are equal AND if the rest of 
the string is a palindrome:
letters[0] == letters[-1] and is_palindrome(letters[1:-1])

3. If the string is of length 0 we can say the string is a palindrome and 
return true

4. base case algorithm:
if letters == "":
    return True
5.
if we have a string of length n and are taking away the first and last
letter and n is even we eventuially get to two letters and then
zero. If n is odd, we eventuially get to one letter and since 
a string of one letter spliced [1:-1] is '', we have again reached the base case



##############################################################################

"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)


def is_palindrome(letters):
    # LAB 2 QUESTION 2 PART B --- add a precondition for the function
    
    
    #Precondition:
    #A palindrome is defined here as any string such that the letters
    #in the string backward are equal - a string like 
    #>>> is_palindrome("race***car")
    #>>> True
    #Thus, any valid string input is my pre condition
    precondition(type(letters)==str)
 
    
    


    
#  Lab 3, Question 1b --- REPLACE THE REST OF THIS FUNCTION WITH YOUR ANSWER
    
    
    letters = lower_case_letters(letters) #normally this line would be in a wrapper function  
    if letters == '':
            
        return True
    else:
       
        ret = letters[0] == letters[-1] and is_palindrome(letters[1:-1])    
        postcondition(ret ==(letters == letters[::-1]))
        return ret
    # LAB 2 QUESTION 2 PART C --- add a postcondition for the function






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

