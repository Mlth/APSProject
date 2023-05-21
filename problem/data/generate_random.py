#! /usr/env/python3

import sys
import random

N, O, S = map(int, sys.argv[1:4])

onlyUpdatesFirst = str(sys.argv[4])
numberOfUpdates = int(sys.argv[5])
longRanges = str(sys.argv[6])
shortRanges = str(sys.argv[7])
onlyPositive = str(sys.argv[8])

print(N, O, S)

array = []

for i in range(O):
    if onlyUpdatesFirst == "True" and i < numberOfUpdates:
        index = str(random.randint(1, N))
        value = str(random.randint(-10000, 10000))
        if(onlyPositive == "True"):
            value = str(random.randint(0, 10000))
        array.append("quake" + " " + index + " " + value)
    else:
        if i < numberOfUpdates:
            index = str(random.randint(1, N))
            value = str(random.randint(-10000, 10000))
            if(onlyPositive == "True"):
                value = str(random.randint(0, 10000))
            array.append("quake" + " " + index + " " + value)
        else:
            if(longRanges == "True"):
                values = [random.randint(1, N/20), random.randint(N-(N/20), N)]
                array.append("expedition" + " " + str(values[0]) + " " + str(values[1]))
            elif (shortRanges == "True"):
                start = random.randint(1, N-50)
                end = start + 30
                array.append("expedition" + " " + str(start) + " " + str(end))
            else:
                values = sorted([random.randint(1, N), random.randint(1, N)])
                array.append("expedition" + " " + str(values[0]) + " " + str(values[1]))

if(onlyUpdatesFirst != "True"):
    random.shuffle(array)

for string in array: 
    print(string)