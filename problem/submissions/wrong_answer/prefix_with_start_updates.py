import math
from collections import defaultdict

N, O = map(int, input().split())

array = []
array.extend(map(int, input().split()))

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
                calculations[(a, a+i)] = min((array[gi] for gi in range(a, a+i)), default=array[a])
        minMode = True
        
    if(operationType == "min"):
        largestPowerOfTwo = 2**((snd - fst + 1).bit_length() - 1)
        minValue = min(calculations[fst - 1, fst + largestPowerOfTwo - 1 - 1], calculations[snd - 1 - largestPowerOfTwo + 1, snd - 1])
        print(minValue)