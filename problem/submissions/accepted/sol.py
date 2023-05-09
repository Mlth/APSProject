#! /usr/env/python3
import math

class SegmentTree:
    def __init__(self, N, S):
        self.N = N
        self.tree = [S]*self.N*2
    
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

N, O, S = map(int, input().split())

tree = SegmentTree(N, S)

for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "update"):
        tree.update(fst, snd)
    elif(operationType == "min"):
        print(tree.min(fst, snd))