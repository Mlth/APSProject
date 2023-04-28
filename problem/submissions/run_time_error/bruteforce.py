import math

N, O = map(int, input().split())

array = []
array.extend(map(int, input().split()))

for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "update"):
        array[fst-1] = snd
    elif(operationType == "min"):
        currentMin = math.inf
        for i in range(fst-1, snd):
            if (array[i] < currentMin):
                currentMin = array[i]
        print(currentMin)