#!/usr/bin/env python

import re
import sys


current_key= None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key0,key1,key2,count = line.split('\t')
    
    
    # convert count (currently a string) to int
    try:
        key0=int(key0)
        key1=int(key1)
        key2=int(key2)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if (current_key == [key0,key1,key2]):
        current_count += count
        
    else:
        if current_key:
            # write result to STDOUT
            
                #Extract Digits
                
                if(current_count>=1000):  
                    print('%s'%(current_key))
                
        current_count = count
        current_key = [key0,key1,key2]
    
# do not forget to output the last word if needed!

if (current_key == [key0,key1,key2]):
        if(current_count>=1000):
            print('%s'%(current_key))