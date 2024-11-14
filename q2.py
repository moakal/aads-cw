class NetworkWithUndo:
    def __init__(self, N):
        # already implemented
        self.inArray = ArrayListWithUndo()
        for _ in range(N):
            self.inArray.append(-1)
        self.undos = Stack()
        self.undos.push(N)

    def getSize(self):
        # already implemented
        return self.inArray.length()

    # Add a new node to the network
    def add(self):
        ops = 0
        self.inArray.append(-1)
        ops += 1
        # Record the number of operations for undo
        self.undos.push(ops)

    # Find the root of the cluster containing node i
    def root(self, i):
        ops = 0
        path = Stack()
        current = i

        # Follow parent links to find the root
        while self.inArray.get(current) >= 0:
            path.push(current)
            current = self.inArray.get(current)
        root_node = current

        # Path compression for all visited nodes
        while path.size > 0:
            node = path.pop()
            if self.inArray.get(node) != root_node:
                self.inArray.set(node, root_node)
                ops += 1

        # Record operations for undo
        self.undos.push(ops)
        return root_node

    # Merge clusters containing nodes `i` and `j`
    def merge(self, i, j):
        # Both nodes must be roots
        if self.inArray.get(i) >= 0 or self.inArray.get(j) >= 0:
            assert 0

        # If nodes are the same, nothing to merge
        if i == j:
            return

        ops = 0
        size_i = -self.inArray.get(i)
        size_j = -self.inArray.get(j)

        # Merge smaller cluster into larger one
        if size_i <= size_j:
            self.inArray.set(i, j)
            ops += 1
            self.inArray.set(j, -(size_i + size_j))
            ops += 1
        else:
            self.inArray.set(j, i)
            ops += 1
            self.inArray.set(i, -(size_i + size_j))
            ops += 1

        # Record operations for undo
        self.undos.push(ops)

    # Undoes last operation
    def undo(self):
        if self.undos.size > 0:
            num_ops = self.undos.pop()
            for _ in range(num_ops):
                self.inArray.undo()

    def toArray(self):
        # already implemented
        return self.inArray.toArray()

    def __str__(self):
        # already implemented
        return str(self.toArray()) + "\n-> " + str(self.undos)
