#the first class is copied from the miller and ranum text

#Miller, Brad, and David Ranum. "Queues." Problem Solving with 
#Algorithms and Data Structures. N.p., n.d. Web. 09 Nov. 2015.


class Queue:
    #constructor
    def __init__(self):
        self.items = []
    #accessors (empty and size)
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    #mutators:
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()


class Pure_queue:
    #same constructor
    def __init__(self):
        self.items = []
    #acessors stay the same:
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
        
    #we modify the mutators to do something else
    #without changing the objects the func was called with
    def enqueue(self, item):
        nq = Pure_queue()
        nq.items = [item] + self.items
        return nq
    def dequeue(self):
#        nq = Pure_queue()                 <<These were wrong, put this in a seperate one func called removeItem(self):
#        nq.items = self.items[1:]
        return self.items[-1]

"""
The fundamental abstract constuctors are init and enqueue
###################YES: this is what you need to create ALL possible queues  
######what you need for all possible queues are the fundamental abstract constuctors



pre/post for dequeue (broken into 'head' and 'withouthead') , size and is_empty

there is basically no precondition for size or is_empty. The postcondition
of the former is to return the number of elements in a stack
and of the latter to say true if there are zero elements
and false otherwise.

        >>>>>Explicity<<<<<

is_empty:
Postcondition(Queue().is_empty()==True)

size:
#note with both of these, the answer is clear
#for any possible queue

Postcondition(Q.enqueue(x).size() == Q.size() + 1 AND Queue().size() == 0)


head: (or in our words, the first part of dequeue ) two answers a), b)
precondition is Queue is not empty
    a)
    Q.withitem(x).head() === x if Q.size() ==0 else Q.withitem(y).head()
    
    b)
    
    Queue().withItem(x) === x AND
    Q.withitem(y).withitem(x).head() === Q.withitem(y).head()

#These are things relative to the constructors (both of them)

withoutHead: (precond is Queue is not empty)

Postcondition(  Queue().withitem(x).withouthead() === Queue()  \
AND  Q.withitem(y).withitem(x).withouthead() === Q.withitem(y).withoutHead().withitem(x) )

#notice, for each postcondition, we use 
#the first as the base case and the second as the recursive case









##########NOTES::::
 

we do postconditions not related to the
implementations of the function
so, just use name of methods in postconditions
and not internals or postconditions


We use postconditions based on ALL our abstract constructors

these are our axioms (how methods behave for ALL possilble data strutures of that type)

#
#



"""
        
        
        
        
        
        
        
        
        