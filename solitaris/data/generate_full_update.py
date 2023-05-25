#! /usr/env/python3

#This manual testcase updates all values in the array before asking for any queries.
#This ensures that the user cannot pick the initial value of the array and get lucky.

import random

N = 20000
O = 75000
S = 100

print(N, O, S)

#Update all values
for i in range(1, N+1):
    print("quake", i, random.choice([random.randint(-10000, -1), random.randint(1, 10000)]))

#Quick check for the entire range
print("expedition", 1, N)
#Random checks
for i in range(N+1, O):
    start = random.randint(1, N-20)
    end = start + 20
    print("expedition", start, end)