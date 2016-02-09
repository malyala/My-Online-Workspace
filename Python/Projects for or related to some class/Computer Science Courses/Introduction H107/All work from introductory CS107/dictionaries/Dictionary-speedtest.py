"""
    funcTime(function, repeats):
      Run the function _function_ for _repeats_ iterations,
      then return the average elapsed time (from cs105)

    testDictionarySpeeds(nEntries, nLookups, maxLookup, seed=-1):
      Do some speed tests of the dictionary classes with random data
      (set 'seed' to re-use same random numbers each time)

#>>> testDictionarySpeeds(10, 3, 10, 42)  # just see if the testing system works

#>>> testDictionarySpeeds(100, 300, 150, 42)  # find what you're looking for 2/3 of the time

#>>> testDictionarySpeeds(10000, 300, 10100, 42) # Haverford has 4-digit extensions, so try that size

>>> testDictionarySpeeds(10000, 30000, 10100, 42) # like the above, but more lookups

"""

import time
from Dictionary_Faster import Dictionary1, Dictionary2
from BinaryTree import *
def funcTime(function, repeats=0, minTime=0.250):
    """
        Run FUNCTION for REPEATS repetitions,
         and return the average time taken.
        If REPEATS is 0 or missing,
         run for MINTIME (default 1/4sec) consecutive calls
    """
    r = repeats if repeats != 0 else 1
    done = False
    while not done:
        start = time.clock()
        for i in range(0,r):
            function()
        end = time.clock()
        if repeats>0 or end-start>minTime:
            done=True
        else:
            r = r*2
#    print("     R was "+str(r))
    return (end-start)/(r*1.0)



# the following two functions are for timing; note that 'entries' to be added, 
#  and 'lookups' to be done, are pre-built Python lists, to avoid timing the
#  work of any shuffling or whatever must be done to choose these lists

def addRandomEntries(someDictionary, entries):
    for e in entries:
        someDictionary.put(e[0], e[1])

def lookupABunch(someDictionary, lookups):
    for l in lookups:
        someDictionary.lookup(l)  # good thing there's no optimizer for Python, or it would just skip this


def testDictionarySpeeds(nEntries, nLookups, maxLookup, seed=-1): # set seed to something >0 for repeatable tests
    # build random workloads:
    import random
    entries = []
    lookups = []
    for num in range(nEntries):
        entries.append((num, 'x'))  # key is 'num', value is 'x'
    if seed >= 0:
        random.seed(seed)
    random.shuffle(entries)
    for l in range(nLookups):
        lookups.append(random.randint(0,maxLookup-1))

    # create dictionaries and test procedures
    d1 = Dictionary1()
    d2 = Dictionary2()

    def test1e(): return addRandomEntries(d1, entries)
    def test1l(): return lookupABunch(d1, lookups)
    def test2e(): return addRandomEntries(d2, entries)
    def test2l(): return lookupABunch(d2, lookups)

    return [ "#1 put:", funcTime(test1e),
             "#2 put:", funcTime(test2e),
             "#1 lookup:", funcTime(test1l),
             "#2 lookup:", funcTime(test2l)
             ]


# copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    # print "Result of doctest is:", result
    if result[0] == 0:
        print("Wahoo! Passed all " +str(result[1])+ " tests!")
    else:
        print("Rats!")

if __name__ == "__main__":
    _test()
    def nothing(): return
    print("Note: calling nothing seems to take about " + str(funcTime(nothing, 1000000)) + " seconds on this computer")

