class ArrayList:
    def __init__(self):
        self.inArray = [0 for i in range(10)] # capacity set to 10 for start
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
            self._resizeUp() # resize array if reached capacity
    def insert(self, i, e):
        for j in range(self.count,i,-1):
            self.inArray[j] = self.inArray[j-1]
        self.inArray[i] = e
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp() # resize array if reached capacity
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
    def appendAll(self, A):
        for i in range(len(A)):
            self.append(A[i])
    def toArray(self):
        newArray = [0 for i in range(self.count)]
        for i in range(self.count):
            newArray[i] = self.inArray[i]
        return newArray
        
class Stack:
    def __init__(self):
        self.inList = ArrayList()
    def __str__(self):
        return(str(self.inList.toArray()))
    def size(self):
        return self.inList.length()
    def push(self, e):
        self.inList.insert(0,e)
    def pop(self):
        return self.inList.remove(0)

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
        if self.undos.size() != 0:
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
