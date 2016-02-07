"""
    Test Suite:
==================
#GCD tests:

>>> GCD(3, 6)
3

>>> GCD(12, 18)
6

>>> GCD(-12, 18)
6

>>> GCD(9,12)
3

>>> GCD(4,3)
1

>>> GCD(60,103)
1

>>> GCD(1,1)
1

>>> GCD(-1,1)
1

>>> GCD(1,2)
1

>>> GCD(2,1)
1

>>> GCD(7,21)
7

>>> GCD(13,13)
13

>>> GCD(-12,12)
12

>>> GCD(10,245)
5

>>> GCD(10,-245)
5


>>> GCD(10,0)
10

>>> GCD(-10,0)
10


>>> GCD(0,0)
0

>>> GCD(0,-5)
5

>>> GCD(0,1)
1


#End of GDC tests

=================
=================

#in_reduced_form tests:

>>> in_reduced_form([3, 6])
[1, 2]

>>> in_reduced_form([-3, 6])
[-1, 2]

>>> in_reduced_form([1, 1])
[1, 1]

>>> in_reduced_form([1, -1])
[1, -1]

>>> in_reduced_form([1, 2])
[1, 2]

>>> in_reduced_form([0, 2])
[0, 1]

>>> in_reduced_form([0, -2])
[0, -1]

>>> in_reduced_form([324325, 1])
[324325, 1]

>>> in_reduced_form([324325, -1])
[324325, -1]

>>> in_reduced_form([324325, 2])
[324325, 2]

>>> in_reduced_form([-324325, -2])
[-324325, -2]

>>> in_reduced_form([24, 6])
[4, 1]

>>> in_reduced_form([-24, 6])
[-4, 1]

>>> in_reduced_form([64, 12])
[16, 3]

>>> in_reduced_form([36, 54])
[2, 3]


#no change test 1
>>> test0 = [3, 6]
>>> in_reduced_form(test0)
[1, 2]
>>> test0  # this should NOT have been changed by a function
[3, 6]


#no change test 2
>>> test_a = [64, 12] 
>>> in_reduced_form(test_a)
[16, 3]
>>> test_a
[64, 12]

#no change test 3
>>> test_b = [36, 54] 
>>> in_reduced_form(test_b)
[2, 3]
>>> test_b
[36, 54]

#no change test 4
>>> test_zero = [0, 54] 
>>> in_reduced_form(test_zero)
[0, 1]
>>> test_zero
[0, 54]

#no change test 5
>>> test_zero1 = [0, -54] 
>>> in_reduced_form(test_zero1)
[0, -1]
>>> test_zero1
[0, -54]



#End of in_reduced_form tests
================================
================================

#A few reduce tests:


>>> test1 = [3,6]
>>> reduce(test1)
>>> test1
[1, 2]

>>> test2 = [1,2]
>>> reduce(test2)
>>> test2
[1, 2]

>>> test3_a = [64, 12]
>>> reduce(test3_a)
>>> test3_a
[16, 3]

>>> test3_b = [64, -12]
>>> reduce(test3_b)
>>> test3_b
[16, -3]

>>> test_reduce_zero = [0, -12]
>>> reduce(test_reduce_zero)
>>> test_reduce_zero
[0, -1]


#clever test of both reduce and in_reduced_form 
>>> test3 = [3,6]
>>> test4 = test3
>>> in_reduced_form(test3)
[1, 2]
>>> test3
[3, 6]
>>> reduce(test3)
>>> test3
[1, 2]
>>> test4
[1, 2]

==============================
End of reduce tests

==============================
    End of test suite


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



def cryp_gcd(larger,smaller):
    #assumes both are positive ints
    ret = []
    remainder = larger %smaller
    q = larger/smaller
    ret.append([larger, (q,smaller), remainder])
    if remainder ==0:
        return ret
    else:
        return ret + cryp_gcd(smaller, remainder)
    
    

def GCD(x,y):
    
    precondition(is_integer(x) and is_integer(y)) #either can be zero, this is a valid question!
    x = abs(x)
    y = abs(y) #saves us some issues later on.. divisors are positive
    if x==0 and y==0:
        ret = 0
        postcondition(x==0 and y==0 and ret==0) # look it up, GCD(0,0) =0 since 0 is the largest natural divisor
        return ret
    elif x ==0 or y ==0:
        ret = max(x,y)
        postcondition((x % ret) == 0 and (y % ret) == 0)
        return ret
    smaller_z = min(x,y)
    larger_z = max(x,y)
    remainder = larger_z % smaller_z
    if remainder == 0:
        postcondition((x % smaller_z) == 0 and (y % smaller_z) == 0)
        return smaller_z 
    else:
        ret_gcd = GCD(smaller_z, remainder)
        postcondition(x%ret_gcd ==0 and y%ret_gcd == 0)
        return ret_gcd

def in_reduced_form(fraction_in_a_list):
    precondition(len(fraction_in_a_list)==2 and all(map(is_integer, fraction_in_a_list)) and fraction_in_a_list[1] != 0)
    num = fraction_in_a_list[0] #written out for clarity
    den = fraction_in_a_list[1]

    #these next two lines have no impact if the num == 0
    gcd = GCD(num, den)
    ret = [num/gcd, den/gcd]
    postcondition(GCD(ret[0], ret[1]) == 1)#a reduced fraction by definition has a gcd of 1 btwn num and denom
    return ret
    
def reduce(fraction_in_a_list):
    precondition(len(fraction_in_a_list)==2 and all(map(is_integer, fraction_in_a_list)) and 
                 fraction_in_a_list[1] != 0)

#If the num was zero then the denom will be reduced to 1 or -1 
#because gcd(0, a) == abs(a)
    gcd = GCD(fraction_in_a_list[0], fraction_in_a_list[1])        
    fraction_in_a_list[0] = fraction_in_a_list[0]/gcd
    fraction_in_a_list[1] = fraction_in_a_list[1]/gcd   #lists are mutable
#this postcondition is a way to state the defnintion of reduced form (that the only int k such that both
#the num and denom are divided without remainder is 1)
    postcondition( GCD(fraction_in_a_list[0], fraction_in_a_list[1]) == 1 ) 
  
    
  

# User interface for reduce, which should be defined above (as should GCD)
# Do NOT change this, but you can write your own if you like
def reduce_ui():
    n = input("Enter numerator ")
    d = input("Enter non-zero denominator (or 0 to stop) ")
    while (d != 0):
        result = in_reduced_form([n, d])
        print """According to "in_reduced_form", that's""", result[0], "/", result[1], "in reduced terms."

        fraction_in_list = [n, d]
        reduce(fraction_in_list)
        print """According to "reduce", that's""", fraction_in_list[0], "/", fraction_in_list[1], "in reduced terms."

        n = input("Enter another numerator ")
        d = input("Enter another non-zero denominator (or 0 to stop) ")

    print "Thanks for playing the fractions game!"

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": 
    _test()
    reduce_ui()

