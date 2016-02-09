"""
Compute base to the exp power, for integer exp>0,
using a straightforward translation of the rules
     base^1 = base
     base^exp = base * base^(exp-1)
There are much more efficient algorithms for exponentiation,
but our emphasis here is on simplicity rather than speed.

For example,
>>> power(3.0, 3)
27.0
>>> power(0.9, 5)  # doctest: +ELLIPSIS
0.59049...
"""

def power(b, e):
    if (e == 1):
        return b
    else:
        return b * power(b, e-1)
    
    
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
    
