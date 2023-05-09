#! /usr/env/python3
import math
from collections import defaultdict

'''
    This implementation works for input where all updates come before any min-query. Therefore, it should pass the first and second test groups but not the third one, since it does not update values after receiving the first min-query.
'''

N, O, S = map(int, input().split())

array = [S]*N

calculations = defaultdict(int)
powerOfTwos = []
for i in range(1, N+1):
    log2Calc = math.log2(i)
    if(math.ceil(log2Calc) == math.floor(log2Calc)):
        powerOfTwos.append(i - 1)

minMode = False
for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "update"):
        array[fst-1] = snd

    elif(operationType == "min" and not minMode):
        for i in powerOfTwos:
            for a in range(N - i):
                calculations[(a, a+i)] = min((array[gi] for gi in range(a, a+i+1)), default=array[a])
        minMode = True
        
    if(operationType == "min"):
        largestPowerOfTwo = 2**((snd - fst + 1).bit_length() - 1)
        minValue = min(calculations[fst - 1, fst + largestPowerOfTwo - 1 - 1], calculations[snd - 1 - largestPowerOfTwo + 1, snd - 1])
        print(minValue)