#!/usr/bin/env python

import itertools
import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    items = line.split()

    itemset=list(itertools.combinations(items,2))
    
    for i in range(0,len(itemset)):
        i = list(map(int, itemset[i]))
        print('%s\t%s' % (i, 1))
        
    # increase counters
#     for i in itemset:
#         # write the results to STDOUT (standard output);
#         # what we output here will be the input for the
#         # Reduce step, i.e. the input for reducer.py
#         #
#         # tab-delimited; the trivial word count is 1
#         print('%s\t%s' % (itemset, 1))
