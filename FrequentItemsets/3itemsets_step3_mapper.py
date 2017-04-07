#!/usr/bin/env python

import itertools
import sys

candidateList=[]
def read_candidates():
    global candidateList
    
    f= open('./candidates')
    
    lines=f.readlines()
    for i in range(0,len(lines)):
        
        candidate=map(int,lines[i].strip().split('\t'))
        candidateList.append(candidate)
read_candidates()    
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    items = line.split()

    itemset=list(itertools.combinations(items,3))
    
      
    for i in range(0,len(itemset)):
            temp=list(map(int,itemset[i]))
            
            if(temp in candidateList):
                print('%s\t%s\t%s\t%s'%(temp[0],temp[1],temp[2],1))
    
    