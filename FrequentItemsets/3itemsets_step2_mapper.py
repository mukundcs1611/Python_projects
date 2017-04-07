#!/usr/bin/env python



import sys


# input comes from STDIN (standard input)


val0=0
val1=0
val2=0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    num=line.split('\t')
    issubfrequent=False
    
    if(len(num)==2):
        val0=num[0]
        val1=num[1]
        
    else :
        val0=num[0]
        val1=num[1]
        val2=num[2]
            
    
    print('%s\t%s\t%s'%(val0,val1,val2))