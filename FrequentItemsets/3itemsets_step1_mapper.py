#!/usr/bin/env python


import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    tokens=line.split()
    
    i = list(map(int, tokens))
    print('%s\t%s' % (i[0],i[1]))
        
