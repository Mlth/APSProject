from ..data_structures import SegmentTree

N, O, S = map(int, input().split())

tree = SegmentTree(N, S)

for i in range(O):
    operation = input().split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    if(operationType == "update"):
        tree.update(fst, snd)
    elif(operationType == "min"):
        print(tree.min(fst, snd))