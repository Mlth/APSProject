#! /usr/bin/env python3

import sys
import re

line = sys.stdin.readline()
assert re.match(r"((?:-?\d+ ?){3})", line), line

N, O, S = map(int, line.split())
assert 1 <= N <= 100000
assert 1 <= O <= 125000
assert -10000 <= S <= 10000

for i in range(O):
    operationLine = input()
    assert re.match(r"(?:quake|expedition)? -?\d{0,6} -?\d{0,6}$", operationLine), operationLine
    operation = operationLine.split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    assert operationType == "quake" or "expedition"
    if(operationType == "expedition"):
        assert 0 < fst <= snd <= N
    else:
        assert 0 < fst <= N
        assert -10000 <= snd <= 10000

assert sys.stdin.readline() == ""
sys.exit(42)