"""
Compute base to the exp power, for integer exp>0,
using a straightforward translation of the rules
     base**1 = base
     base**exp = base * base**(exp-1)
There are much more efficient algorithms for exponentiation,
but our emphasis here is on simplicity rather than speed.

Note that we do not allow negative or zero exponents,
  as our current algorithm does not handle them

Examples of the power function:
>>> power(3, 3)
27

>>> power(3.0, 3)  # note that the ".0" is retained in the answer
27.0

>>> power(1.5, 2)   # 3/2 squared is 9/4
2.25

When we don't want to write out _all_ the digits of the answer,
we put the "# doctest: +ELLIPSIS" at the end of the example question, like so
>>> power(0.9, 5)  # doctest: +ELLIPSIS
0.5904900...
"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from logic import *

def power(base, exp):
    precondition(is_integer(exp) and exp > 0)
    """postcondition: the result is the base raised to the exp power,
                      or a close approximation for information that
                      isn't represented exactly (such as real numbers)."""
    if exp == 1:
        return base
    else:
        assert(exp > 1)
        base_to_the_exp_minus_one = power(base, exp-1)
        return base * base_to_the_exp_minus_one


def simple_power_ui():
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    print "First, trying out tests from initial comment in power.py..."   
    doctest.testmod()

    print " "  # get a blank line
    print "Now you try one!"
    users_base = input("Enter the base: ")
    users_exp  = input("Enter the exponent: ")
    if (isinstance(users_exp, int) and users_exp > 0):
        print power(users_base, users_exp)
    else:
        print "Sorry, the exponent must be a positive integer!"

# run the user interface only if we're not importing this for some other program
# I copied this from http://docs.python.org/lib/module-doctest.html
if __name__ == "__main__":
    simple_power_ui()
