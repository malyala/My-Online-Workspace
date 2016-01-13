# direct recursive solution to Fibonacci sequence calculator
# meant to be timed by fib-time.py, so run that to see the timing
# To avoid throwing off the timing, there are no pre- or post-conditions checked

def fib(n):
    # precondition(n is a positive integer)
    # postcondition(fib(n) is the nth element of the Fibonacci sequence
    precondition(is_integer(n) and n>0)
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)



