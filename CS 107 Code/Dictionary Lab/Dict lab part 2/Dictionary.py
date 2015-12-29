"""
  Dictionary class, and two implementations
  (Some of the repr tests for the second one fail but are actually correct because
  the only change is the order of the items)

>>> d = Dictionary()

#It prints using the repr method after each put method is called since each put method
#returns a dictionary instance

>>> d.put('Dave', 4973)
[['Dave', 4973]]
>>> d.put('J.D.', 4993)
[['Dave', 4973], ['J.D.', 4993]]
>>> d.put('CS lab', 1202)
[['CS lab', 1202], ['Dave', 4973], ['J.D.', 4993]]
>>> d.lookup('Dave')
4973
>>> d.put('Dave', 1202)  # when Dave is working in the lab
[['CS lab', 1202], ['Dave', 1202], ['J.D.', 4993]]
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

                        #Eq tests:
                        
>>> a,b = Dictionary(), Dictionary()
>>> a == b
True
>>> a.put("Test", 42)
[['Test', 42]]
>>> a==b
False
>>> b.put("Test", 42)
[['Test', 42]]
>>> a==b
True
>>> a.put("Something Funny", 24).put("Something even funnier", 25)
[['Something Funny', 24], ['Something even funnier', 25], ['Test', 42]]
>>> a == b
False
>>> b.put("Something even funnier", 25).put("Something Funny", 24)
[['Something Funny', 24], ['Something even funnier', 25], ['Test', 42]]
>>> a == b
True



            # Add some tests of "merge" here:

>>> b.put("You're good! You're good!", 31)
[['Something Funny', 24], ['Something even funnier', 25], ['Test', 42], ["You're good! You're good!", 31]]
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
>>> e.lookup("Test")
1000


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

 




#============================================================================================
#As cited for the second class, I also use some ideas (namely binary search and, merge sort notions)
# from my EDx course with the accompanied text (both cited for dictionary2 below)
#============================================================================================
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
    # in which case, we replace the value for key k with v
    def withEntry(self, key, value):
        ret = Dictionary1()
        ret.__listOfPairs = self.__listOfPairs[::]
        ret.put(key, value) # I am lazy.
        self.__rep_inv__()
        ret.__rep_inv__()
        return ret

    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):                                       ##++++ Need to update w/binary search 
        precondition(True)
        #really, our precondition is if the list in self is key values pairs sorted by key
        def bs(alist, key, low, high):
                #precondition: alist is sorted appropreately and 
                #low, high are valid indicies of alist
            mid = (low + high) /2
            if low ==high:
                #postcond: if we have a value for a key, return it, else give "No entry"
                if alist[low][0] == key: return alist[low][1]
                else: return "No entry"
            #postcond: if we have a value for a key, return it, else give "No entry"
            elif alist[mid][0]==key: return bs(alist, key, mid, mid)
            #postcond: if we have a value for a key, return it, else give "No entry"
            elif alist[mid][0] > key: return bs(alist, key, low, mid-1)
            #postcond: if we have a value for a key, return it, else give "No entry"
            else: return bs(alist, key, mid+1, high)
            
        #postcond: if we have a value for a key, return it, else give "No entry"
        return bs(self.__listOfPairs, key,  0, len(self.__listOfPairs)-1)

    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    #  d.put(k, v) returns the updated d, so d.put(k1, v1).put(k2, v2) is legal
    def put(self, key, value):
        precondition(True)
        
        def Bisec_insert(alist, low, high, key, value):
            mid = (low + high)/2 # since low high are indexes, mid will always be an int in python 2
            
            if high == -1: # we have an empty list
                alist.append([key, value])
            elif low == high:
                if alist[low][0] == key:
                    alist[low][1] = value
                elif alist[low][0] > key:
                    alist.insert(low, [key, value]) #insert in python inserts right before the value determined by the given index
                else:
                    alist.insert(low+1, [key, value])        
            elif alist[mid][0]== key:
                Bisec_insert(alist, mid, mid, key, value)
            elif alist[mid][0] > key:
                Bisec_insert(alist, low, mid, key, value)
            else:
                Bisec_insert(alist, mid+1, high, key, value)
                
        alist = self.__listOfPairs
        Bisec_insert(alist,0,len(alist)-1, key, value)
        self.__rep_inv__()
        return self
                
    def __eq__(self,otherd):               #for sorted lists, give the simple recursive matching with an inner list comparison
        precondition( isinstance(otherd,Dictionary1) )
        "replace this with your equality test" 
        if len(self.__listOfPairs) != len(otherd.__listOfPairs): return False
        for i in range(len(self.__listOfPairs)):
            if self.__listOfPairs[i] != otherd.__listOfPairs[i]:
                return False
        return True
  
    # axioms:
    #Dictionary1().merge(Dictionary1()) === Dictionary1()
    #D.withEntry(k,v).merge(C) === D.merge(C).withEntry(k,v)
    #D.merge(C.withEntry(k,v)) === D.merge(C).withEntry(k,v) iff D does not have the key k or has the same key-value pair
    #D.withEntry(k,v1).merge(C.withEntry(k,v2)) === D.merge(C).withEntry(k,v1)
    def merge(self, otherDictionary):                                    # this is easy with two sorted lists 
        precondition( isinstance(otherDictionary,Dictionary1) )
        """
        merge two dictionaries and return a composite
        If there is a repeated key, the value if of the first dictionary, called self
        
        """
        ret = Dictionary1()
        L = ret.__listOfPairs
        first, other = self.__listOfPairs[::], otherDictionary.__listOfPairs[::] #this is inefficient copying if we have large dictionaries
        while len(first) != 0 and len(other) !=0:
            if first[0][0] <= other[0][0]: #recall: we side with the first if they are equal keys
                L.append(first[0])
                first = first[1:]
            else:
                L.append(other[0])
                other = other[1:]
        L += first + other
        
        self.__rep_inv__()
        otherDictionary.__rep_inv__()
        ret.__rep_inv__()
        return ret

  
    def __repr__(self):
        precondition(True)
        return str(self.__listOfPairs)
        
        
        
        
    def __rep_inv__(self): # each element except last is less than or equal to next element
        for i in range(len(self.__listOfPairs)-1): #range(-1) == [] so no error for singelton list
            if self.__listOfPairs[i][0] > self.__listOfPairs[i+1][0]: raise AssertionError("The sorted list rep inv has failed.")
           

#==============================================================================================
#   For this Dictionary2 class, I use many ideas and some similar code from
#   the Python MIT Edx course taught by Eric Grimson
#   There is a text that accompanies this course: Introduction to Computation And Programming 
#   Using Python -John Guttag
#==============================================================================================



from BinaryTree import *
from copy import deepcopy
class Dictionary2:
    """
        A dictionary represented with a binary tree
        For any node, all items with values less than that node are to the left
        and all values greater or equal to are to the right
        
    """

    def __init__(self):
        precondition(True)
        self.tree = BinaryTree(None) # we define new dictionaries to have the value None in the root of their tree

    # "extending" constructor method: 'withEntry'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
    def withEntry(self, key, value):
        precondition(True)
        ret = deepcopy(self)
        assert(self.__rep_inv__() and ret.__rep_inv__())
        return ret.put(key, value) #a pure fuctional one is just a mutation of a copy

    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
        
        def treelook(tree, key):
            #precondition: the tree is not a leaf, as in, it is not None but a BinaryTree instance
            #it must either have a [key, value] as it's value or have a None (be an empty dictionary)
            
            if tree.get_val() is None: #empty dictionary
                #postcond: if there is a value for key, we give it. Otherwise, we give 'No entry'
                return "No entry"
            elif tree.get_val()[0] == key:
                #postcond: if there is a value for key, we give it. Otherwise, we give 'No entry'
                return tree.get_val()[1]
            elif tree.get_val()[0] > key:
                #postcond: if there is a value for key, we give it. Otherwise, we give 'No entry'
                if tree.get_left(): return treelook(tree.get_left(), key)
                else: return "No entry"
            else:
                #postcond: if there is a value for key, we give it. Otherwise, we give 'No entry'
                if tree.get_right(): return treelook(tree.get_right(), key)
                else: return "No entry"
                
        #postcond: if there is a value for key, we give it. Otherwise, we give 'No entry'       
        return treelook(self.tree, key)

    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    #  d.put(k, v) returns the updated d, so d.put(k1, v1).put(k2, v2) is legal
    def put(self, key, value): # you overide values of duplicates
        
        def Bput(tree, key, val):
            if tree.get_val() is None or tree.get_val()[0] == key: #if we have a new dict or the same key, we overdide the value
                tree.value = [key, val]
            elif tree.get_val()[0] > key: #if the key is less than the current tree's key we check if we can add it to the left, otherwise call recursively on the left node
                if tree.get_left(): Bput(tree.get_left(), key, val)
                else: tree.add_left([key, val])
            else: 
                if tree.get_right(): Bput(tree.get_right(), key, val)# same as left but for right side
                else: tree.add_right([key, val])
                
        Bput(self.tree, key, value) # this is just the call made
        assert(self.__rep_inv__())
        return self
     
    def __eq__(self, other):

        if self.tree.get_val()== None or other.tree.get_val() == None: #relies on definition of a new tree
            return self.tree.get_val() == other.tree.get_val()

        def is_one_good(all_of_this, in_this):
            stack = [all_of_this.tree]
            while len(stack) > 0:
                first = stack.pop()        
                if in_this.lookup(first.get_val()[0]) == "No entry": return False
                if first.get_left():
                    stack.append(first.get_left())
                if first.get_right():
                    stack.append(first.get_right())
            return True
                    # we check we can lookup each element in each other tree
        return is_one_good( self, other) and is_one_good(other, self)
    
    # axioms:
    #Dictionary2().merge(Dictionary2()) === Dictionary2()
    #D.withEntry(k,v).merge(C) === D.merge(C).withEntry(k,v)
    #D.merge(C.withEntry(k,v)) === D.merge(C).withEntry(k,v) iff D does not have the key k or has the same key-value pair
    #D.withEntry(k,v1).merge(C.withEntry(k,v2)) === D.merge(C).withEntry(k,v1)
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2))
        ret = deepcopy(otherDictionary)
        
        stack = [self.tree]
        while len(stack) > 0:
            first = stack.pop()
            val = first.get_val()[::]
            ret.put(val[0],val[1]) # we add each element of the first to the second so that the first ovverides any duplicates in the second
            if first.get_left():
                stack.append(first.get_left())
            if first.get_right():
                stack.append(first.get_right())
        assert(self.__rep_inv__() and otherDictionary.__rep_inv__() and ret.__rep_inv__())
        return ret

    def __repr__(self):
        ret = []
        stack = [self.tree]
        # we make a list of all the values (key-val pairs) and make it a string
        while len(stack) > 0:
            first = stack.pop()
            ret += [first.get_val()]
            if first.get_left():
                stack.append(first.get_left())
            if first.get_right():
                stack.append(first.get_right())
                
        return  str(ret)
            

    def __rep_inv__(self):
        if self.tree.get_val() == None: return true
        
        def rep(tree):
            
            left, right = True, True #this is tricky: read my comments on the assignment of left closely
            if tree.get_left():
                if tree.get_val()[0] <= tree.get_left().get_val()[0]: return False
            else: left = False # mark left as false so I don't need to make a recursive call
            
            if tree.get_right():
                if tree.get_val()[0] > tree.get_right().get_val()[0]: return False
            else: right = False
            
            if left: # if there is a left, check that it is correct, otherwise make 'left' true
                left = rep(tree.get_left())
            else: left = True
            if right:
                right = rep(tree.get_right())
            else: right = True           
            return left and right #if we had a left brach, its recursive call would be here, otherwise, we just have left = true
            
            
        return rep(self.tree)
            
            
                
                
                



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



