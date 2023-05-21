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
# Of the form "*description*_*numberOfSample*".
tc minEntireRange_1 generate_explicit 10 1 123 expedition 1 10
tc minRangeSubsequence_2 generate_explicit 6 2 250 expedition 1 3 expedition 3 6
tc oneElementArray_3 generate_explicit 1 1 400 expedition 1 1
tc lastElementUpdate_4 generate_explicit 10 5 6 expedition 1 10 quake 10 0 expedition 1 10 quake 10 10000 expedition 1 10
tc allEqualElementsAfterUpdates_5 generate_explicit 4 7 100 quake 1 200 quake 2 200 quake 3 200 quake 4 200 expedition 1 2 expedition 1 3 expedition 3 4
tc negativeValues_6 generate_explicit 4 5 500 expedition 1 3 quake 1 -5000 expedition 1 3 quake 3 -8000 expedition 1 4
tc multipleUpdatesOnSameElement_7 generate_explicit 6 5 900 quake 3 45 expedition 1 4 quake 3 800 quake 3 750 expedition 1 4
tc updateWithInitialValue_8 generate_explicit 4 3 350 expedition 1 4 quake 2 350 expedition 1 4
tc updateAllValues_9 generate_explicit 5 7 30 quake 1 1 quake 2 -2 expedition 1 5 quake 3 40 quake 4 -60 quake 5 7 expedition 2 3
tc allNegativeValues_10 generate_explicit 5 3 -100 expedition 1 5 quake 5 -300 expedition 1 5

# Group 1
tc random1RandomRanges generate_random 1000 1000 0 False 500 False False False
tc random1ShortRanges generate_random 1000 1000 0 False 500 False True False
tc random1OnlyPositiveShortRanges generate_random 1000 1000 10000 False 500 False True True

# Group 2
tc random2LongRanges generate_random 20000 125000 0 True 5000 True False False
tc random2ShortRanges generate_random 20000 125000 0 True 5000 False True False
tc random2OnlyPositiveShortRanges generate_random 20000 125000 10000 True 5000 False True True

# Group 3
tc random3RandomRanges generate_random 100000 125000 0 False 20000 False False False
tc random3ShortRanges generate_random 100000 125000 0 False 20000 False True False
tc random3OnlyPositiveShortRanges generate_random 100000 125000 10000 False 20000 False True True

# Manual test cases
tc fullUpdate generate_full_update