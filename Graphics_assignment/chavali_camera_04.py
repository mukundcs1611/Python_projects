#Chavali,Srinivas Mukund 
#1001-242-350
#2016-04-20
#Assignment_04

from chavali_graphics_04 import cl_world


class camera:
    ob_world=[]
    noOfCams=0
    cameraNames=[]
    projTypes=[]
    vrp=[]
    vpn=[]
    vup=[]
    prp=[]
    W=[]
    s=[]  
    canvasas=[]
      
    def __init__(self):
        pass
        
#         self.canvas=canvas
        
#         return self.load_camera()
        
    def load_camera(self):
        filename='cameras_04.txt' 
        infile=open(filename)
      
        for line in infile.readlines():
            tokens=line.split()
            if(len(tokens)==1):
                
                self.noOfCams=self.noOfCams+1
                        
            else :    
                firstToken=tokens[0]
                if(firstToken=='i') : #nameofcamera
                    self.cameraNames.append(tokens[1])
                elif(firstToken=='t'):
                    self.projTypes.append(tokens[1])
                elif(firstToken=='r'):
                    self.vrp.append([tokens[1],tokens[2],tokens[3]])
                elif(firstToken=='n'):
                    self.vpn.append([tokens[1],tokens[2],tokens[3]])
                elif(firstToken=='u'):
                    self.vup.append([tokens[1],tokens[2],tokens[3]])
                elif(firstToken=='p'):
                    self.prp.append([tokens[1],tokens[2],tokens[3]])
                elif(tokens[0]=='w'):
                    self.W.append({'umin':tokens[1],'umax':tokens[2],'vmin':tokens[3],'vmax':tokens[4],'nmin':tokens[5],'nmax':tokens[6]})
                elif(tokens[0]=='s'):
                    self.s.append({'xmin':tokens[1],'ymin':tokens[2],'xmax':tokens[3],'ymax':tokens[4]})    
                     
        
        for i in range(self.noOfCams):
            graphicObj=cl_world()
#                 graphicObj.defWorld(self.canvas, self.s[i], self.W[i], self.vup[i], self.vpn[i], self.vrp[i], self.prp[i])
            self.ob_world.append(graphicObj)
        
        
        return self.ob_world,self    
    
    
    def cameraDefWOrld(self):
        pass
    