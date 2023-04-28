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
        start += self.N -1
        end += self.N -1
        min = math.inf
        while (start <= end):
            if (start%2 == 1):
                if(self.tree[start] < min):
                    min = self.tree[start]
                start += 1
            if (end%2 == 0):
                if(self.tree[end] < min):
                    min = self.tree[end]
                end -= 1
            start = math.floor(start/2)
            end = math.floor(end/2)
        return min

    def update(self, index, value):
        index += self.N -1
        self.tree[index] = value
        index = math.floor(index/2)
        while(index >= 1):
            self.tree[index] = min(self.tree[2*index], self.tree[2*index+1])
            index = math.floor(index/2)