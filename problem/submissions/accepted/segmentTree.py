import math

class SegmentTree:
    def __init__(self, array, N):
        self.N = N
        self.tree = self.makeTree(array)

    def makeTree(self, array):
        tree = ([0]*self.N)
        tree.extend(array)
        for i in range(len(tree)-1, 1, -2):
            tree[math.floor(i/2)] = min(tree[i], tree[i-1])
        return tree
    
    def min(self, start, end):
        self.calcMin(1, self.N, len(self.tree), start, end)
    
    def calcMin(self, nodeIndex, nodeStart, nodeEnd, rangeStart, rangeEnd):
        if (nodeStart >= rangeStart and nodeEnd <= rangeEnd):
            return self.tree[nodeIndex]
        return min(self.calcMin(nodeIndex*2, nodeStart, (nodeEnd - self.N)/2 + self.N, rangeStart, rangeEnd), self.calcMin(nodeIndex*2+1, (nodeEnd - nodeStart)/2 + nodeStart), nodeEnd, rangeStart, rangeEnd)

    def update(self, index, value):
        index += self.N
        self.tree[index] = value
        index = math.floor(index/2)
        while(index >= 1):
            self.tree[index] = min(self.tree[2*index], self.tree[2*index+1])
            index = math.floor(index/2)