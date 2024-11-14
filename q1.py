# ArrayList and Stack code to use

class Stack():
    def __init__(self):
        self.inList = None
        self.size = 0
        
    def push(self, v):
        self.size += 1
        self.inList = (v,self.inList)
        
    def pop(self):
        if self.size == 0: assert(0)
        self.size -= 1
        (v,ls) = self.inList
        self.inList = ls
        return v
    
    def __str__(self):
        s = "["
        ls = self.inList
        for _ in range(self.size):
            (v,ls) = ls
            s += str(v)
            if ls!=None: s += ", "
        return s+"]"
        
class ArrayList:
    def __init__(self):
        self.inArray = [0 for i in range(10)]
        self.count = 0
        
    def get(self, i):
        return self.inArray[i]

    def set(self, i, e):
        self.inArray[i] = e

    def length(self):
        return self.count

    def append(self, e):
        self.inArray[self.count] = e
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp()

    def insert(self, i, e):
        for j in range(self.count,i,-1):
            self.inArray[j] = self.inArray[j-1]
        self.inArray[i] = e
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp()
    
    def remove(self, i):
        self.count -= 1
        val = self.inArray[i]
        for j in range(i,self.count):
            self.inArray[j] = self.inArray[j+1]
        return val

    def _resizeUp(self):
        newArray = [0 for i in range(2*len(self.inArray))]
        for j in range(len(self.inArray)):
            newArray[j] = self.inArray[j]
        self.inArray = newArray
        
    def toArray(self):
        return self.inArray[:self.count]

    def __str__(self):
        if self.count == 0: return "[]"
        s = "["
        for i in range(self.count-1): s += str(self.inArray[i])+", "
        return s+str(self.inArray[self.count-1])+"]" 

## QUESTION 1 IMPLEMENTATION

class ArrayListWithUndo(ArrayList):
    def __init__(self):
        super().__init__()
        self.undos = Stack()
        
    def set(self, i, v):
        self.undos.push(("set",i,self.inArray[i]))
        self.inArray[i] = v

    def append(self, v):
        self.undos.push(("rem",self.count,None))
        self.inArray[self.count] = v
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp() # resize array if reached capacity
        
    def insert(self, i, v):
        self.undos.push(("rem",i,None))
        for j in range(self.count,i,-1):
            self.inArray[j] = self.inArray[j-1]
        self.inArray[i] = v
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp() # resize array if reached capacity
    
    def remove(self, i):
        self.undos.push(("ins",i,self.inArray[i]))
        self.count -= 1
        val = self.inArray[i]
        for j in range(i,self.count):
            self.inArray[j] = self.inArray[j+1]
        return val
    
    def undo(self):
        if self.undos.size != 0:
            v = self.undos.pop()
            if v[0] == "set":
                self.inArray[i] = v[2]
            elif v[0] == "rem":
                self.count -= 1
                for j in range(v[1],self.count):
                    self.inArray[j] = self.inArray[j+1]
            elif v[0] == "ins":
                for j in range(self.count,v[1],-1):
                    self.inArray[j] = self.inArray[j-1]
                self.inArray[i] = v[2]
                self.count += 1
            
    def __str__(self):
        return str(self.toArray())+"\n-> "+str(self.undos)
