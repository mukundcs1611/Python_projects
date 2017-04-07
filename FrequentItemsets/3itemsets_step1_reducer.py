#!/usr/bin/env python

import itertools
import sys


current_key = None
valuelist = []
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key,value = line.split('\t', 1)
    # convert count (currently a string) to int
    if current_key==key:
        valuelist.append(value)
   
    elif current_key is None:
        current_key=key
        valuelist.append(value)
    
    else :
        
        temp=list(itertools.combinations(valuelist,2))             
        for i in range(0,len(temp)):
                t=list(map(int,temp[i]))
                print('%s\t%s\t%s'%(t[0],t[1],current_key))
                
        current_key=key
        valuelist=[] 
        valuelist.append(value)   
if current_key==key:
                #Extract Digits
        temp=list(itertools.combinations(valuelist,2))
             
             
        for i in range(0,len(temp)):
                t=list(map(int,temp[i]))
                print('%s\t%s\t%s'%(t[0],t[1],current_key))        

