"""
Compute b to the e power, for integer e>0,
using the imperative paradigm's description:
    start with b as the result,
        and keep multiplying by b and count the number of e's we've done,
        until we've done all the e's

For example,
>>> power(3.0, 3)
27.0
>>> power(0.9, 5)  # doctest: +ELLIPSIS
0.59049...
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

def orig_power(b, e):
    precondition(isinstance(e, int) and e > 0)
    # postcondition: the result is b to the e power
    if (e == 1):
        return b
    else:
        return b * orig_power(b, e-1)

def power(b, e):
    precondition(isinstance(e, int) and e > 0)
    exp_so_far = 1
    result_so_far = b
    loop_precondition(exp_so_far == 1 and b == result_so_far and exp_so_far <= e)
    while exp_so_far < e:
        loop_invariant(orig_power(b, exp_so_far) == result_so_far and
                       exp_so_far <= e)
        loop_progress(e - exp_so_far)
        exp_so_far = exp_so_far + 1
        result_so_far  = result_so_far * b
    loop_postcondition(exp_so_far == e and orig_power(b, exp_so_far) == result_so_far)
    
    postcondition(orig_power(b, e) == result_so_far)
    return result_so_far
    
    
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
    # print "Result of doctest is:", result
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__":
    print "First, running Doctest tests:"
    _test()
    print "Now you try one!"
    simple_power_ui()


# HERE ARE THE FIVE STEPS OF PROVING THE LOOP IS CORRECT,
#   (PLUS THE TWO OTHER STEPS FOR THE FUNCTION INCLUDING THE LOOP, GIVEN BELOW)
#
#   I. IF WE SKIP THE LOOP, THE LOOP POSTCONDITION HOLDS
#      (i.e. the loop precondition and condition under which the loop is skipped
#       together give us the loop postcondition).
#
#    We skip the loop if exp_so_far >= e  (since it runs while exp_so_far<e)
#    From loop precondition, we know exp_so_far <= e,
#     for both of these to be true (to skip the loop), exp_so_far == e
#    Since we know result_so_far == b (also from loop precond.)
#     and orig_power(b, 1) == b (from the definition of orig_power)
#     we now know both parts of the postcondition.
#
#  II. WHEN ENTERING THE LOOP, THE INVARIANT IS TRUE
#      (i.e. the loop precondition (and, if necessary, the
#       condition under which the loop is executed) gives us the invariant)
#
#    The loop precondition is
#          exp_so_far == 1 and b == result_so_far and exp_so_far <= e
#       Since b == orig_power(b, 1) and exp_so_far == 1,
#          we know b == orig_power(b, exp_so_far) and exp_so_far <= e
# 
# III. THE INVARIANT IS INVARIANT
#      (i.e. the loop invariant and what happens in the loop body
#       together give us the loop invariant again).
#
#    At the start of the loop body, we know the invariant is true
#    for the initial values of the variables and that we've entered the loop
#          result_so_far1 == orig_power(b, exp_so_far1)    (from the invariant)
#           and exp_so_far1 < e                      (since we're in the loop)
#    Note that if we multiply both sides of the first line by "b" we get
#          result_so_far1 * b == orig_power(b, exp_so_far1) * b
#           and exp_so_far1 < e
#    Note that if we add one to each side of the second line we get
#          result_so_far1 * b == orig_power(b, exp_so_far1) * b
#           and exp_so_far1+1 < e+1
#    or, since x < e+1 is the same as x<= e (for integers), this is:
#          result_so_far1 * b == orig_power(b, exp_so_far1) * b
#           and exp_so_far1+1 <= e
#    The definition of orig_power lets us simplify the right-hand side of the first line:
#          result_so_far1 * b == orig_power(b, exp_so_far1+1)
#           and exp_so_far1+1 <= e
#    The loop body in SSA tells us:
#          result_so_far2 = result_so_far1 * b
#          exp_so_far2 = exp_so_far1 + 1
#    Substituting these into our modified loop invariant, we find
#          result_so_far2 == orig_power(b, exp_so_far2)
#           and exp_so_far2 <= e
#    Q.E.D. -- the invariant is true for the values at the bottom of the loop body
#
#  IV. PROGRESS IS MADE IN THE LOOP
#      (i.e. (a) having the progress expression <= 0 makes the loop stop, and
#            (b) the progress expression gets smaller each time.)
#
#    (a) To show that progress <= 0 will make the loop stop, we need to show
#         that it is the opposite of the condition that lets the while keep going
#        For this example, we need to show that e-exp_so_far <= 0
#         is the same as exp_so_far >= e.
#        We start with the condition progress <= 0:
#            e-exp_so_far <= 0
#        Now add "exp_so_far" to both sides:
#            e <= exp_so_far
#        Finally, rewrite the <= as >= by switching the sides:
#            exp_so_far >= e
#        which is what we needed to derive.
#    (b) To show the progress expression gets smaller, we need to show that
#          the progress expression with the values at the end of the loop body
#          (i.e., exp_so_far2) is smaller than the progress expression with
#          the values of variables at the end of the start of the loop body, i.e,
#          we need to show
#                    e-exp_so_far2 < e-exp_so_far1
#          we substitute the definition of exp_so_far (see Step III above)
#                e-(exp_so_far1+1) < e-exp_so_far1
#          now subtract "e" from both sides
#                   -(exp_so_far1+1) < -exp_so_far1
#          and distribute the "-" on the left side
#                    -exp_so_far1-1  < -exp_so_far1
#          and finally add exp_so_far1 to both sides, giving
#                                 -1 < 0
#          clearly this is true.
#
#   V. IF WE EXIT FROM THE LOOP BODY, THE POSTCONDITION HOLDS
#      (i.e. the loop invariant and the condition under which we leave the loop
#       together give us the loop postcondition).
#
#    when getting out of the loop, exp_so_far >= e
#     substituting this into the loop invariant gives us the postcondition
#
#
# To show the function as a whole is correct,
#   we must also show the loop precondition must hold
#   (based on the funciton's precondition and the statements before the loop),
#   and show the function's postcondition must hold
#   (based on the loop postcondition and the statements after the loop).
#
# These are both simple substitutions


