'''
Created on Oct 14, 2016

@author: chavali
'''

from collections import defaultdict
from math import log10

import operator

from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import math


class Doc(object):
    
    def __init__(self,noOfDocs):
        self.doc_freq={}
        
        self.noOfDocs=noOfDocs
        self.documents={} #list holding dictionary of {doc,corr. weights}
        self.queries=[] 
        self.pList={}
    def termFreq(self,str):
        word_weights={}
        for i in str:
            word_weights[i]=word_weights.get(i,0)+1.0
        
        for i in word_weights:
            word_weights[i]=(1+log10(word_weights[i]))
            word_weights[i]=word_weights[i]/len(str)
        return word_weights
#         self.queries.append([str,word_weights])#query itself and corr weights
        
    def termFreqIDF(self,doc):
#         L2 Norm

        l=0.0
       
        word_weights={}
        for i in self.noOfDocs[doc]:
#             self.words_in_doc[i]=i
            word_weights[i]=word_weights.get(i,0)+1.0
        
        #find tf, idf , multiply  both and normalize     
        for i in word_weights:
            
            word_weights[i]=(1+log10(word_weights[i]))*self.idf(i)
            
            
        for i in word_weights:
            l=l+word_weights[i]**2    
            
        length=math.sqrt(l)
        for i in word_weights:
            word_weights[i]=word_weights[i]/length
            
        self.documents[doc]=word_weights #list itself and corr weights
        
            
    
    def doc_freqofT(self,token):
        sum=0
        for doc in self.noOfDocs:
            if(token in self.noOfDocs[doc]):
                sum=sum+1
        return sum
    
    def idf(self,token):
            dFreq=self.doc_freqofT(token)
        
            return log10(len(self.noOfDocs)/dFreq)
        
            
    def create_postings_list(self):
        self.pList = defaultdict(list)
        for dd in (self.documents):
            for k,v in self.documents[dd].items():
                self.pList[k].append([dd,v])# bad code, appending doc id with the corr weight of that term
    def similar(self,weightsofQuery):
        
        topten={}
        temp={}
        score={}
        for t in weightsofQuery:
         topten[t]=self.pList.get(t,0)
         if topten[t]!=0: #if there is no match in the postings list ignore the calc of score
             
            for w in topten[t]:
                score[w[0]]=score.get(w[0],0)+w[1]*weightsofQuery[t]   
                    
    def printAll(self):
        print(self.documents["2012-10-22.txt"])
        
#         for i in self.pList:
#             print(self.pList[i])