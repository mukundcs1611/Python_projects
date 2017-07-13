'''
Created on Jun 28, 2017

@author: chavali
'''
from flask import Flask,request,redirect
from flask.templating import render_template
from dbmodule import DB
from flask.json import jsonify
import json
from flask.helpers import url_for
from flask.globals import session



loggedinusers=[]
app=Flask(__name__)
db={}
db=DB()
db.connectToDB()


@app.route('/')
def mainPage():
    return render_template('index.html',l={'name':'Srinivas Mukund Chavali', 'id': '1001242350'})
 
@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    loginid=request.form['loginid']
    passw=request.form['pass']
    if(db.register(loginid,passw,name)==1):
        return render_template('viewcourses.html',name={'id':loginid})
    else:
        return "User id is already taken please choose a different id <br/><a href='/'>Go Back</a>"    
@app.route('/login',methods=['POST'])
def login():
    
    
    uid=request.form['id']
    passw=request.form['pass']
    ret=db.validateLogin(uid, passw)
    
    try:
        n=int(ret)
    except:
        return render_template('viewcourses.html',name={'id':uid})
    if(n==1 or n==0):
        return "User ID or password wrong , did you enter the correct details? <br/><a href='/'>Go Back</a>"
@app.route('/_getmycourses/<uid>',methods=['POST'])
def viewmycourses(uid):
    
    if(db.redisObj.get(uid) is None):
        return "Please Login to see your courses <br/> <br/><a href='/'>Go To Login Screen</a>"
    l=db.getenrolledcourses(uid)
    
    return json.dumps(l)
@app.route('/dropcourse/<course>/<instructor>/<section>/<uid>')
def dropmycourses(course,instructor,section,uid):
    
    
    if(db.redisObj.get(uid) is None):
        return "Please Login to view your content <br/> <br/><a href='/'>Go To Login Screen</a>"
    if(db.dropcourse(uid, course,instructor,section)):
        
        
        return render_template('/viewcourses.html', name={'id':uid,'success':"Drop Successful"})
    else:
        return "cannot delete <br/><a href='/login'>Go Back</a> "

@app.route('/searchcourses/<uid>',methods=['POST'])
def searchcourses(uid):
    if(db.redisObj.get(uid) is None):
        return "Please Login to see your courses <br/> <br/><a href='/'>Go To Login Screen</a>"
    
    l=db.getallcourses()
    return json.dumps(l)
@app.route('/enroll/<course>/<instructor>/<section>/<uid>')
def enrollcourse(course,instructor,section,uid):
    if(db.redisObj.get(uid) is None):
        return "Please Login to see your courses <br/> <br/><a href='/'>Go To Login Screen</a>"
    
    if(db.enrollcourse(uid, course,instructor,section)==2):
        
       
       
        return render_template('/viewcourses.html', name={'id':uid,'success':"Enroll Successful"})
    else:
        return "cannot enroll <br/><a href='/'>Go to Login</a> "
@app.route('/logout/<uid>')
def logout(uid):
    db.redisObj.delete(uid)
    return redirect('/')
@app.route('/getcourse',methods=['POST'])
def getcourses():
    course=request.form['course']
    instructor=request.form['instructor']
   
    l=db.getcourse(course, instructor)
    if(~l):
        return "INternal Error"
    else:
        return json.dumps(l)
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')
if(__name__=='__main__'):
    app.run(debug=True,port=5000)    