class ArrayListWithUndo(ArrayList):
    def __init__(self):
        super().__init__()
        self.undos = Stack()

    def set(self, i, v):
        self.undos.push(("set", i, self.inArray[i]))
        self.inArray[i] = v

    def append(self, v):
        self.undos.push(("rem", self.count, None))
        self.inArray[self.count] = v
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp()  # resize array if reached capacity

    def insert(self, i, v):
        self.undos.push(("rem", i, None))
        for j in range(self.count, i, -1):
            self.inArray[j] = self.inArray[j - 1]
        self.inArray[i] = v
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp()  # resize array if reached capacity

    def remove(self, i):
        self.undos.push(("ins", i, self.inArray[i]))
        self.count -= 1
        val = self.inArray[i]
        for j in range(i, self.count):
            self.inArray[j] = self.inArray[j + 1]
        return val

    def undo(self):
        if self.undos.size != 0:
            v = self.undos.pop()
            if v[0] == "set":
                self.inArray[v[1]] = v[2]
            elif v[0] == "rem":
                self.count -= 1
                for j in range(v[1], self.count):
                    self.inArray[j] = self.inArray[j + 1]
            elif v[0] == "ins":
                for j in range(self.count, v[1], -1):
                    self.inArray[j] = self.inArray[j - 1]
                self.inArray[i] = v[2]
                self.count += 1

    def __str__(self):
        return str(self.toArray()) + "\n-> " + str(self.undos)
