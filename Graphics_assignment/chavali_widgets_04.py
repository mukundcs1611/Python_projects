#Chavali, Srinivas Mukund
#1001-242-350
#2016-04-20
# Assignment_04

from math import *
import struct
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

import math
from tkinter import Label




class cl_widgets:
    def __init__(self,ob_root_window,ob_world,camera):
        self.ob_root_window=ob_root_window
        self.ob_world=ob_world
#         self.menu=cl_menu(self)
        self.pannel_01 = cl_pannel_01(self)
        self.pannel_02 = cl_pannel_02(self)
   
        self.camera=camera
        self.ob_canvas_frame=cl_canvas_frame(self)
        #self.status = cl_statusBar_frame(self)
        
        
        for j in range(len(self.ob_world)):
            
            self.ob_world[j].defWorld(self.ob_canvas_frame.canvas,camera.s[j],camera.W[j],camera.vup[j],camera.vpn[j],camera.vrp[j],camera.prp[j],camera.cameraNames[j],camera.projTypes[j],j)# Added parallel view 3d params 05-apr
        
        for worlds in self.ob_world:
            worlds.add_canvas(self.ob_canvas_frame.canvas)

class cl_canvas_frame:
    def __init__(self, master):
        self.master=master
        self.canvas = Canvas(master.ob_root_window,width=640, height=640, bg="yellow", highlightthickness=0)
        self.canvas.pack(expand=YES, fill=BOTH)
        
#         master.camera.addCanvas()
        self.canvas.bind('<Configure>', self.canvas_resized_callback) 
        self.canvas.bind("<ButtonPress-1>", self.left_mouse_click_callback)
        #self.canvas.bind("<ButtonRelease-1>", self.left_mouse_release_callback)
        #self.canvas.bind("<B1-Motion>", self.left_mouse_down_motion_callback)
        #self.canvas.bind("<ButtonPress-3>", self.right_mouse_click_callback)
        #self.canvas.bind("<ButtonRelease-3>", self.right_mouse_release_callback)
        #self.canvas.bind("<B3-Motion>", self.right_mouse_down_motion_callback)
        #self.canvas.bind("<Key>", self.key_pressed_callback)    
        self.canvas.bind("<Up>", self.up_arrow_pressed_callback)
        self.canvas.bind("<Down>", self.down_arrow_pressed_callback)
        self.canvas.bind("<Right>", self.right_arrow_pressed_callback)
        self.canvas.bind("<Left>", self.left_arrow_pressed_callback)     
        self.canvas.bind("<Shift-Up>", self.shift_up_arrow_pressed_callback)
        self.canvas.bind("<Shift-Down>", self.shift_down_arrow_pressed_callback)
        self.canvas.bind("<Shift-Right>", self.shift_right_arrow_pressed_callback)
        self.canvas.bind("<Shift-Left>", self.shift_left_arrow_pressed_callback)   
        self.canvas.bind("f", self.f_key_pressed_callback)  
        self.canvas.bind("b", self.b_key_pressed_callback)
          
    def key_pressed_callback(self,event):
        print ('key pressed')      
    def up_arrow_pressed_callback(self,event):
        print ('pressed up')
        
    def down_arrow_pressed_callback(self,event):
        print ('pressed down')     
    def right_arrow_pressed_callback(self,event):
        print ('pressed right')       
    def left_arrow_pressed_callback(self,event):
        print ('pressed left')       
    def shift_up_arrow_pressed_callback(self,event):
        self.canvas.world.translate(0,1)
    def shift_down_arrow_pressed_callback(self,event):
        pass
    def shift_right_arrow_pressed_callback(self,event):
        pass
    def shift_left_arrow_pressed_callback(self,event):
        pass
    def f_key_pressed_callback(self,event):

        print ("f key was pressed")
    def b_key_pressed_callback(self,event):
        
        print ("b key was pressed")         
    def left_mouse_click_callback(self,event):
        print ('Left mouse button was clicked')
        print ('x=',event.x, '   y=',event.y)
        self.x = event.x
        self.y = event.y  
        self.canvas.focus_set()
    def left_mouse_release_callback(self,event):
        print ('Left mouse button was released')
        print ('x=',event.x, '   y=',event.y)
        print ('canvas width', self.canvas.cget("width"))
        self.x = None
        self.y = None
        
    def left_mouse_down_motion_callback(self,event):
        print ('Left mouse down motion')
        print ('x=',event.x, '   y=',event.y)
        self.x = event.x
        self.y = event.y 
        
    def right_mouse_click_callback(self,event):
        
        self.x = event.x
        self.y = event.y   
    def right_mouse_release_callback(self,event):
        
        self.x = None
        self.y = None        
    def right_mouse_down_motion_callback(self,event):
        pass
    def canvas_resized_callback(self,event):
        wscale = float(event.width)/float(self.canvas.cget("width"))
        hscale = float(event.height)/float(self.canvas.cget("height"))
        self.width = event.width
        self.height = event.height
        self.canvas.config(width=event.width,height=event.height)
        #self.canvas.config(width=event.width-4,height=event.height-4)
        #print 'canvas width height', self.canvas.cget("width"), self.canvas.cget("height")
        #print 'event width height',event.width, event.height
        
        self.canvas.pack()
        print ('canvas width', self.canvas.cget("width"))
        print ('canvas height', self.canvas.cget("height"))
        self.canvas.scale("all",0,0,wscale,hscale)
        
class cl_pannel_01:
    filename=''
    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.var_filename = StringVar()
        self.var_filename.set('')
        
        self.file_dialog_button = Button(frame, text="browse", command=self.browse_file)
        self.file_dialog_button.pack(side=LEFT)
        self.hi_there = Button(frame,text="load", command=self.load_callback)
        self.hi_there.pack(side=LEFT)
        
        
#         self.load_camera()
    
                     
#                 
#            i top
# t parallel
# r 0 4 0
# n 0 -1 0
# u 0 0 -1
# p 0 0 5 
# w -4 4 -4 4 -20 100
# s 0.1 0.6 0.4 0.9
    def load_callback(self):    
        ##Write a method which reads from a file
        
        infile=open(self.master.pannel_01.filename)
        temp_canvas=self.master.ob_canvas_frame.canvas
        for j in range(len(self.master.ob_world)):
            
            if(len(self.master.ob_world[j].objects)>0):
                temp_canvas.delete(self.master.camera.cameraNames[j])
                self.master.ob_world[j].objects=[]    
                temp_canvas.update()
                self.master.ob_world[j].canvasPrevLen=self.master.ob_world[j].canvasPrevLen+len(self.master.ob_world[j].coords)+4
        
        vertices=0
        faces=0
        v={}
        f={}
        W={}
        s={}
        camRef=self.master.camera
        for line in infile.readlines():
            
            tokens = line.split()        # tokens on each line
            numbers = [float(i) for i in tokens[1:len(tokens)]]
            if(len(tokens)>0):
                firsttoken = tokens[0]
                if(firsttoken=='v'):
                    vertices+=1      
                    v[vertices]=numbers[0:len(tokens)]
                             
                elif(tokens[0]=='f'):
                    faces+=1   
                    f[faces]=[int(i) for i in numbers[0:len(tokens)]]
                    
        
        for j in range(len(self.master.ob_world)):
            self.master.ob_world[j].defFig(temp_canvas,v,f)          
            for i in f:
                if(len(f[i])==3):
                    vertex1=[v[f[i][0]][0],v[f[i][0]][1],v[f[i][0]][2]]
                    vertex2=[v[f[i][1]][0],v[f[i][1]][1],v[f[i][1]][2]]
                    vertex3=[v[f[i][2]][0],v[f[i][2]][1],v[f[i][2]][2]]        
                    self.master.ob_world[j].drawTriangle(camRef.cameraNames[j],temp_canvas,vertex1,vertex2,vertex3)
                if(len(f[i])==4):
                    vertex1=[v[f[i][0]][0],v[f[i][0]][1],v[f[i][0]][2]]
                    vertex2=[v[f[i][1]][0],v[f[i][1]][1],v[f[i][1]][2]]
                    vertex3=[v[f[i][2]][0],v[f[i][2]][1],v[f[i][2]][2]]        
                    vertex4=[v[f[i][3]][0],v[f[i][3]][1],v[f[i][3]][2]]
                    self.master.ob_world[j].drawPolygon(camRef.cameraNames[j],temp_canvas,vertex1,vertex2,vertex3,vertex4)        

#         frame.grid()

       
    def say_hi(self):
        print ( "hi there, everyone!")
    def ask_for_string(self):
        s=simpledialog.askstring('My Dialog', 'Please enter a string')
        print ( s)
    def ask_for_float(self):
        f=simpledialog.askfloat('My Dialog', 'Please enter a string')
        print ( f)

    def browse_file(self):
        self.var_filename.set(filedialog.askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.txt")]))
        self.filename = self.var_filename.get()
        print(self.filename)
class cl_pannel_02:
    filename=''
    
    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
#         self.button = Button(frame,text="Open Dialog", fg="blue", command=self.open_dialog_callback)
#         self.button.pack(side=LEFT)

        
        Label(frame, text="Rotation Axis:").pack(side=LEFT)
        self.axis=IntVar()
        Radiobutton(frame, text='z', variable=self.axis,
                    value=0).pack(side=LEFT, anchor=W)
        Radiobutton(frame, text='x', variable=self.axis,
                    value=1).pack(side=LEFT, anchor=W)
        Radiobutton(frame, text='y', variable=self.axis,
                    value=2).pack(side=LEFT, anchor=W)
        frame.pack(expand=1, fill=X, pady=2, padx=2)
        self.angle=IntVar()
        self.angle.set(0)
        Label(frame, text="Degree:").pack(side=LEFT)
        sb=Spinbox(frame, from_=-360, to=360,textvariable=self.angle,width=4)
        sb.pack(side=LEFT)
        self.angsteps=IntVar()
        self.angsteps.set(1)
        Label(frame, text="Steps:").pack(side=LEFT)
        sb2=Spinbox(frame, from_=1, to=10,textvariable=self.angsteps,width=4)
        sb2.pack(side=LEFT)
        Button(frame, text='Rotate', command=self.call_rotate).pack(side=LEFT)
        frame2 = Frame(master.ob_root_window)
        frame2.pack(expand=1, fill=X, pady=2, padx=2)
        Label(frame2, text="Scale Ratio:").pack(side=LEFT)
        self.scalesel=DoubleVar()
        self.scalesel.set(0)
        Radiobutton(frame2, text='all', variable=self.scalesel,
                    value=0).pack(side=LEFT, anchor=W)
        self.scaleAll=DoubleVar()
        self.scaleAll.set(1.00)
        sb3=Spinbox(frame2, from_=0, to=2,textvariable=self.scaleAll,width=4,increment=0.25)
        sb3.pack(side=LEFT)
                   
        Radiobutton(frame2, text='[Sx,Sy,Sz]:', variable=self.scalesel,
                    value=1).pack(side=LEFT, anchor=W)
        self.e1 = Entry(frame2,width=3)
        self.e1.pack(side=LEFT)
        self.e1.delete(0, END)
        self.e1.insert(0, 1.0)
        self.e2 = Entry(frame2,width=3)
        self.e2.pack(side=LEFT)
        self.e2.delete(0, END)
        self.e2.insert(0, 1.0)
        self.e3 = Entry(frame2,width=3)
        self.e3.pack(side=LEFT)
        self.e3.delete(0, END)
        self.e3.insert(0, 1.0)
        self.scaleSteps=IntVar()
        self.scaleSteps.set(1)
        Label(frame2, text="Steps:").pack(side=LEFT)
        sb4=Spinbox(frame2, from_=1, to=10,textvariable=self.scaleSteps,width=4)
        sb4.pack(side=LEFT)
        Button(frame2, text='Scale', command=self.call_scale).pack(side=LEFT)
        Label(frame2, text="[dx,dy,dz]:").pack(side=LEFT)
        self.e4 = Entry(frame2,width=3)
        self.e4.pack(side=LEFT)
        self.e4.delete(0, END)
        self.e4.insert(0, 0.0)
        self.e5 = Entry(frame2,width=3)
        self.e5.pack(side=LEFT)
        self.e5.delete(0, END)
        self.e5.insert(0, 0.0)
        self.e6 = Entry(frame2,width=3)
        self.e6.pack(side=LEFT)
        self.e6.delete(0, END)
        self.e6.insert(0, 0.0)
        self.translateSteps=IntVar()
        self.translateSteps.set(1)
        Label(frame2, text="Steps:").pack(side=LEFT)
        sb5=Spinbox(frame2, from_=1, to=10,textvariable=self.scaleSteps,width=4)
        sb5.pack(side=LEFT)
        Button(frame2, text='Translate', command=self.call_translate).pack(side=LEFT)
        
        
        
    def call_rotate(self):    
        
        temp_canvas=self.master.ob_canvas_frame.canvas
        for i in range(len(self.master.ob_world)):
            self.master.ob_world[i].rotate(temp_canvas,self.axis.get(),math.radians(self.angle.get()),self.angsteps.get())                  
        
    def call_scale(self):
        steps=self.scaleSteps.get()
        scalewidth=1.0
        scaleheight=1.0
        scaledepth=1.0
        if(self.scalesel.get()==0):
            scalewidth=self.scaleAll.get()   
            scaleheight=self.scaleAll.get()
            scaledepth=self.scaleAll.get()
        else:
            scalewidth=getdouble(self.e1.get())   
            scaleheight=getdouble(self.e2.get())
            scaledepth=getdouble(self.e3.get())
        for i in range(len(self.master.ob_world)):   
            self.master.ob_world[i].scale(self.master.ob_canvas_frame.canvas,[scalewidth,scaleheight],steps)
        
    def call_translate(self):
        steps=self.translateSteps.get()
        for i in range(len(self.master.ob_world)):
            self.master.ob_world[i].translate_all(self.master.ob_canvas_frame.canvas,getdouble(self.e4.get()),getdouble(self.e5.get()),getdouble(self.e6.get()),steps)   
#     def open_dialog_callback(self):
#         d = MyDialog(self.master.ob_root_window)
#         print ( d.result)
#         print ( "mydialog_callback pressed!"   )     
#     
#                        
# class MyDialog(simpledialog.Dialog):
#     def body(self, master):
# 
#         Label(master, text="Integer:").grid(row=0, sticky=W)
#         Label(master, text="Float:").grid(row=1, column=0 ,sticky=W)
#         Label(master, text="String:").grid(row=1, column=2 , sticky=W)
#         self.e1 = Entry(master)
#         self.e1.insert(0, 0)
#         self.e2 = Entry(master)
#         self.e2.insert(0, 4.2)
#         self.e3 = Entry(master)
#         self.e3.insert(0, 'Default text')
# 
#         self.e1.grid(row=0, column=1)
#         self.e2.grid(row=1, column=1)
#         self.e3.grid(row=1, column=3)
#         
#         
#         self.cb = Checkbutton(master, text="Hardcopy")
#         self.cb.grid(row=3, columnspan=2, sticky=W)
# 
# 
#     def apply(self):
#         try:
#             first = int(self.e1.get())
#             second = float(self.e2.get())
#             third=self.e3.get()
#             self.result = first, second, third
#         except ValueError:
#             tkMessageBox.showwarning(
#                 "Bad input",
#                 "Illegal values, please try again"
#             )
# 
# 
# #class StatusBar:
# 
#     #def __init__(self, master):
#         #self.master=master
#         #self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
#         #self.label.pack(fill=X)
# 
#     #def set(self, format, *args):
#         #self.label.config(text=format % args)
#         #self.label.update_idletasks()
# 
#     #def clear(self):
#         #self.label.config(text="")
#         #self.label.update_idletasks()       
# 
# class cl_statusBar_frame:
# 
#     def __init__(self, master):
#         self.master=master
#         status = StatusBar(master.ob_root_window)
#         status.pack(side=BOTTOM, fill=X)
#         status.set('%s','This is the status bar')
# 
# 
#     def set(self, format, *args):
#         self.label.config(text=format % args)
#         self.label.update_idletasks()
# 
#     def clear(self):
#         self.label.config(text="")
#         self.label.update_idletasks()
# class cl_menu:
#     def __init__(self, master):
#         
#         self.master=master
#         self.menu = Menu(master.ob_root_window)
#         master.ob_root_window.config(menu=self.menu)
#         self.filemenu = Menu(self.menu)
#         self.menu.add_cascade(label="File", menu=self.filemenu)
#         self.filemenu.add_command(label="New", command=self.menu_callback)
#         self.filemenu.add_command(label="Open...", command=self.menu_callback)
#         self.filemenu.add_separator()
#         self.filemenu.add_command(label="Exit", command=self.menu_callback)
#         self.dummymenu = Menu(self.menu)
#         self.menu.add_cascade(label="Dummy", menu=self.dummymenu)
#         self.dummymenu.add_command(label="Item1", command=self.menu_item1_callback)
#         self.dummymenu.add_command(label="Item2", command=self.menu_item2_callback)
#         
#         self.helpmenu = Menu(self.menu)
#         self.menu.add_cascade(label="Help", menu=self.helpmenu)
#         self.helpmenu.add_command(label="About...", command=self.menu_help_callback)        
# 
#     def menu_callback(self):
#         print ("called the menu callback!")
#                         
#     def menu_help_callback(self):
#         print ("called the help menu callback!") 
#     def menu_item1_callback(self):
#         print ("called item1 callback!")    
# 
#     def menu_item2_callback(self):
#         print ("called item2 callback!")    
