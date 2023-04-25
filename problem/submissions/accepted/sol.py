from segmentTree import SegmentTree

N, O = map(int, input().split())

array = []
array.extend(input().split())

tree = SegmentTree(array, N)

for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "update"):
        tree.update(fst, snd)
    elif(operationType == "min"):
        print(tree.min(fst, snd))