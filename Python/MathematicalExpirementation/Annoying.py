
from math import sqrt

def f(x):
    assert(type(x)==int and x >0)
    if x==1:
        return sqrt(2)
    else:
        return sqrt(2 + f(x-1))


def PercBound(y):
    def g(x):
        if x==1:
            return sqrt(2)
        else:
            return y*g(x-1)
    return g

def testfor(n):
    g = PercBound((2-sqrt(2))/2.0)
    for i in range(1,n):
        print(i,"g(i)", g(i), "f(i)", f(i),  g(i) <= f(i))




