#! /usr/env/python3

import sys

N, O, S = map(int, sys.argv[1:3])

operations = []
for i in range(3+1, (3+1+(O*3)), 3):
    operations.append(sys.argv[i], sys.argv[i+1], sys.argv[i+2])

print (N, O, S)
for i in (len(operations)):
    print(operations[i])