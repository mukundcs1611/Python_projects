#Chavali,Srinivas Mukund 
#1001-242-350
#2016-05-02
#Assignment_05

from chavali_camera_05 import *


from tkinter import Tk
from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from numpy import *
from tkinter import simpledialog 
from tkinter.constants import LEFT, END
import tkinter





    
camera = camera().load_camera()
AngleX = 0.0
Incr = 15  
AngleY = 0.0
AngleZ = 0.0

inputfile = None
v = {}
f = {}
W = {}
s = {}




def createGLUTMenus(): 

    

#     // create the menu and
#     // tell glut that "processMenuEvents" will
#     // handle the events
    menu = glutCreateMenu(processMenuEvents)

#     //add entries to our menu
    glutAddMenuEntry("Pyramid", 1)
    glutAddMenuEntry("Cow", 2)
    glutAddMenuEntry("Teapot", 3)
    

#     // attach the menu to the right button
    glutAttachMenu(GLUT_RIGHT_BUTTON)




def processMenuEvents(option):
    global inputfile
    if(option == 1):
        inputfile = 'pyramid_05.txt'
    elif(option == 2):
        inputfile = 'cow_05.txt'    
    else:
        inputfile = 'teapot_05.txt'
       
    return 1
def display_message(x, y, message):
      # print("display_message")
      glColor3f( 0,0,0 )
      glWindowPos2f(x, y)
      
      for ch in message:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(ch)))            
def drawFig():
    
    global v
    global f
    colors = [[0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]]
    glNewList(1, GL_COMPILE)
    
    
    for j in range(len(camera.figF)):
            
                for i in range(1, len(camera.figF[j]) + 1):
                    if(len(f[i]) == 3):
                        vertex1 = [v[f[i][0]][0], v[f[i][0]][1], v[f[i][0]][2]]
                        vertex2 = [v[f[i][1]][0], v[f[i][1]][1], v[f[i][1]][2]]
                        vertex3 = [v[f[i][2]][0], v[f[i][2]][1], v[f[i][2]][2]]
                        glBegin(GL_TRIANGLES)    
                        glColor3f(colors[i % 4][0], colors[i % 4][1], colors[i % 4][2])
                        drawTriangle(vertex1, vertex2, vertex3)
                        glEnd()
                        
                         
                    if(len(f[i]) == 4):
                        vertex1 = [v[f[i][0]][0], v[f[i][0]][1], v[f[i][0]][2]]
                        vertex2 = [v[f[i][1]][0], v[f[i][1]][1], v[f[i][1]][2]]
                        vertex3 = [v[f[i][2]][0], v[f[i][2]][1], v[f[i][2]][2]]
                        vertex4 = [v[f[i][3]][0], v[f[i][3]][1], v[f[i][3]][2]]
                        glBegin(GL_POLYGON) 
                        drawPolygon(vertex1, vertex2, vertex3, vertex4)
                        glEnd()

                                   
    glEndList()
def drawTriangle(v1, v2, v3):
    

#     glColor3f(0,1,0)
    glVertex3f(v1[0], v1[1], v1[2])
    glVertex3f(v2[0], v2[1], v2[2])
    glVertex3f(v3[0], v3[1], v3[2])

   
  
    
def drawPolygon(v1, v2, v3, v4):
  

  glColor3f(0, 1, 0)
  glVertex3f(v1[0], v1[1], v1[2])
  glVertex3f(v2[0], v2[1], v2[2])
  glVertex3f(v3[0], v3[1], v3[2])
  glVertex3f(v4[0], v4[1], v4[2])

    

        
       
        
        
        

def keyHandler(Key, MouseX, MouseY):
     
     if Key == b'd' :
        load_callback()
     elif Key == b'x':
         rotate('n', 'x')
     elif Key == b'X':
         rotate('positive', 'x')
     elif Key == b'y':
         rotate('n', 'y')
     elif Key == b'Y':
         rotate('positive', 'y')
     elif Key == b'z':
         rotate('n', 'z')
     elif Key == b'Z':
         rotate('positive', 'z')
     elif Key == b'q' or Key == b'Q':
            print ("Bye")
            sys.exit()   
     sys.stdout.flush()
     display()        
            
          
        
def timer(dummy):
     display()
     glutTimerFunc(30, timer, 0)

def reshape(w, h):
      print ("Width=", w, "Height=", h)
anglex=0.0
angley=0.0
anglez=0.0
def display():
      global AngleX
      global AngleY
      global AngleZ
      global anglex,angley,anglez
      global Incr
      w = glutGet(GLUT_WINDOW_WIDTH)
      h = glutGet(GLUT_WINDOW_HEIGHT)
      #      display message
#       glEnable(GL_SCISSOR_TEST)
     
      glScissor(0, 0, 1000, 50) 
      glClearColor(1, 1, 1, 0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glPushMatrix()
      glLoadIdentity()     
      glOrtho(0, 1, 0, 1, 1, 10)      
      gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)
       
      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glViewport(0, 0, 1000, 50)
        
         
      glPopMatrix()
      glMatrixMode(GL_PROJECTION)
      glPopMatrix()
      display_message(10,25, "Press right button to load file, Press d to load,Press x/X to rotate along X,Press y/Y to rotate along Y ")
      display_message(10,5,",Press z/Z to rotate along Z,Q to quit")

      glScissor (0, 0, w, h)
      glClearColor(0, 0, 0, 0)
      glClear(GL_COLOR_BUFFER_BIT)
      
      for i in range(camera.noOfCams):
          glEnable(GL_SCISSOR_TEST)
          glScissor(int(camera.s[i]['xmin'] * (w)), int(camera.s[i]['ymin'] * h), int(camera.s[i]['xmax'] * (w)), int(camera.s[i]['ymax'] * (h)))
          glClearColor(0.4, 0.4, 0.6, 0)
          glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
          glMatrixMode(GL_PROJECTION)
          glLoadIdentity()
          if(camera.projTypes[i] == 'parallel'):
              glOrtho(camera.W[i]['umin'], camera.W[i]['umax'], camera.W[i]['vmin'], camera.W[i]['vmax'], camera.W[i]['nmin'], camera.W[i]['nmax'])
          else:    
#                gluPerspective(45,1,camera.W[i]['nmin'],camera.W[i]['nmax'])
              glFrustum(camera.W[i]['umin'], camera.W[i]['umax'], camera.W[i]['vmin'], camera.W[i]['vmax'], camera.W[i]['nmin'], camera.W[i]['nmax'])
        
          gluLookAt(camera.vrp[i][0], camera.vrp[i][1], camera.vrp[i][2],  # vrp
                    camera.vpn[i][0], camera.vpn[i][1], camera.vpn[i][2],  # vpn
                    camera.vup[i][0], camera.vup[i][1], camera.vup[i][2])  # vup
          glMatrixMode(GL_MODELVIEW)    
          glViewport(int(camera.s[i]['xmin'] * (w)), int(camera.s[i]['ymin'] * (h)), int(camera.s[i]['xmax'] * (w)), int(camera.s[i]['ymax'] * (h)))
          
          glCallList(1) 
          glPushMatrix()
          glLoadIdentity()
          
#           glRotated(Angle,0,1,0)
#           glRotated(AngleZ,0,0,1)
#           glRotated(AngleY,0,1,0)
#           glRotated(AngleX,1,0,0)
          glCallList(2) 
          glPopMatrix()
          
          
#      display message
      glEnable(GL_SCISSOR_TEST)
    
      glScissor(0, 0, 1000, 50) 
      glClearColor(1, 1, 1, 0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      
      glLoadIdentity()     
      glOrtho(0, 1, 0, 1, 1, 10)      
      gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)
   
      glMatrixMode(GL_MODELVIEW)
      glViewport(0, 0, 1000, 50)
      glCallList(3) 
      glPushMatrix()
      glLoadIdentity()
      glCallList(4)    
     
      glPopMatrix()
#       glMatrixMode(GL_PROJECTION)
#       glPopMatrix()
#      
      display_message(10,25, "Press right button to load file, Press d to load,Press x/X to rotate along X,Press y/Y to rotate along Y ")
      display_message(10,5,",Press z/Z to rotate along Z,Q to quit")
      
      glutSwapBuffers()      
      glFlush()
#     
      if(anglez!=AngleZ):   
          glRotated(AngleZ,0,0,1)
      if(angley!=AngleY):    
          glRotated(AngleY,0,1,0)
      if(anglex!=AngleX):
          glRotated(AngleX,1,0,0)
      
      anglex=AngleX
      angley=AngleY
      anglez=AngleZ
#       
      
      
#       Angle = Angle + Incr
      
def rotate(direction, axis):
    global AngleX
    global AngleY
    global AngleZ
    if(axis == 'x'):
        if(direction == 'positive'):
            AngleX = AngleX + 5
           # glRotated(5, 1, 0, 0)
        else:
            AngleX = AngleX - 5
            
        
    elif(axis == 'y'):
        if(direction == 'positive'):
            AngleY = AngleY + 5
            
        else:
            AngleY = AngleY - 5
            
            
        
    else:
        if(direction == 'positive'):
            AngleZ = AngleZ + 5
            
        else:
            AngleZ = AngleZ - 5
            
        
            
def load_callback():    
        # #Write a method which reads from a file
        global inputfile
       
        infile = open(inputfile)
#        
        global v 
        global f
        global W
        global s
        vertices = 0
        faces = 0
        
#         camRef=self.master.camera
        for line in infile.readlines():
            
            tokens = line.split()  # tokens on each line
            numbers = [float(i) for i in tokens[1:len(tokens)]]
            if(len(tokens) > 0):
                firsttoken = tokens[0]
                if(firsttoken == 'v'):
                    vertices += 1      
                    v[vertices] = numbers[0:len(tokens)]
                    
                             
                elif(tokens[0] == 'f'):
                    faces += 1   
                    f[faces] = [int(i) for i in numbers[0:len(tokens)]]
        
        camera.defFig(v, f)
        drawFig()            
        

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"OpenGL Renderer")
glClearColor(1, 1, 0, 0)
glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS);

glutDisplayFunc(display)
glutKeyboardFunc(keyHandler)
glutTimerFunc(300, timer, 0)
glutReshapeFunc(reshape)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
createGLUTMenus()
# glutWireTeapot(1)
# glutMotionFunc(mouse_down_motion)
# glutPassiveMotionFunc(mouse_passive_motion)
# glMatrixMode(GL_PROJECTION)
# glLoadIdentity()
# glMatrixMode(GL_MODELVIEW)
# load_callback('pyramid_05.txt')
# drawFig()




# create_pyramid()
# create_torus(radius, inner_radius, number_of_slices, number_of_inner_slices)
glutMainLoop()

                    
