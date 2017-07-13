'''
Created on Jun 28, 2017

@author: chavali
'''
import mysql.connector
from mysql.connector.constants import ClientFlag
import redis 
import pickle
import time
from asyncio.locks import Lock
class DB:
    
    conn={}
    redisObj={}
    lock=Lock()    
    def connectToDB(self):     
        self.conn=mysql.connector.connect(host='localhost',password='',user='',database='mymav',client_flags=[ClientFlag.LOCAL_FILES])
        self.conn.autocommit=True
        self.redisObj=redis.Redis(
                        host='localhost',#redisautoscale.xle6db.0001.use1.cache.amazonaws.com
                        port=6379,password=''
                        )
                
    def getenrolledcourses(self,userid):    
        
        
        query=("select `courseid`,`section`,`instructor` from enrolledcourses where `userid`='"+str(userid)+"';")
        cursor=self.conn.cursor()
        cursor.execute(query)
     
        
            
        
        l=[]
        for i in cursor:
            l.append({'course':i[0],'section':i[1],'instructor':i[2]})
        
        return l
    
    def getcourse(self,course,instructor):
        stime=time.time()
        
        
        try:
            
        
            query=("select * from `mymav`.`classes` where `courseno`="+str(course)+" or `instructor`='"+str(instructor)+"';")
            cursor=self.conn.cursor()
            cursor.execute(query)
        except:
            return False
        
            
        l=[]
        t=time.time()-stime
        l.append({'time':t})
        
        for i in cursor:
            l.append({'course':i[0],'section':i[1],'title':i[2],'day':i[4],'instructor':i[3],'start':i[5],'end':i[6],'max':i[7],'enrolled':i[8]})
        
        
        return l
        
    def validateLogin(self,uid,passw):
        
        query=("select * from logindetails where `id`='"+str(uid)+"';")
        cursor=self.conn.cursor()
        cursor.execute(query)
        l=list(cursor)
        if(len(l)!=1):
            return 0
        if(str(l[0][2])!=passw):
            return 1
        query=("select name from users where `userid`='"+str(uid)+"';")
        cursor.execute(query)
        l=list(cursor)
        self.userid=uid
        if(self.redisObj.get(uid) is None):
            self.redisObj.set(uid,time.time())
        
                
        return l[0][0]
    def register(self,uid,password,name):
        query=("select * from logindetails where `id`='"+str(uid)+"';")
        cursor=self.conn.cursor()
        cursor.execute(query)
        l=list(cursor)
        if(len(l)==1):
            return 0 #user id already registered
        query2=("INSERT INTO `mymav`.`logindetails` (`id`, `password`) VALUES ('"+str(uid)+"', '"+str(password)+"');")
        cursor.execute(query2)
        
        l=list(cursor)
        self.conn.commit()
        query3=("INSERT INTO `mymav`.`users` (`userid`, `name`) VALUES ('"+str(uid)+"', '"+str(name)+"');")
        cursor.execute(query3)
        l=list(cursor)
        self.conn.commit()
        return 1
    
    def dropcourse(self,uid,course,instructor,section):
        self.conn.commit()
        query=("DELETE FROM `mymav`.`enrolledcourses` WHERE `userid`='"+str(uid)+"' and `courseid`='"+str(course)+"';")
        cursor=self.conn.cursor()
        try:
            cursor.execute(query)
            
        except:
            return False
        l=list(cursor)
        self.conn.commit()
        return True
    def getallcourses(self):
        self.conn.commit()
        query=('select * from `mymav`.`classes`;')
        
        
        
        cursor=self.conn.cursor()
        cursor.execute(query)
        l=[]
        for i in cursor:
            l.append({'course':i[0],'section':i[1],'title':i[2],'day':i[4],'instructor':i[3],'start':i[5],'end':i[6],'max':i[7],'enrolled':i[8]})
        
        return l
    def enrollcourse(self,uid,course,instructor,section):
        query=("select * from `enrolledcourses` where `userid`='"+str(uid)+"' and `courseid`='"+str(course)+"' and `section`='"+str(section)+"';")
        cursor=self.conn.cursor()
        try:
            cursor.execute(query)
        except:
            return 0
        l=list(cursor)
        if(len(l)>0):
            return 1   
        self.conn.commit()
        query=("INSERT INTO `mymav`.`enrolledcourses` (`userId`, `courseid`, `section`, `instructor`) VALUES ('"+str(uid)+"', '"+str(course)+"', '"+str(section)+"', '"+str(instructor)+"');")
        
        try:
            cursor.execute(query)
            self.conn.commit()
        except:
            return 0    
        l=list(cursor)
        
        return 2
        