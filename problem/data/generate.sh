#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution sol.py

compile generate_explicit.py
compile generate_random.py

# Generate answers to sample cases
sample 1
sample 2

# sample
tc sample5 generate_explicit 10 5 6 min 1 10 update 10 0 min 1 10 update 10 10000 min 1 10

# random
tc random1 generate_random 200 100 0 false 0 50

# Group 3
tc randomMax generate_random 100000 1000000 0 false 0 500000