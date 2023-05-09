#! /usr/bin/env python3

import sys
import re

line = sys.stdin.readline()
assert re.match(r"((?:\d+ ?){3})", line), line

N, O, S = map(int, line.split())
assert -100000 <= N <= 100000
assert -10000000 <= O <= 10000000
assert -10000 < S < 10000

for i in range(O):
    operationLine = input()
    assert re.match(r"(?:update|min)? -?\d{0,6} -?\d{0,6}$", operationLine), operationLine
    operation = operationLine.split()
    operationType = operation[0]
    fst, snd = map(int, [operation[1], operation[2]])
    assert operationType == "update" or "min"
    if(operationType == "min"):
        assert 0 < fst <= snd <= N
    else:
        assert 0 < fst <= N
        assert -10000 <= snd <= 10000

assert sys.stdin.readline() == ""
sys.exit(42)