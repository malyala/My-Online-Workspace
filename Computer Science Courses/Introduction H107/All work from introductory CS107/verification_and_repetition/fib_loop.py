"""

>>> fib(5)
5

>>> fib(1)
1

>>> fib(2)
1

>>> fib(10)
55

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

# Hopefully the following will stop any infinite loops without killing anything correct
import resource
resource.setrlimit(resource.RLIMIT_CPU, [3, 5])


# original fibonacci function for use in assertions, postconditions, invariants, etc.
def orig_fib(n):
    precondition(isinstance(n, int) and n>=1)
    # postcondition: gives the Nth number of the Fibonacci sequence
    if n == 1 or n == 2:
        return 1
    else:
        return orig_fib(n-1) + orig_fib(n-2)

def fib(n):
    precondition(isinstance(n, int) and n >= 1)
    if (n == 1):
        postcondition(1 == orig_fib(n)) # i.e., we're about to return the 1st number in the Fibonacci sequence                                                         # Nth number in the Fibonacci sequence
        return 1
    
    term       = 2
    one_before = 1
    current    = 1
    
    while (term < n):
        term = term + 1
        tmp = one_before
        one_before = current
        current = current + tmp

    postcondition(current == orig_fib(n))  # i.e., current is the Nth value of Fib. sequence
    return current

#
#  PUT YOUR PROOF OF CORRETNESS HERE OR HAND IT IN ON PAPER
#
#=================Start of Proof =============================
"""
Collaborator: Ryan herlihy

This proof has two parts. In the first part, we show the proof for the loop in the function.
In the second part, we show the function as a whole is correct given the loop is correct.

Part I: Loop Proof

The Function: 
                def strange_fib_loop(n):
                precondition(is_integer(n) and n>0)
                
                if n <= 2:
                    return 1
                if n == 3:
                    return 2
                
                i = 4
                fib_i = 3
                fib_i_minus_1 = 2
                fib_i_minus_2 = 1
                fib_i_minus_3 = 1
                
                # put your loop_precondition here:
                
                while (i <= n):
                    # Put your loop_invariant, and your loop_progress expression, here:
                
                
                    fib_i = 2 * fib_i_minus_1 - fib_i_minus_3
                    fib_i_minus_3 = fib_i_minus_2
                    fib_i_minus_2 = fib_i_minus_1
                    fib_i_minus_1 = fib_i
                    i = i + 1
                
                # put your loop_postcondition here:
                
                
                # and, finally, the function’s postcondition:
                postcondition(fib_i == fib(n))
                return fib_i

We add the following to this function in the specified locations:
    loop_precondition(i==4 and fib_i == 3 and fib_i_minus_1 == 2 and fib_i_minus_2 == 1 and fib_i_minus_3 == 1 and n >= 4)
    
    loop_invariant( (i==4 and fib_i == 3 and fib_i_minus_1 == 2 and fib_i_minus_2 == 1 and fib_i_minus_3 == 1 and n >= 4) or 
    (fib_i == fib_i_minus_1 and fib+i_minus_1 == fib(i-1) and fib_i_minus_2 == fib(i-2) and fib_i_minus_3 == fib(i-3) and n >= i) )
    
    loop_progress(n-i)
    
    loop_postcondition( (i-1) == n and fib_i == fib(i-1) )
    
Now, the five part proof:
    1.
    If the python interpreter has gotten to the loop guard, it has failed the conditional tests n <= 2 and n==3.
    Otherwise, the function would have returned some value and the loop guard part of the code would not be read. 
    From the function precondition, we know n > 0 and is an int. This with the understanding that n >2 and n != 3 says n >=4.
    Given that i=4, the loop guard can be substituted for n>= 4. We have shown this to be true, so the loop is always entered.
    This means condition one (if loop is skipped then loop postcondition holds) is vacuously true.
    
    However, it seems important to add that if n ==3, returning 2 is correct since the third fibbonacci number is 2.
    Plus, if n <= 2, given that n is an int > 0 by the function precondition, we know n must equal one or two inside the first conditional. 
    Since the first adn second fibbonacci numbers are both one, this returned 1 is correct. Thus, what I think correctness condition one was
    supposed to show, is shown: all other returns that occur without entering the loop satisfy the postcondtion- of returning the correct fibbonacci number.
    
    
    2.
    
    Suppose True == loop_precondition(i==4 and fib_i == 3 and fib_i_minus_1 == 2 and fib_i_minus_2 == 1 and fib_i_minus_3 == 1 and n >= 4)
    
     Then, the first boolean expression in the structure
     loop_invariant(A or B) is held since A is exactly the loop_precondtion which is assumed.
     So we have loop_invariant( True or 
    (fib_i == fib_i_minus_1 and fib+i_minus_1 == fib(i-1) and fib_i_minus_2 == fib(i-2) and fib_i_minus_3 == fib(i-3) and n >= i) ) 
    which by boolean algebra evaluates to loop_invariant(True)
    
    3.
    
    Since the loop invariant takes into account two conditions, we must show under both conditions
    the loop_invariant holds after the loop body is executed. Hence, we show the two parts:
        A. Suppose (i==4 and fib_i == 3 and fib_i_minus_1 == 2 and fib_i_minus_2 == 1 and fib_i_minus_3 == 1 and n >= 4)
        
        Suppose the following code is executed and the values pass the loop guard at the end (statements are numbered for convenience):
        
1        final_fib_i = 2 * fib_i_minus_1 - fib_i_minus_3
2        final_fib_i_minus_3 = fib_i_minus_2
3        final_fib_i_minus_2 = fib_i_minus_1
4        final_fib_i_minus_1 = final_fib_i
5        final_i = i + 1
        
        We need to show (final_i==4 and final_fib_i == 3 and final_fib_i_minus_1 == 2 and final_fib_i_minus_2 == 1 and final_fib_i_minus_3 == 1 and n >= 4) or 
    (final_fib_i == final_fib_i_minus_1 and final_fib_i_minus_1 == fib(final_i-1) and final_fib_i_minus_2 == fib(final_i-2) and final_fib_i_minus_3 == fib(final_i-3) and n >= final_i)
    
        We do this by showing the part after the 'or' is true.
        First, by merely substituting statement 4, we have final_fib_i == final_fib_i 
        which by boolean algebra is true. Then, for the next part we can substitute final_fib_i_minus_1 for final_fib_i for (2*fib_i_minus_1 - fib_i_minus_3) 
        through variable substitution. Again, through variable substitution, we can substitute (2*fib_i_minus_1 - fib_i_minus_3) as (2*2 -1)-by hypothesis- which is 3. Now,
        the right hand side is fib(final_i -1) which is fib(i) by substituting final_i for i +1
        which is fib(4) by substituting 4 for i -by hypothesis-, which is also 3 (h.s math-the 4th fib number is 3: 1,1,2,3).
        
        We repeat this process for the next two parts of the loop invariant with almost the exact same rules used (variable substitution a
        and use of the hypothesis or first loop invariant):
        
        final_fib_minus_2 == fib_i_minus_1 == 2 == fib(3) == fib(4-1) == fib(i -1) == fib(final_i -1 -1) == fib( final_i -2)
        final_fib_minus_3 == fib_i_minus_2 == 1 == fib(2) == fib(4-2) == fib(i -2) == fib(final_i -1 -2) == fib(final_i -3)
        
        Lastly, we know n >= final_i since we can suppose the loop guard is true- which would now
        just be n>= final_i. 
        
        B.
        Suppose 
        (fib_i == fib_i_minus_1 and fib_i_minus_1 == fib(i-1) and fib_i_minus_2 == fib(i-2) and fib_i_minus_3 == fib(i-3) and n >= i)
        
        and suppose the following was executed and the final values passed the loop guard:
1        final_fib_i = 2 * fib_i_minus_1 - fib_i_minus_3
2        final_fib_i_minus_3 = fib_i_minus_2
3        final_fib_i_minus_2 = fib_i_minus_1
4        final_fib_i_minus_1 = final_fib_i
5        final_i = i + 1

        We need to show the updated loop postcondition is true.
        By boolean algebra it is sufficient to show
        final_fib_i == final_fib_i_minus_1 and final_fib_i_minus_1 == fib(final_i-1) and
        final_fib_i_minus_2 == fib(final_i-2) and final_fib_i_minus_3 == fib(final_i-3) and n >= final_i)
        
        Going in order, the first boolean is just given by statement 4.
        Variable substirution yields final_fib_i = final_fib_i which is True by boolean algebra.
        Then, the right side of the next boolean expression can be substituted as (using variable substitution)
        fib(i +1 -1) == fib(i). Now, the left hand side can work as follows:
            final_fib_i == final_fib_i_minus_1 == 2 * fib_i_minus_1 - fib_i_minus_3 == 2* fib(i-1) - fib(i-3) == fib(i-1) + fib(i-2) == fib(i)
            
            The first and second changes are variable substitution. Then we use the hypothesis to substitute for fib_i_minus_1 and fib_i_minus_3.
            Then, using high school algebra we can show fib(i-1) = fib(i-2) + fib(i-3) -> fib(i-2) = fib(i-1) - fib(i-3)--> [2* fib(i-1) - fib(i-3)] 
            == fib(i-1) + [fib(i-1)+ fib(i-3)] == fib(i-1) + fib(i-2). The last step just uses the recrisve definition of fib(n). 
            
        The next boolean expression has right side of fib(final_i -2) == fib(i-1) by variable subst. The left side is fib_i_minus_1
        which by hypothesis is fib(i-1). Thus fib(i-1) == fib(i-1) evalueates to true by boolean algebra.
        
        The next boolean expression works exaclty the same way: rhs == fib(i-2) and lhs == fib_i_minus_2 == fib(i-2) (by hypothesis)
        
        The last boolean expression is true because we assume the loop guard is true (that n >= final_i). 
        ---------------------------------------------------------------------------------------------
        Hence, in either case of the loop_invariant intiallay holding, it holds again assuming the loop guard is true after
        the loop body is executed.
        
        
        
    4.
    
    There are two parts. First, we know the loop progress expression decreases by one since
    i increases by one. See: (n-(i+1)) = (n-i) -1 [the original progress expression minus one]
    Or.. n- (i+1) < n-i 
    
    Second, if n-i < 0, then n<i and the loop guard n >= i is false, meaning the loop terminates.
    
    Thus, the loop is exited.
    
    5.
    
    Since we know that i only increases by one, the loop will terminate when i = n+1 (because otherwise
     the loop would have run under a false loop guard: n+1 !<= n)
     
     Thus, i = n+1 --> i-1 = n
     
    Second, from substitution using the loop_invariant, we know that 
    fib_i == fib_i_minus_1 == fib(i-1)
    
Part 2: Proving the function as a whole works.
We have already shown in part 1 that the loop_precondition must hold if reached
since the informal if else rules indicate this (the failure of the booleans of the first
two conditionals).
Formally, one would convert the entire function into SSA to show
that if the loop precondition is reached, it holds.


Now, if we suppose the loop postcondition:
    loop_postcondition( (i-1) == n and fib_i == fib(i-1) )
    
    We can just substitute (i-1) == n inside fib_i:
        fib_i == fib(i-1) == fib(n), allgiven by hypothesis.
        
        Thus the function's precondition:
        fib_i == fib(n) 
        holds if the loop_postcondition holds.
        
        

"""


#=================End of Proof================================





# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all fib() tests"
        
n = input("Which element of the Fibonacci sequence? ")
if isinstance(n, int) and n > 0:
    print fib(n)
else:
    print "oh, come on!"

