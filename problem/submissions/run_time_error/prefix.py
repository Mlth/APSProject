import math
from collections import defaultdict

N, O = map(int, input().split())

array = []
array.extend(map(int, input().split()))

calculations = defaultdict(int)
powerOfTwos = [0]

minMode = False
for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "update"):
        array[fst-1] = snd
    elif(operationType == "min" and not minMode):
        for i in range(1, N+1):
            log2Calc = math.log2(i)
            if(math.ceil(log2Calc) == math.floor(log2Calc)):
                powerOfTwos.append(i)

        for i in powerOfTwos:
            for a in range(N - i):
                calculations[(a, a+i)] = min(array[a], array[a+i])
        minMode = True
    elif(operationType == "min"):
        break