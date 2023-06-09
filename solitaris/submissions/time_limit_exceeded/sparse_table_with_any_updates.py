#! /usr/env/python3
import math
from collections import defaultdict

'''
    This implementation does the preprocessing everytime it receives an update. This means that it becomes very slow. It should be able to pass the first test-group since that group does not contain much input. It should also be able to pass the second because it only has updates in the beginning, but should get time-limit exceeded for the third test-group, since that test-group has mixed queries.
'''

N, O, S = map(int, input().split())

array = [S]*N

calculations = defaultdict(int)
def updateCalculations():
    for i in powerOfTwos:
        for a in range(N - i):
            min = array[a]
            for gi in range(a, a+i+1):
                val = array[gi]
                if val < min:
                    min = val
            calculations[(a, a+i)] = min

powerOfTwos = []
for i in range(1, N+1):
    log2Calc = math.log2(i)
    if(math.ceil(log2Calc) == math.floor(log2Calc)):
        powerOfTwos.append(i - 1)

updated = False    

for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "quake"):
        array[fst-1] = snd
        updated = False
    elif (operationType == "expedition"):
        if not updated:
            updateCalculations()
            updated = True
        largestPowerOfTwo = 2**((snd - fst + 1).bit_length() - 1)
        minValue = min(calculations[(fst - 1, fst + largestPowerOfTwo - 1 - 1)], calculations[(snd - 1 - largestPowerOfTwo + 1, snd - 1)])
        print(minValue)