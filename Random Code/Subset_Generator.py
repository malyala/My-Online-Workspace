def lstr(l):
    ret =""
    for i in l:
        ret += i
    return ret

class Loop():
    def __init__(self):
        self.l=[]
    def push(self,item):
        self.l.append(item)
    def pop(self,item):
        assert(len(self)>0)
        return self.pop(0)
    def __len__(self):
        return len(self.l)
    def __getitem__(self,key):
        return self.l[key%len(self)]
    def __getslice__(self,i,j):
        assert(type(i)==int and type(j)==int and j>=i)
        if j<len(self)+1:
            return lstr(self.l[i:j])
        else:
            return lstr(self.l[i::]+self.l[0:j%len(self)])


def subsets(S):
    """
    returns all subsets ofstringS (something like"ABC")
    as a list ["A","B","C","AB",...]
    """
#1:makeaQueue
    Q= Loop()
    for letter in S:Q.push(letter)
    yield ""
    
#use it
    for i in range(len(Q)):
        if i==0: continue
        for j in range(len(Q)):
            yield Q[j:j+i]
    
    if S!= "": yield S
            
def print_g(g):
    for i in g:
        print i

