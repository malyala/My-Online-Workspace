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


import sys
sys.path.append('/home/courses/python')
from logic import *





class Dictionary1:
    """
        A dictionary represented with a Python list.
        Each list element is a tuple of two parts, the key and the value
    """
    def __init__(self):
        self.__listOfPairs = []

    def withEntry(self, key, value):
        ret = Dictionary1()
        ret.__listOfPairs = self.__listOfPairs[::]
        ret.put(key, value) # I am lazy.
        return ret


    def lookup(self, key):                                    
        def bs(alist, key, low, high):
            mid = (low + high) /2
            if low ==high:
                if alist[low][0] == key:
                    return alist[low][1]
                else: return "No entry"
            elif alist[mid][0]==key: return bs(alist, key, mid, mid)
            elif alist[mid][0] > key: return bs(alist, key, low, mid-1)
            else: return bs(alist, key, mid+1, high)
                
        return bs(self.__listOfPairs, key,  0, len(self.__listOfPairs)-1)
        
        
    def put(self, key, value):

        def Bisec_insert(alist, low, high, key, value):
            mid = (low + high)/2 
            if high == -1: 
                alist.append([key, value])
            elif low == high:
                if alist[low][0] == key:
                    alist[low][1] = value
                elif alist[low][0] > key:
                    alist.insert(low, [key, value]) 
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
        return self
                
    def __eq__(self,otherd):               
        if len(self.__listOfPairs) != len(otherd.__listOfPairs): return False
        for i in range(len(self.__listOfPairs)):
            if self.__listOfPairs[i] != otherd.__listOfPairs[i]:
                return False
        return True
  

    def merge(self, otherDictionary):                              
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
        return ret

  
    def __repr__(self): return str(self.__listOfPairs)
        
        
        
        
    def __rep_inv__(self):
        for i in range(len(self.__listOfPairs)-1): 
            if self.__listOfPairs[i][0] > self.__listOfPairs[i+1][0]: raise AssertionError("The sorted list rep inv has failed.")
           



from BinaryTree import *
from copy import deepcopy
class Dictionary2:

    def __init__(self):
        self.tree = BinaryTree(None) 

    def withEntry(self, key, value):
        ret = deepcopy(self)
        assert(self.__rep_inv__() and ret.__rep_inv__())
        return ret.put(key, value) #a pure fuctional one is just a mutation of a copy


    def lookup(self, key):
        def treelook(tree, key):
            if tree.get_val() is None: 
                return "No entry"
            elif tree.get_val()[0] == key:
                return tree.get_val()[1]
            elif tree.get_val()[0] > key:
                if tree.get_left(): return treelook(tree.get_left(), key)
                else: return "No entry"
            else:
                if tree.get_right(): return treelook(tree.get_right(), key)
                else: return "No entry"
        return treelook(self.tree, key)


    def put(self, key, value): 
        def Bput(tree, key, val):
            if tree.get_val() is None or tree.get_val()[0] == key: 
                tree.value = [key, val]
            elif tree.get_val()[0] > key: 
                if tree.get_left(): Bput(tree.get_left(), key, val)
                else: tree.add_left([key, val])
            else: 
                if tree.get_right(): Bput(tree.get_right(), key, val)
                else: tree.add_right([key, val])
        Bput(self.tree, key, value) 
        return self
     
    def __eq__(self, other):
        if self.tree.get_val()== None or other.tree.get_val() == None: 
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
        return is_one_good( self, other) and is_one_good(other, self)
    
    def merge(self, otherDictionary):
        ret = deepcopy(otherDictionary)
        stack = [self.tree]
        while len(stack) > 0:
            first = stack.pop()
            val = first.get_val()[::]
            ret.put(val[0],val[1]) 
            if first.get_left():
                stack.append(first.get_left())
            if first.get_right():
                stack.append(first.get_right())
        return ret

    def __repr__(self):
        ret = []
        stack = [self.tree]
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
            left, right = True, True 
            if tree.get_left():
                if tree.get_val()[0] <= tree.get_left().get_val()[0]: return False
            else: left = False 
            if tree.get_right():
                if tree.get_val()[0] > tree.get_right().get_val()[0]: return False
            else: right = False
            if left:
                left = rep(tree.get_left())
            else: left = True
            if right:
                right = rep(tree.get_right())
            else: right = True           
            return left and right 
        return rep(self.tree)
            
            
                
                
                




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



