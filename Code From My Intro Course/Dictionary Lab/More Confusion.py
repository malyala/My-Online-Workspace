"""
  Dictionary class, and two implementations

>>> d = Dictionary()

#It prints using the repr method after each put method is called since each put method
#returns a dictionary instance
>>> d.put('Dave', 4973)
[('Dave', 4973)]
>>> d.put('J.D.', 4993)
[('J.D.', 4993), ('Dave', 4973)]

>>> d.put('CS lab', 1202)
[('CS lab', 1202), ('J.D.', 4993), ('Dave', 4973)]

>>> d.lookup('Dave')
4973

>>> d.put('Dave', 1202)  # when Dave is working in the lab
[('Dave', 1202), ('CS lab', 1202), ('J.D.', 4993)]
>>> d.lookup('Dave')
1202
>>> d.lookup('CS lab')
1202

>>> d.lookup('Steven')
'No entry'

>>> d2 = d.withEntry('Steven', 1203)
>>> d.lookup('Steven')
'No entry'

>>> d2.lookup('Steven')
1203

>>> a,b = Dictionary(), Dictionary()
>>> a == b
True
>>> a.put("Test", 42)
[('Test', 42)]
>>> a==b
False
>>> b.put("Test", 42)
[('Test', 42)]
>>> a==b
True
>>> a.put("Something Funny", 24).put("Something even funnier", 25)
[('Something even funnier', 25), ('Something Funny', 24), ('Test', 42)]
>>> a == b
False
>>> b.put("Something even funnier", 25).put("Something Funny", 24)
[('Something Funny', 24), ('Something even funnier', 25), ('Test', 42)]
>>> a == b
True

# Add some tests of "merge" here

>>> b.put("You're good! You're good!", 31)
[("You're good! You're good!", 31), ('Something Funny', 24), ('Something even funnier', 25), ('Test', 42)]
>>> c = b.merge(a)
>>> b.lookup("You're good! You're good!")
31
>>> a.lookup("You're good! You're good!")
'No entry'
>>> e = Dictionary().put("Test", 1000)
>>> f,g = e.merge(a), a.merge(e)
>>> f.lookup("Test")
1000
>>> g.lookup("Test")
42







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



class Dictionary1:
    """
        A dictionary represented with a Python list.
        Each list element is a tuple of two parts, the key and the value
    """
    def __init__(self):
        precondition(True)
        self.__listOfPairs = []

    # "extending" constructor method: 'withEntry'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry unless d has the key k
    # in which case, a copy is returned
    def withEntry(self, key, value):
        add= True
        ret = Dictionary1()
        ret.__listOfPairs = self.__listOfPairs
        for i in self.__listOfPairs:
            if i[0] == key:
                add = False
        if add:
            ret.__listOfPairs = [(key, value)] + ret.__listOfPairs
        return ret

    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
        for pair in self.__listOfPairs:
            if pair[0] == key:
                return pair[1]
        return "No entry"

    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    #  d.put(k, v) returns the updated d, so d.put(k1, v1).put(k2, v2) is legal
    def put(self, key, value):
        precondition(True)
        # WHEN ready, change to inserting sorted by value using binary search to sort it
        pairs = self.__listOfPairs[::]
        not_changed = True
        for i in pairs:
            if key == i[0]:
                not_changed = False
                self.__listOfPairs.remove(i)
                self.__listOfPairs = [(key, value)] + self.__listOfPairs
        if not_changed:
            self.__listOfPairs = [(key, value)] + self.__listOfPairs
        return self
                
    def __eq__(self,otherd):
        precondition( isinstance(otherd,Dictionary1) )
        "replace this with your equality test" 
        if len(self.__listOfPairs) != len(otherd.__listOfPairs): return False
        for i in self.__listOfPairs:
            match = otherd.lookup(i[0])
            if match ==  "No entry" or i[1] != match:
                return False
        return True
  
    # axioms:
    #Dictionary1().merge(Dictionary1()) === Dictionary1()
    #D.withEntry(k,v).merge(C) === D.merge(C).withEntry(k,v)
    #D.merge(C.withEntry(k,v)) === D.merge(C).withEntry(k,v) iff D does not have the key k or has the same key-value pair
    #D.withEntry(k,v1).merge(C.withEntry(k,v2)) === D.merge(C).withEntry(k,v1)
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1) )
        """
        merge two dictionaries and return a composite
        If there is a repeated key, the value if of the first dictionary, called self
        
        """
        ret = Dictionary1()
        ret.__listOfPairs = self.__listOfPairs[::] 
        for i in otherDictionary.__listOfPairs:
            if self.lookup(i[0]) == "No entry":
                ret.__listOfPairs += i
        return ret
  
    def __repr__(self):
        precondition(True)
        return str(self.__listOfPairs) 


from BinaryTree import *
from random import *
from copy import deepcopy
class Dictionary2:
    """
        A dictionary represented with a binary tree
        For any node, all items with values less than that node are to the left
        and all values greater or equal to are to the right
        
        Also, all keys are strings !!!
    """

    def __init__(self):
        precondition(True)
        self.d = BinaryTree(None)


    # "extending" constructor method: 'withEntry'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
    def withEntry(self, key, value):
        precondition(True)
        ret = deepcopy(self)
        #now we use the same modifying algorithm as for put
        return ret.put(key, value)
        

    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
        
        stack = [self.d]
        if self.d.get_val() is None:
            return "No entry"
        
        while len(stack) != 0:
            first = stack.pop()
            if first.get_val()[0] == key:
                return first.get_val()[1]
            if first.get_left():
                stack.append(first.get_left())
            if first.get_right():
                stack.append(first.get_right())
        return "No entry"
        
        
        
        
        
        
        
        return "No entry"

    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    #  d.put(k, v) returns the updated d, so d.put(k1, v1).put(k2, v2) is legal
    def put(self, key, value):
        ## need to make it so that no duplicates can be added!!!
        
        precondition(True)
        c_node = self.d
        
        if c_node.get_val() is None:
            c_node.value = [self, key]
            return self
        
        direction = randint(2,20)%2
        while  not c_node.partial_leaf():
            if direction == 1: c_node = c_node.get_left()
            else: c_node = c_node.get_right()
            direction = randint(2,20)%2
        
        if c_node.is_leaf():
            if direction == 0: c_node.add_left([key, value])
            else: c_node.add_right([key, value])
        elif not c_node.left: c_node.add_left([key, value])
        else: c_node.add_right([key, value])
        return self
        
        

    def __eq__(self,otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2) )
        return False




    # axioms:
    #Dictionary2().merge(Dictionary2()) === Dictionary2()
    #D.withEntry(k,v).merge(C) === D.merge(C).withEntry(k,v)
    #D.merge(C.withEntry(k,v)) === D.merge(C).withEntry(k,v) iff D does not have the key k or has the same key-value pair
    #D.withEntry(k,v1).merge(C.withEntry(k,v2)) === D.merge(C).withEntry(k,v1)
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2) )
        
  
  #Here, I used a search algorithm from a MIT Python Edx course taught by Eric Grimson
    def __repr__(self):
        
        return self.d.__repr__()
        
        precondition(True)
        tree = self.d
        stack =[tree]
        ret = []
        while len(stack) != 0:
            first = stack.pop()
            ret += [first.get_val()]
            if first.get_right():
                stack.append(first.get_right())
            if first.get_left():
                stack.append(first.get_left())
        return str(ret)
            
            






# by default, use the first representation, but this is changed in DocTest below
Dictionary = Dictionary1

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Dictionary
    whatever_dictionary_was = Dictionary

    print "=========================== Running doctest tests for Dictionary1 ===========================\n"
    Dictionary = Dictionary1
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"

    print "\n\n\n\n"
    
    print "=========================== Running doctest tests for Dictionary2 ===========================\n"
    Dictionary = Dictionary2
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"
    Dictionary = whatever_dictionary_was
    

if __name__ == "__main__":
    _test()



