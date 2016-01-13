"""
Compute base to the exp power, for integer exp>0, in a slightly different way.
Ultimately, of course, it should produce the same answers as before:

For example,
>>> power(3.0, 3)
27.0
>>> power(3.0, 5)
243.0
>>> power(0.9, 5)  # doctest: +ELLIPSIS
0.59049...

But it will do this by making use of power_with_hint,
  which will be told both the *question* (what base and exp are we asking about)
  and a hint, in the form of the same base to a smaller exponent.
The hint will show up as two parameters:
   exp_of_hint (3rd parameter) is the smaller exponent used in the hint,
   hint_value (4th parameter) is the base to that smaller value.

So, if we were finding 3**5, we could give the hint that 3**3 is 27:
>>> power_with_hint(3.0, 5, 3, 27.0) 
243.0

An even more helpful hint would be the value of 3**4:
>>> power_with_hint(3.0, 5, 4, 81.0) 
243.0

Or a less helpful but still correct hint would be the value of 3**2 
>>> power_with_hint(3.0, 5, 2, 9.0)
243.0

Of course, we should always get 243.0 as the answer to 3**5,
regardless of the hint.
If the function actually makes use of the hint, it is likely to get
the wrong answer if the hint is wrong, so we'll make that part of
our precondition, to rule out something like
   power_with_hint(3.0, 5, 3, 81.0)  <--- NOT a legal use of power_with_hint

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


# original power function for use in assertions below;
#  we do NOT need to prove it correct
def orig_power(b, e):
    precondition(is_number(b) and is_integer(e) and e > 0)
    # postcondition: the result is b to the e power
    if (e == 1):
        return b
    else:
        return b * orig_power(b, e-1)


def power_with_hint(b, e, exp_of_hint, hint_value):
    precondition(is_number(b) and is_number(hint_value) and is_integer(exp_of_hint) and
                 is_integer(e) and e > 0 and
                 exp_of_hint <= e and
                 orig_power(b, exp_of_hint) == hint_value # or b**exp_of_hint == hint_value
                 )
    progress(e - exp_of_hint)
    if exp_of_hint == e:
        result = hint_value
        postcondition(result == orig_power(b, e)) # or result == b**e
        return result
    else:
        result = power_with_hint(b, e, exp_of_hint + 1, b*hint_value)
        postcondition(result == orig_power(b, e))
        return result

def power(b, e):
    precondition(is_number(b) and is_integer(e) and e > 0)

    result = power_with_hint(b, e, 1, b)
    postcondition(result == orig_power(b, e))
    return result
    
    
def simple_power_ui():
    users_base = input("Enter the base, or 0 to quit: ")
    while users_base > 0:
        users_exp  = input("Enter the exponent: ")
        if (isinstance(users_exp, int) and users_exp > 0):
            print power(users_base, users_exp)
        else:
            print "Sorry, the exponent must be a positive integer!"
        users_base = input("Enter the base, or 0 to quit: ")
        

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__":    _test()


"""
To prove "power" correct, we use the usual steps for proving functions:
 1. Show the precondition must hold for each function that is called
 2, Show that the postcondition must hold at each return
 3. For recursive functions, show that progress is made
(Since power calls upon power_with_hint, we will need a proof for it too;
 we don't normally do proofs for functions mentioned only in assertions,
 such as orig_power, though).

To make these work, we'll need to have pre- and post conditions for each
 function, and progress expressions for each recursive function.
These appear in the program above, and make reference to orig_power so
 they can be checked as the program runs.

Taking the functions in the order they appear above, we prove power_with_hint first:

 1. power_with_hint calls only upon itself and ==, +, -, and *.
    The last 4 work for any numeric values (unlike /),
        and work with numbers (from the precondition), so they are fine.
    The precondition for the called function (power_with_hint) follows from three things:
      a. the precondition held at the start of power_with_hint
      b. the definitions of the parameters in the call:
      c. the definition of power_with_hint

    (The above constitutes a "semi-detailed" proof;
     detail for the call to power_with_hint is spelled out below:)

    We NEED TO PROVE the precondition of the called function works with the values given in the call:
     NEED_TO_PROVE:    is_number(b given in call)
     NEED TO PROVE:    is_number(hint_value given in call) 
     NEED_TO_PROVE:    is_integer(exp_of_hint given in call) 
     NEED_TO_PROVE:    is_integer(e given in call)
     NEED TO PROVE:    e given in call > 0 
     NEED_TO_PROVE:    exp_of_hint given in call <= e given in call
     NEED_TO_PROVE:    orig_power(b given in call, exp_of_hint given in call) == hint_value given in call
     
     Let's take those one at a time:

     NEED_TO_PROVE:    is_number(b given in call)  [BORING]
         we can assume is_number(b) is true    (It's the precondition of the function we're proving)
         b given in call = b                   (given in the function call itself)
         is_number(b given in call)            (substitute #2 into #1)
         
     NEED TO PROVE:    is_number(hint_value given in call)  [BORING]
         is_number(b) and is_number(hint_value)     (precondition of the function we're proving)
         hint_value given in call = b*hint_value    (given in the function call itself)
         is_number(hint_value given in call)        (substitute #2 into #1, grade-school math (* is closed on numbers))

     NEED_TO_PROVE:    is_integer(exp_of_hint given in call)  [BORING]
         is_integer(exp_of_hint)                    (precondition of the function we're proving)
         exp_of_hint given in call = exp_of_hint+1  (given in the function call itself)
         is_integer(exp_of_hint given in call)      (substitute #2 into #1, grade-school math (+ is closed on integers))
     
     NEED_TO_PROVE:    is_integer(e given in call)  [BORING]
         is_integer(e)                          (precondition of the function we're proving)
         e given in call = e                    (given in the function call itself)
         is_integer(e given in call)            (substitute #2 into #1)

     NEED TO PROVE:    e given in call > 0  [BORING]
         e > 0                                  (precondition of the function we're proving)
         e given in call = e                    (given in the function call itself)
         e given in call > 0                    (substitute #2 into #1)
         
     NEED_TO_PROVE:    exp_of_hint given in call <= e given in call    [AT LAST, NOT TOTALLY TRIVIAL]
         exp_of_hint <= e                              (precondition of the function we're proving)
         e != exp_of_hint                              (the call is in the "else" part of "if e == exp_of_hint")
         exp_of_hint < e                               (two steps above, with grade-school math (x<=y and x!=y means x<y)
         is_integer(exp_of_hint)                       (precondition of the function we're proving)
         exp_of_hint+1 <= e                            (grade-school math two steps above i<j and i+1<=j are the same for integers)
         exp_of_hint given in call = exp_of_hint+1     (given in the function call)
         e given in call = e                           (given in the function call)
         exp_of_hint given in call <= e given in call  (substitute two above steps into the one above that)
         
     NEED_TO_PROVE:    orig_power(b given in call, exp_of_hint given in call) == hint_value given in call
         orig_power(b, exp_of_hint) = hint value       (precondition of the function we're proving)
         b ** exp_of_hint = hint_value                 (postcondition of orig_power)
         b * b ** exp_of_hint = b*hint_value           (multiply both sides by b)
         b ** (exp_of_hint+1) = b*hint_value           (high-school math: x * x**y = x**(y+1)
         exp_of_hint given in call = exp_of_hint+1     (given in the function call)
         hint_value given in call = b*hint_value       (given in the function call)
         orig_power(b given in call, exp_of_hint given in call) = hint value given in call      (substitute two above steps into the one above that)

              
 2. (fully detailed)
    There are two returns from power_with_hint:
    In the first, inside "if (e == exp_of_hint)", is
        return hint_value
    From the precondition, we know hint_value == orig_power(b, exp_of_hint), so we substitute:
        return orig_power(b, exp_of_hint)
    From the if condition, we know e == exp_of_hint, so we substitute and get
        return orig_power(b, e)
    This is the postcondition.

    In the second return, in the "else" of this if, is
        return power_with_hint(b, e, exp_of_hint + 1, b*hint_value)
    While this looks daunting, we can replace a function call with it's postcondition, getting
        return orig_power(b, e)
    Once again, this is the postcondition!

 3. (semi-detailed level)
        power_with_hint is recursive, so there must be _no_ recursive call when
           its progress expression is <= 0, and the progress expression must
           get smaller in each recursive call.
     i. Since we know exp_of_hint <= e (from the precondition), and the recursive call
           is made only if exp_of_hint != e, we know there is no call made for e < 1.
    ii. Since the recursive call uses exp_of_hint+1 for the new exponent,
           e - exp_of_hint gets smaller.

The proof for power is much simpler 
if we omit the details about which type of value each variable has:

 1. power calls only on power_with_hint, which has the precondition
             orig_power(b, exp_of_hint) == hint_value and exp_of_hint <= e
    substituting the definitions of exp_of_hint (1) and hint_value (b), we get
             orig_power(b, 1) == b and 1 <= e
    The first follows from the definition of orig_power;
    the second from power's postcondition

 2. power has only one return:
        return power_with_hint(b, e, 1, b)
    We can replace the call to power_with_hint with power_with hint's postcondition, getting
        return orig_power(b, e)
    And thus we have proved power meets its own postcondition (that it returns orig_power(b, e))

 3. power is not recursive, so no progress needs to be shown for it.
"""
