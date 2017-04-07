#!/usr/bin/env python

import re
import sys


current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word,count = line.split('\t', 1)
    
    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            if current_count>=1000:
                #Extract Digits
                temp=re.findall(r'\d+',current_word)
                temp = list(map(int, temp))  
                print('%s\t%s'%(temp[0],temp[1]))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_count>=1000:
    if current_word == word:
        #Extract Digits
        temp=re.findall(r'\d+',current_word)
        temp = list(map(int, temp))  
        print('%s\t%s'%(temp[0],temp[1]))