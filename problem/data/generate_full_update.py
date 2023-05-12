#! /usr/env/python3

#This manual testcase updates all values in the array before asking for any queries.
#This ensures that the user cannot pick the initial value of the array and get lucky.

import random

N = 100000
O = 150000
S = 100

print(N, O, S)

#Update all values
for i in range(1, 100001):
    print("update", i, random.choice([random.randint(-10000, -1), random.randint(1, 10000)]))

#Quick check for the entire range
print("min", 1, 100000)
#Random checks
for i in range(100002, O+1):
    points = sorted([random.randint(1, 100000), random.randint(1, 100000)])
    print("min", points[0], points[1])