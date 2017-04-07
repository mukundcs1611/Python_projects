#Chavali, Srinivas Mukund 
#1001-242-350
#2016-04-05
#Assignment_03
# from _decimal import Decimal
from math import *
from time import sleep
import time
from tkinter import *

from numpy  import *


class cl_world:
    worldC={}
    viewCoord={}
    xtheta=0.0
    ytheta=0.0
    ztheta=0.0
    worldRealC={}
    vrp=[]
    vrp2=[]
    vpn=[]
    prp=[]
    vup=[]
    nmin=0
    nmax=0
    umin=0
    umax=0
    vmin=0
    vmax=0
    facesf=False
    xPartSize=0
    yPartSize=0
    origin=[]
    VxScale=0
    VyScale=0
    vertices={}
    faces={}
    objects=[]
    i=0
    canvasPrevLen=0
    
    xMScale=0.0
    yMScale=0.0
    coords=[]
    def __init__(self,canvases=[]):
        
       
        self.canvases=canvases
        #self.display
        
    
 
    def add_canvas(self,canvas):
        self.canvases.append(canvas)
        canvas.world=self
        
    
    def create_graphic_objects(self,canvas):
        self.objects.append(canvas.create_line(63,63,64,574))
        self.objects.append(canvas.create_line(0,0,canvas.cget("width"),canvas.cget("height")))
        self.objects.append(canvas.create_line(canvas.cget("width"),0,0,canvas.cget("height")))
        self.objects.append(canvas.create_oval(int(0.25*int(canvas.cget("width"))),
            int(0.25*int(canvas.cget("height"))),
            int(0.75*int(canvas.cget("width"))),
            int(0.75*int(canvas.cget("height")))))        
    def translate(self,points,translate):
        
        points[0]=float(points[0])+(0-translate[0])
        points[1]=float(points[1])+(0-translate[1])
        points[2]=float(points[2])+(0-translate[2])
        return points
    def viewMappingPerspective(self,v1):

        v1t=[0.0,0.0,0.0]
        #Step 1 Translate vrp to origin
        self.translate(v1,self.vrp)
        
            
        #Step 2 Rotate VPN around x-axis until it lies in the xz-plane
        
        if(float(self.vpn[1])!=0.0 or float(self.vpn[2])!=0.0 ):
            #v1[1]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+v1[1]*(-1*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))
            #v1[1]*(-1*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))
            v1t[1]=v1[1]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+v1[2]*((-1)*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))                                                                                           
            v1t[2]=v1[1]*(self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+ v1[2]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))
            v1[1]=v1t[1]
            v1[2]=v1t[2]
            
        
        #Step 3 Rotate VPN around y-axis until it aligns with the positive z-axis
        #pb2+c2 pa2+b2+c2
        if(float(self.vpn[0])!=0.0 or self.vpn[1]!=0.0):
            v1t[0]=v1[0]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))+ v1[2]*(-self.vpn[0]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
            v1t[2]=v1[0]*(self.vpn[0]/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2))))+v1[2]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
            v1[0]=v1t[0]
            v1[2]=v1t[2]
        
        if(float(self.vup[1])!=0.0 or float(self.vup[0])!=0.0):
            v1t[0]=v1[0]*(self.vup[1]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))+v1[1]*((-1)*self.vup[0]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))
            v1t[1]=v1[0]*(self.vup[0]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))+v1[1]*(self.vup[1]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))
#            v1t[0]=float(v1[0])*self.vup[1]/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))+float(v1[1])*(-(math.pow(self.vup[0],2))/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))
#            v1t[1]=float(v1[1])*self.vup[1]/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))+float(v1[0])*(math.pow(self.vup[0],2)/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))                             
            v1[0]=v1t[0]
            v1[1]=v1t[1]
        
      
        #step 5 Translate the Center of Window on the front plane (nmin) to the origin
        self.translate(v1,[float(self.prp[0]),float(self.prp[1]),float(self.prp[2])])
        
        #Step 6  Shear such that the Direction of Projection (DOP) becomes parallel to the z-axis. DOP is deﬁned by connecting the center of window (CW) to PRP
#             
#         v1t[0]=v1[0]+v1[2]*self.shx
#         v1t[1]=v1[1]+v1[2]*self.shy
#         v1[0]=v1t[0]
#         v1[1]=v1t[0] 

#         Step 8  Scale such that the view volume becomes the canonical parallel view volume which is bounded by the planes x = 1; x = −1; y = 1; y = −1; z = 0; z = 1
         
        v1[0]=v1[0]*(1/self.nmax)*(self.umax-self.umin)*(1/self.VxScale)
        v1[1]=v1[1]*(1/self.nmax)*(self.vmax-self.vmin)*(1/self.VyScale)#(self.scaley)
        v1[2]=v1[2]*(1/self.nmax)*(self.nmax-self.nmin)
         
        return v1

        
    def viewMappingParallel(self,v1):
        #vpn vup vrp are ,pdified too!!
        v1t=[0.0,0.0,0.0]
       
        #Step 1 Translate vrp to origin
        self.translate(v1,self.vrp)
        
            
        #Step 2 Rotate VPN around x-axis until it lies in the xz-plane
        
        if(float(self.vpn[1])!=0.0 or float(self.vpn[2])!=0.0 ):
            #v1[1]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+v1[1]*(-1*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))
            #v1[1]*(-1*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))
            v1t[1]=v1[1]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+v1[2]*((-1)*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))                                                                                           
            v1t[2]=v1[1]*(self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+ v1[2]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))
            v1[1]=v1t[1]
            v1[2]=v1t[2]
            
        
        #Step 3 Rotate VPN around y-axis until it aligns with the positive z-axis
        #pb2+c2 pa2+b2+c2
        if(float(self.vpn[0])!=0.0 or self.vpn[1]!=0.0):
            vpnt=[0.0,self.vpn[1],math.sqrt(math.pow(self.vpn[0],2)+math.pow(self.vpn[2],2))]
            
            v1t[0]=v1[0]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))+ v1[2]*(-self.vpn[0]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
            v1t[2]=v1[0]*(self.vpn[0]/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2))))+v1[2]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
            v1[0]=v1t[0]
            v1[2]=v1t[2]
        
        #step 4 Rotate VUP around z-axis until it lies in the yz-plane with positive y
        if(float(self.vup[1])!=0.0 or float(self.vup[0])!=0.0):
            v1t[0]=v1[0]*(self.vup[1]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))+v1[1]*((-1)*self.vup[0]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))
            v1t[1]=v1[0]*(self.vup[0]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))+v1[1]*(self.vup[1]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[0],2))))
#            v1t[0]=float(v1[0])*self.vup[1]/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))+float(v1[1])*(-(math.pow(self.vup[0],2))/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))
#            v1t[1]=float(v1[1])*self.vup[1]/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))+float(v1[0])*(math.pow(self.vup[0],2)/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))                             
            v1[0]=v1t[0]
            v1[1]=v1t[1]
        #Step 5  Shear such that the Direction of Projection (DOP) becomes parallel to the z-axis. DOP is deﬁned by connecting the center of window (CW) to PRP


        #step 6 Translate the Center of Window on the front plane (nmin) to the origin
#         self.translate(v1,[self.umin,self.vmin,self.nmin])
        
        #step 7 

        #Step 8  Scale such that the view volume becomes the canonical parallel view volume which is bounded by the planes x = 1; x = −1; y = 1; y = −1; z = 0; z = 1

#         v1[0]=v1[0]*(float(1/self.vmax))
#         v1[1]=v1[1]*(float(1/self.vmax))
#         v1[2]=v1[2]*(0.008)
        
        return v1
    def getRealCoord(self,v):
        ##Adhoc method ! taking in vertex values and scaling with viewport and window at the same time.      
        
        vi=[0.0,0.0,0.0]
        if(float(v[0])<0):
            vi[0]=(self.origin[0])-((-1*float(v[0]))*self.xPartSize*self.VxScale)
             
        elif(float(v[0])>=0):
            vi[0]=(self.origin[0])+((float(v[0]))*self.xPartSize*self.VxScale)
             
        if(float(v[1])<0):
            vi[1]=(self.origin[1])+((-1*float(v[1]))*self.yPartSize*self.VyScale)
             
        elif(float(v[1])>=0):
            vi[1]=(self.origin[1])-((float(v[1]))*self.yPartSize*self.VyScale)
                 
        if(float(v[2])<0):
            vi[2]=(self.origin[1])-((-1*float(v[2]))*self.yPartSize*self.VyScale)
             
        elif(float(v[2])>=0):
            vi[2]=(self.origin[1])+((float(v[2]))*self.yPartSize*self.VyScale)
           
        return vi    
    def translate_all(self,canvas,dx,dy,dz,steps):
        
        #dx,dy,dz=self.getRealCoord([dx,dy,dz])
        lists=canvas.find_withtag(self.cameraName)
        x=0
        dx=dx/steps
        dy=dy/steps
        dz=dz/steps
        for i in range(steps):
         for c in range(len(self.coords)):
            
            line=[0.0,0.0,0.0,0.0,0.0,0.0]
            
            for k in range(6):
                if(k%3==0):#for x
                    if(self.origin[0]>=self.coords[c][k]):
                        line[k]=(-1)*(self.origin[0]-self.coords[c][k])/(self.xPartSize*self.VxScale)
                    else: 
                        line[k]=(self.coords[c][k]-self.origin[0])/(self.xPartSize*self.VxScale)
                elif(k%3==1):
                    if(self.origin[1]>=self.coords[c][k]):
                        line[k]=(-1)*(self.coords[c][k]-self.origin[1])/(self.yPartSize*self.VyScale)
                    else: 
                        line[k]=(self.origin[1]-self.coords[c][k])/(self.yPartSize*self.VyScale)
                else:
                    if(self.origin[1]>=self.coords[c][k]):
                            line[k]=(-1)*(self.origin[1]-self.coords[c][k])/(self.yPartSize*self.VyScale)
                    else: 
                            line[k]=(self.coords[c][k]-self.origin[1])/(self.yPartSize*self.VyScale)#                 for z value , differentiate from the 1,2 and 3 vertex and take the z from faces list
            x0,y0,z0,x1,y1,z1=line
            
            canvas.coords(lists[x],self.coords[c][0],self.coords[c][1],self.coords[c][3],self.coords[c][4])
            canvas.move(lists[x],dx,dy)
            points=canvas.coords(lists[x])
            z0=self.coords[c][2]
            z1=self.coords[c][5]
            self.coords[c]=[points[0],points[1],z0,points[2],points[3],z1]
                                       
            
            points=self.lineClip(self.viewxMin,self.viewyMin,self.viewxMax,self.viewyMax, points[0],points[1],points[2],points[3])
            if(points[0] is None):
   
                    canvas.itemconfig(lists[x],fill='yellow')
                    
            else:
                    canvas.coords(lists[x],points)  
                    canvas.itemconfig(lists[x],fill='black')
                    
            x=x+1    
#         
#         points[0]=float(points[0])+(0-translate[0])
#         points[1]=float(points[1])+(0-translate[1])
#         points[2]=float(points[2])+(0-translate[2])
#         return points
    def fly(self,canvas,dx,dy,dz):
        for c in range(len(self.coords)):
                canvas.coords(c+5+self.canvasPrevLen,self.coords[c][0],self.coords[c][1],self.coords[c][3],self.coords[c][4])
                canvas.move(c+5+self.canvasPrevLen,-dx,dy)
                points=canvas.coords(c+5+self.canvasPrevLen)
                z0=self.coords[c][2]
                z1=self.coords[c][5]
                self.coords[c]=[points[0],points[1],z0,points[2],points[3],z1]                           
            
                points=self.lineClip(self.viewxMin,self.viewyMin,self.viewxMax,self.viewyMax, points[0],points[1],points[2],points[3])
                if(points[0] is None):
   
                    canvas.itemconfig(c+5+self.canvasPrevLen,fill='yellow')
                else:
                    canvas.coords(c+5+self.canvasPrevLen,points)  
                    canvas.itemconfig(c+5+self.canvasPrevLen,fill='black')
   
        
    def drawTriangle(self,cameraName,canvas,v1,v2,v3):
       
        
        if(self.cameraType=='parallel'):
            self.firstV=self.getRealCoord(self.viewMappingParallel(v1))
            self.secondV=self.getRealCoord(self.viewMappingParallel(v2))
            self.thirdV=self.getRealCoord(self.viewMappingParallel(v3))
        else:
            self.firstV=self.getRealCoord(self.viewMappingPerspective(v1))
            self.secondV=self.getRealCoord(self.viewMappingPerspective(v2))
            self.thirdV=self.getRealCoord(self.viewMappingPerspective(v3))
                
#         self.firstV=self.getRealCoord(v1)
#         self.secondV=self.getRealCoord(v2)
#         self.thirdV=self.getRealCoord(v3)
        points = [int((self.firstV[0])),int((self.firstV[1])),int((self.firstV[2])),int((self.secondV[0])),int((self.secondV[1])),int((self.secondV[2])), int(self.thirdV[0]),int(self.thirdV[1]),int((self.thirdV[2]))]
        
        self.objects.append(canvas.create_line(points[0],points[1],points[3],points[4],fill='black',tags=self.cameraName))
        self.coords.append([points[0],points[1],points[2],points[3],points[4],points[5]])
        self.objects.append(canvas.create_line(points[3],points[4],points[6],points[7],fill='black',tags=self.cameraName))
        self.coords.append([points[3],points[4],points[5],points[6],points[7],points[8]])
        self.objects.append(canvas.create_line(points[0],points[1],points[6],points[7],fill='black',tags=self.cameraName))
        self.coords.append([points[0],points[1],points[2],points[6],points[7],points[8]])
        
       
#          
#         self.objects.append(canvas.create_polygon(points,outline='black',fill='yellow'))
        
        
    def drawPolygon(self,cameraName,canvas,v1,v2,v3,v4):
#         firstV=[]
#         secondV=[]
#         thirdV=[]
#         fourthV=[]
        if(self.cameraType=='parallel'):
            self.firstV=self.getRealCoord(self.viewMappingParallel(v1))
            self.secondV=self.getRealCoord(self.viewMappingParallel(v2))
            self.thirdV=self.getRealCoord(self.viewMappingParallel(v3))
            self.fourthV=self.getRealCoord(self.viewMappingParallel(v4))
        else:
            self.firstV=self.getRealCoord(self.viewMappingPerspective(v1))
            self.secondV=self.getRealCoord(self.viewMappingPerspective(v2))
            self.thirdV=self.getRealCoord(self.viewMappingPerspective(v3))
            self.fourthV=self.getRealCoord(self.viewMappingPerspective(v4))
#         self.firstV=self.getRealCoord(v1)
#         self.secondV=self.getRealCoord(v2)
#         self.thirdV=self.getRealCoord(v3)
#         self.fourthV=self.getRealCoord(v4)
        self.facesf=True
        points = [int((self.firstV[0])),int((self.firstV[1])),int((self.firstV[2])),int((self.secondV[0])),int((self.secondV[1])),int((self.secondV[2])), int(self.thirdV[0]),int(self.thirdV[1]),int((self.thirdV[2])),int(self.fourthV[0]),int(self.fourthV[1]),int(self.fourthV[2])]

        self.objects.append(canvas.create_line(points[0],points[1],points[3],points[4],fill='black',tags=self.cameraName))#01
        self.coords.append([points[0],points[1],points[2],points[3],points[4],points[5]])
        self.objects.append(canvas.create_line(points[0],points[1],points[9],points[10],fill='black',tags=self.cameraName))#03
        self.coords.append([points[0],points[1],points[2],points[9],points[10],points[11]])
        self.objects.append(canvas.create_line(points[3],points[4],points[6],points[7],fill='black',tags=self.cameraName))#12
        self.coords.append([points[3],points[4],points[5],points[6],points[7],points[8]])
        self.objects.append(canvas.create_line(points[6],points[7],points[9],points[10],fill='black',tags=self.cameraName))#23
        self.coords.append([points[6],points[7],points[8],points[9],points[10],points[11]])
#         self.objects.append(canvas.create_polygon(points,outline='black',fill='yellow'))
        #self.window2Viewport(canvas)
    
    def defFig(self,canvas,v,f):
        self.vertices=v
        self.faces=f
        
    def defWorld(self,canvas,s,w,vup,vpn,vrp,prp,cameraName,cameraType,camno):
        
#    Initialize
        self.cameraName=cameraName
        self.coords=[]
        self.xtheta=0.0
        self.ytheta=0.0
        self.ztheta=0.0
        self.camno=camno
        self.cameraType=cameraType
        
        self.vup=[float(vup[0]),float(vup[1]),float(vup[2])]
        self.vpn=[float(vpn[0]),float(vpn[1]),float(vpn[2])]
        self.vrp=[float(vrp[0]),float(vrp[1]),float(vrp[2])]
        self.prp=[float(prp[0]),float(prp[1]),float(prp[2])]
        
#         del[self.objects]    
        xParts=int(float(w['umax'])-float(w['umin']))
        yParts=int(float(w['vmax'])-float(w['vmin']))
        self.nmin=int(float(w['nmin']))
        self.nmax=int(float(w['nmax']))
        self.vmin=int(float(w['vmin']))
        self.vmax=int(float(w['vmax']))
        self.umin=int(float(w['umin']))
        self.umax=int(float(w['umax']))
        
        width=int(canvas.cget("width"))
        height=int(canvas.cget("height"))
        self.defCanView()
        
#         origin=[width/2,height/2]
        
        self.xPartSize=width/xParts
        self.yPartSize=height/yParts
        self.view=s
        self.viewxMin=float(self.view['xmin'])*width
        self.viewyMin=float(self.view['ymin'])*height
        self.viewxMax=float(self.view['xmax'])*width
        self.viewyMax=float(self.view['ymax'])*height
        self.VxScale=float(self.view['xmax'])-float(self.view['xmin'])
        self.VyScale=float(self.view['ymax'])-float(self.view['ymin'])
        
        self.worldRealC={'xmin':(float(self.view['xmin'])*width),'ymin':(float(self.view['ymin'])*height),'xmax':(float(self.view['xmax'])*width),'ymax':(float(self.view['ymax'])*height)}
        self.origin=[self.worldRealC['xmin']+(self.worldRealC['xmax']-self.worldRealC['xmin'])/2,self.worldRealC['ymin']-(self.worldRealC['ymin']-self.worldRealC['ymax'])/2]
        points=[self.worldRealC['xmin'],self.worldRealC['ymin'],self.worldRealC['xmax'],self.worldRealC['ymax']]
        self.objects.append(canvas.create_rectangle(points,fill='white',outline='black',tags='dabba'+self.cameraName))
#         self.objects.append(canvas.create_line(self.worldRealC['xmin'],self.worldRealC['ymin'],self.worldRealC['xmin'],self.worldRealC['ymax']))
#         self.objects.append(canvas.create_line(self.worldRealC['xmax'],self.worldRealC['ymin'],self.worldRealC['xmax'],self.worldRealC['ymax']))
#         self.objects.append(canvas.create_line(self.worldRealC['xmin'],self.worldRealC['ymin'],self.worldRealC['xmax'],self.worldRealC['ymin']))
#         self.objects.append(canvas.create_line(self.worldRealC['xmin'],self.worldRealC['ymax'],self.worldRealC['xmax'],self.worldRealC['ymax']))
        canvas.create_text(self.worldRealC['xmin']+10.00,self.worldRealC['ymin']+10.00,text=cameraName)
  
    def defCanView(self):
        #Modify VUP 
        if(float(self.vpn[1])!=0.0 or float(self.vpn[2])!=0.0 ):
            vup1t=self.vup[1]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+self.vup[2]*((-1)*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))
            vup2t=self.vup[1]*(self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+ self.vup[2]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))
            
            self.vup[1]=vup1t
            self.vup[2]=vup2t
        
        if(float(self.vpn[0])!=0.0 or self.vpn[1]!=0.0):
                
            vup0t=self.vup[0]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))+ self.vup[2]*(-self.vpn[0]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
            vup2t=self.vup[0]*(self.vpn[0]/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2))))+self.vup[2]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
            self.vup[0]=vup0t
            self.vup[2]=vup2t
            
        #modify prp
#         if(float(self.vpn[1])!=0.0 or float(self.vpn[2])!=0.0 ):
#             prp1t=self.prp[1]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+self.prp[2]*((-1)*self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))
#             prp2t=self.prp[1]*(self.vpn[1]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))+ self.prp[2]*(self.vpn[2]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))
#              
#             self.prp[1]=prp1t
#             self.prp[2]=prp2t
        #Step 3 Rotate VPN around y-axis until it aligns with the positive z-axis
        #pb2+c2 pa2+b2+c2
#         if(float(self.vpn[0])!=0.0 or self.vpn[1]!=0.0):
#                  
#             prp0t=self.prp[0]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)))/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))+ self.prp[2]*(-self.vpn[0]/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
#             prp2t=self.prp[0]*(self.vpn[0]/float(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2))))+self.prp[2]*(math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2))/math.sqrt(math.pow(self.vpn[1],2)+math.pow(self.vpn[2],2)+math.pow(self.vpn[0],2)))
#             self.prp[0]=prp0t
#             self.prp[2]=prp2t
#          
#         #step 4 Rotate VUP around z-axis until it lies in the yz-plane with positive y
#         if(float(self.vup[1])!=0.0 or float(self.vup[0])!=0.0):
#             prp0t=self.prp[0]*(self.vup[1]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[1],2))))+self.prp[1]*((-1)*self.vup[0]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[1],2))))
#             prp1t=self.prp[0]*(self.vup[0]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[1],2))))+self.prp[1]*(self.vup[1]/(math.sqrt(math.pow(self.vup[1],2)+math.pow(self.vup[1],2))))
# #            v1t[0]=float(v1[0])*self.vup[1]/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))+float(v1[1])*(-(math.pow(self.vup[0],2))/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))
# #            v1t[1]=float(v1[1])*self.vup[1]/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))+float(v1[0])*(math.pow(self.vup[0],2)/float(math.sqrt(math.pow(self.vup[0],2)+math.pow(self.vup[1],2))))                             
#             self.prp[0]=prp0t
#             self.prp[1]=prp1t    
#              
        #vrp modification
        vrpFinal=[0.0,0.0,0.0]
        self.translate(vrpFinal, self.prp)  
        self.shx=-vrpFinal[0]/vrpFinal[2]#=> -x when multiplied with z  -vrpFinal[0]/vrpFinal[2]
        self.shy=-vrpFinal[1]/vrpFinal[2]
        vrpFinal=[0.0,0.0,vrpFinal[2]]
        if((abs(vrpFinal[2]+self.nmax))>abs(vrpFinal[2]+self.nmin)):
            self.scalex=abs(vrpFinal[2])/(((self.umax-self.umin)/2)*(vrpFinal[2]+self.nmax))
            self.scaley=abs(vrpFinal[2])/(((self.vmax-self.vmin)/2)*(vrpFinal[2]+self.nmax))
            self.scalez=1/(((self.nmax-self.nmin)/2)*(vrpFinal[2]+self.nmax))
        else:
                self.scalex=abs(vrpFinal[2])/(((self.umax-self.umin)/2)*(vrpFinal[2]+self.nmin))
                self.scaley=abs(vrpFinal[2])/(((self.vmax-self.vmin)/2)*(vrpFinal[2]+self.nmin))
                self.scalez=1/(((self.nmax-self.nmin)/2)*(vrpFinal[2]+self.nmin))    
                         
            
             
    def rotate(self,canvas,axis,angle,steps):
        tempArr=self.coords
    
        thetaPerStep=angle/steps
        
        lists=canvas.find_withtag(self.cameraName)
        
        
            
        for x in range(steps):
            
            
            f=0
#           Modifying routine for dealim with scaled objects
            index=0
            for c in range(len(self.coords)):
                if(self.facesf):
                    if(c%4==0):# traverse faces list for z 
                        f=f+1
                else:
                    if(c%3==0):
                        f=f+1         
                cos_t=  math.cos(thetaPerStep)
                sin_t = math.sin(thetaPerStep)
                line=[0.0,0.0,0.0,0.0,0.0,0.0]
                
                for k in range(6):
                    if(k%3==0):#for x
                        if(self.origin[0]>=self.coords[c][k]):
                            line[k]=(-1)*(self.origin[0]-self.coords[c][k])/(self.xPartSize*self.VxScale)
                        else: 
                            line[k]=(self.coords[c][k]-self.origin[0])/(self.xPartSize*self.VxScale)
                    elif(k%3==1):
                        if(self.origin[1]>=self.coords[c][k]):
                            line[k]=(-1)*(self.coords[c][k]-self.origin[1])/(self.yPartSize*self.VyScale)
                        else: 
                            line[k]=(self.origin[1]-self.coords[c][k])/(self.yPartSize*self.VyScale)
                    else:
                        if(self.origin[1]>=self.coords[c][k]):
                            line[k]=(-1)*(self.origin[1]-self.coords[c][k])/(self.yPartSize*self.VyScale)
                        else: 
                            line[k]=(self.coords[c][k]-self.origin[1])/(self.yPartSize*self.VyScale)#                 for z value , differentiate from the 1,2 and 3 vertex and take the z from faces list
                x0,y0,z0,x1,y1,z1=line
                if(axis==1):
#                     y0t,z0t,y1t,z1t=0.0,0.0,0.0,0.0

                    y0t=y0*cos_t-z0*sin_t
                    z0t=y0*sin_t+z0*cos_t
                    
                    y1t=y1*cos_t-z1*sin_t
                    z1t=y1*sin_t+z1*cos_t
                    
                    y0,z0,y1,z1=y0t,z0t,y1t,z1t
                if(axis==2):
                    x0t=z0*sin_t+x0*cos_t
                    z0t=z0*cos_t-x0*sin_t
                     
                    x1t=z1*sin_t+x1*cos_t
                    z1t=z1*cos_t-x1*sin_t
                    
                    
                    x0,z0,x1,z1=x0t,z0t,x1t,z1t
                    
                if(axis==0):
                    x0t,y0t,x1t,y1t=0.0,0.0,0.0,0.0
                    
                    x0t=x0*cos_t-y0*sin_t
                    y0t=y0*cos_t+x0*sin_t
                
                    x1t=x1*cos_t-y1*sin_t
                    y1t=y1*cos_t+x1*sin_t
                
                    x0,y0,x1,y1=x0t,y0t,x1t,y1t
                
                [x0,y0,z0]=self.getRealCoord([x0,y0,z0])
                [x1,y1,z1]=self.getRealCoord([x1,y1,z1])    
                
                canvas.coords(lists[index],x0,y0,x1,y1)
                tempArr[c]=[x0,y0,z0,x1,y1,z1]
                
                points=canvas.coords(lists[index])
                points=self.lineClip(self.viewxMin,self.viewyMin,self.viewxMax,self.viewyMax,points[0],points[1],points[2],points[3])
                if(points[0] is None):
   
                    canvas.itemconfig(lists[x],fill='yellow')
                    tempArr[c]=[x0,y0,z0,x1,y1,z1]
                        
                else:
                    canvas.coords(lists[x],points)  
                    canvas.itemconfig(lists[x],fill='black')
                    tempArr[c]=[points[0],points[1],z0,points[2],points[3],z1]
                    

                
                index=index+1
            canvas.update()
            time.sleep(0.2)     
            self.coords=tempArr            
                    
# Scaling in multiple steps
# currently works for scale greater than 1
    def scale(self,canvas,vals,steps):
#         if(vals[0]<1.0):
#             vals[0]=-vals[0]
#         if(vals[0]<1.0):
#             vals[1]=-vals[1]    
        xScale=vals[0]    
        yScale=vals[1]
        
        xPerStep=(xScale-1)/steps
        yPerStep=(yScale-1)/steps
        xscaleFinal=1.0
        yscaleFinal=1.0
        
        
        lists=canvas.find_withtag(self.cameraName)
        for s in range(steps):
            x=0
            xscaleFinal=xscaleFinal+xPerStep
            yscaleFinal=yscaleFinal+yPerStep    
            if(s==0):
                xscaleNet=xscaleFinal
                yscaleNet=yscaleFinal
            else:
                xscaleNet=xscaleFinal/(xscaleFinal-xPerStep)
                yscaleNet=yscaleFinal/(yscaleFinal-yPerStep)
                                     
            for c in range(len(self.coords)):
                canvas.coords(lists[x],self.coords[c][0],self.coords[c][1],self.coords[c][3],self.coords[c][4])
                canvas.scale(lists[x],self.origin[0],self.origin[1],xscaleNet,yscaleNet)
                points=canvas.coords(lists[x])
                
                z0=self.coords[c][2]
                z1=self.coords[c][5]
                self.coords[c]=[points[0],points[1],z0,points[2],points[3],z1]                           
            
                points=self.lineClip(self.viewxMin,self.viewyMin,self.viewxMax,self.viewyMax, points[0],points[1],points[2],points[3])
                if(points[0] is None):
   
                    canvas.itemconfig(lists[x],fill='yellow')
                    
                        
                else:
                    canvas.coords(lists[x],points)  
                    canvas.itemconfig(lists[x],fill='black')
                    

                x=x+1
            canvas.update()
            time.sleep(0.2)    
            
            
    def lineClip(self,xmin,ymin,xmax,ymax,x0,y0,x1,y1):
        ins,left,right,lower,upper = 0,1,2,4,8

        def clip(xa,ya):

            p=ins  #start with default value :inside

            # for x
            if xa<xmin:
                p|=left
            elif xa>xmax:
                p|=right

            # for y
            if ya<ymin:
                p|=lower
            elif ya>ymax:
                p|=upper
            return p


        k1 = clip(x0, y0)
        k2 = clip(x1, y1)



        while(k1|k2) != 0: 

        
            if (k1&k2) != 0:
                #             trivially reject
                return None,None,None,None

            #non-trivial case, at least one point outside window

            opt = k1 or k2 
            if opt & upper:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif opt & lower:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif opt & right:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif opt & left:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin
            else:
                raise RuntimeError('Clipping error')

            if opt == k1:
                x0, y0 = x, y
                k1 = clip(x0, y0)
            
            elif opt == k2:
            
                x1, y1 = x, y
                k2 = clip(x1, y1)
        return x0, y0, x1, y1


            