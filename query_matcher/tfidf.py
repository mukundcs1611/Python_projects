'''
Created on Oct 12, 2016

@author: chavali
'''
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict, Counter
import math
import operator

class Doc(object):
    
    def __init__(self,noOfDocs):
        self.doc_freq={}
        
        self.noOfDocs=noOfDocs
        self.documents={} #list holding dictionary of {doc:corr. weights}
        self.pList={}#postings list {token : weights in decreasing order}
        self.idf={}
        self.postListFirstRun=True
# termFreq for queries     
    def termFreq(self,strng):
        word_weights=Counter(strng)
        l=0.0
        
        
        for i in word_weights:
            word_weights[i]=(1+math.log10(word_weights[i]))
            l=l+word_weights[i]**2    
            
        length=math.sqrt(l)
        for i in word_weights:
            word_weights[i]=word_weights[i]/length

        return word_weights

#   tfidf for documents      
    def termFreqIDF(self,doc):

        l=0.0
       
        if(doc not in self.documents):
            
            word_weights=Counter(self.noOfDocs[doc])
    
            #find tf, idf , multiply  both and normalize     
            for i in word_weights:
                
                word_weights[i]=(1+math.log10(word_weights[i]))*self.idfM(i)
                l=l+word_weights[i]**2
                
            length=math.sqrt(l)
            for i in word_weights:
                word_weights[i]=word_weights[i]/length
                
            self.documents[doc]=word_weights #list itself and corr weights
            
            
    def getweight(self,filename,token):
        if(filename not in self.documents):
            self.termFreqIDF(filename)
            
        return self.documents[filename][token]
            
    def doc_freqofT(self,token):
        dfreq=0.0
        if(self.doc_freq.get(token) is None):
        
            for doc in self.noOfDocs:
                if(token in self.noOfDocs[doc]):
                    dfreq=dfreq+1
        
        self.doc_freq[token]=dfreq
        
                        
        return self.doc_freq.get(token)
    
    
    def idfM(self,token):
        
        if(self.idf.get(token) is None):
            
            dFreq=self.doc_freqofT(token)
            self.idf[token]=math.log10(len(self.noOfDocs)/dFreq)
        
        return self.idf.get(token)
            
    
    def create_postings_list(self):
    
            
            if(len(self.pList)==0):
                self.pList = defaultdict(list)
                       
            for dd in (self.documents):
                
                for k,v in self.documents[dd].items():
                    if(len(self.pList[k])>=10):
                        continue
                    self.pList[k].append([dd,v])
            self.postListFirstRun=False            
#    This method calculates cosine similarity of a query and a document , returns most similar document or an appropriate messsage  
    def similar(self,weightsofQuery):
        
#         Finding tf-idf for necessary documents
        for i in weightsofQuery:
            
            for j in filtered_words:
                if i in filtered_words[j]:
                    self.termFreqIDF(j)

# Generate postings list for the processed documents 

        self.create_postings_list()    
        
        topten={}
        Actualscore={}
        upperboundScore={}
        
        for t in weightsofQuery:

            
            if t in self.pList:
                topten[t]=self.pList[t]
            else:
                continue    
           
            documents=[sub_list[0] for sub_list in  topten[t]]
            
            for d in self.documents:
                if d in documents:
                        i=documents.index(d)           
                        Actualscore[d]=Actualscore.get(d,0)+topten[t][i][1]*weightsofQuery[t]
                else:    
                        upperboundScore[d]=upperboundScore.get(d,0)+topten[t][9][1]*weightsofQuery[t]    

        if(len(Actualscore)!=0):
            top=max(Actualscore.items(),key=operator.itemgetter(1))
        
            if(len(upperboundScore)!=0): 
                
                topUB=max(upperboundScore.items(),key=operator.itemgetter(1))
        
                if(top[1]>topUB[1]):
                    return top
                else:
                    return {"Fetch More",0.000000}
            else:
                return top    
            
        elif(len(Actualscore)==0 and len(upperboundScore)==0):
            return {"NONE",0.000000}               
              
    def checkTFIDF(self):
        print(self.documents["2012-10-22.txt"])
        
if __name__ == "__main__":
   

    corpusroot = './presidential_debates'
    check=stopwords.words('english')
    filtered_words={}
    tokenizer = RegexpTokenizer(r'[a-z]+')
    stemmer = PorterStemmer()    

    def textTrimmer(doc):
        
        tokens = tokenizer.tokenize(doc)
        
        tokens=[stemmer.stem(word) for word in tokens if word not in check]
        return tokens
    
    for filename in os.listdir(corpusroot):
        file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
        doc=file.read()
        file.close() 
        doc = doc.lower()
        filtered_words[filename]=textTrimmer(doc)
    
    tf= Doc(filtered_words)
    
    #method 1
    def query(qstring):
        qstring.lower()
        queryWeights=tf.termFreq(textTrimmer(qstring))
        
        return tf.similar(queryWeights)
    #method 2    
    def getidf(token):
        return tf.idfM(token)
    #method 3
    def getweight(filename,token):
        if(filename in os.listdir(corpusroot) ):
            return tf.getweight(filename, token)
        else:
            return "0.0000"
    
    
#     print("(%s, %.12f)" % query("health insurance wall street"))
    print("(%s, %.12f)" % query("terror attack"))
    print("(%s, %.12f)" % query("particular constitutional amendment"))
    
#     print( query("vector entropy"))
#     print("%.12f" % getweight("2012-10-03.txt","health"))
#     print("%.12f" % getidf("health"))
#     
        
        
    
