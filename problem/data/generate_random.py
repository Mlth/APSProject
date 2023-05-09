#! /usr/env/python3

import sys
import random

N, O, S = map(int, sys.argv[1:4])

onlyUpdatesFirst = bool(sys.argv[4])
firstUpdates = int(sys.argv[5])
numberOfUpdates = int(sys.argv[6])

print(N, O, S)

array = []

for i in range(O):
    if onlyUpdatesFirst and i < firstUpdates:
        array.append("update" + " " + str(random.randint(1, N)) + " " + str(random.randint(-10000, 10000)))
    else:
        if i < numberOfUpdates:
            array.append("update" + " " + str(random.randint(1, N)) + " " + str(random.randint(-10000, 10000)))
        else: 
            values = sorted([random.randint(1, N), random.randint(1, N)])
            array.append("min" + " " + str(values[0]) + " " + str(values[1]))

random.shuffle(array)

for string in array: 
    print(string)