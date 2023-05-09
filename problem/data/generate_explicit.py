#! /usr/env/python3

import sys

N, O, S = map(int, sys.argv[1:4])

operations = []
for i in range(4, (4+1+(O*3))-1, 3):
    operations.append([sys.argv[i], sys.argv[i+1], sys.argv[i+2]])

print (N, O, S)
for i in range(len(operations)):
    operationType = operations[i][0]
    fst = operations[i][1]
    snd = operations[i][2]
    print(operationType, fst, snd)