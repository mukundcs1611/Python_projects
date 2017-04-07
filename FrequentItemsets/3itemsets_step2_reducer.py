#!/usr/bin/env python


import sys


current_key = None
current_key1=None
valuelist = []
word = None

# input comes from STDIN
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()
# 
#     # parse the input we got from mapper.py
#     values = line.split('\t')
#     t=list(map(int,values))
#     if(values[2]!=0):
#         print('%s\t%s\t%s'%(t[2],t[0],t[1]))        

for line in sys.stdin:
    line = line.strip()
    key,key1,val = line.split("\t")
    # convert count (currently a string) to int
    
    try:
        val = int(val)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    
    if(val==0):
        current_key=key
        current_key1=key1
    if(val!=0 and (key==current_key and key1==current_key1)):
        print('%s\t%s\t%s'%(val,key,key1))    