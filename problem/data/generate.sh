#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution sol.py

compile generate_explicit.py

# Generate answers to sample cases
sample 1
sample 2

tc  edge1 generate_explicit 10 5 6 min 1 10 update 10 0 min 1 10 update 10 10000 min 1 10