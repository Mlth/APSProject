#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution sol.py

compile generate_explicit.py
compile generate_random.py
compile generate_full_update.py

# Generate answers to sample cases
sample 1
sample 2

# Sample tests for general- and edge-cases.
# Of the form "*description*_*numberOfSample*"
tc minEntireRange_1 generate_explicit 10 1 123 min 1 10
tc minRangeSubsequence_2 generate_explicit 6 2 250 min 1 3 min 3 6
tc oneElementArray_3 generate_explicit 1 1 400 min 1 1
tc lastElementUpdate_4 generate_explicit 10 5 6 min 1 10 update 10 0 min 1 10 update 10 10000 min 1 10
tc allEqualElementsAfterUpdates_5 generate_explicit 4 7 100 update 1 200 update 2 200 update 3 200 update 4 200 min 1 2 min 1 3 min 3 4
tc negativeValues_6 generate_explicit 4 5 500 min 1 3 update 1 -5000 min 1 3 update 3 -8000 min 1 4
tc multipleUpdatesOnSameElement_7 generate_explicit 6 5 900 update 3 45 min 1 4 update 3 800 update 3 750 min 1 4
tc updateWithInitialValue_8 generate_explicit 4 3 350 min 1 4 update 2 350 min 1 4
tc updateAllValues_9 generate_explicit 5 7 30 update 1 1 update 2 -2 min 1 5 update 3 40 update 4 -60 update 5 7 min 2 3
tc allNegativeValues_10 generate_explicit 5 3 -100 min 1 5 update 5 -300 min 1 5

# Randomly generated tests
tc random1 generate_random 200 100 0 false 0 50

# Group 3
tc randomMax generate_random 100000 1000000 0 false 0 500000

# Manual test cases
tc fullUpdate generate_full_update