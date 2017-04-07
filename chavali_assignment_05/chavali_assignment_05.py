'''
Created on May 1, 2016

@author: chavali
'''
import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
import chavali_camera_04

# def display ():
#   glClear (GL_COLOR_BUFFER_BIT)
#   
#   glBegin (GL_TRIANGLES)
#   glColor3f  ( 1,1, 1)
#   glVertex3f (-1, 0, 0)
#   glVertex3f ( 1, 0, 0)
#   glVertex3f ( 0, 1, 0)
#   glEnd   ()
#   glFlush ()
#   glutSwapBuffers ()

Angle = 90
Incr = 1

def display():
      global Angle
      global Incr
      w=glutGet(GLUT_WINDOW_WIDTH)
      h=glutGet(GLUT_WINDOW_HEIGHT)
      glScissor (0,0,w,h)
      glClearColor(0,0,0,0)
      glClear(GL_COLOR_BUFFER_BIT)
      glEnable(GL_SCISSOR_TEST)
      glScissor(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
      glClearColor(0.4,0.4,0.6,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(-4,4,-4,4,20,100)
      gluLookAt(0,0,4,0,0,-1,0,1,0)
      glMatrixMode(GL_MODELVIEW)    
      glViewport(int(0.01*w),int(0.1*h),int(0.4*w),int(0.4*h))
      glCallList(1) 
      glPushMatrix()
      glLoadIdentity()
      glCallList(2) 
      glPopMatrix()
      glFlush()
      glutSwapBuffers() 
#       for i in range(0, chavali_camera_04.camera.noOfCams):
#           here call the glscissor the look at and different methods as below
#             hardcode camera coordinates for now
        







#       
#       glScissor (0,0,w,h)
#       glClearColor(0,0,0,0)
#       glClear(GL_COLOR_BUFFER_BIT)
#       
#     glEnable(GL_SCISSOR_TEST)
#     glScissor(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
#     glClearColor(0.4,0.4,0.6,0)
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glFrustum(-1,1,-1,1,1,30)
#     gluLookAt(0,0,3,0,0,0,0,1,0)
#     glMatrixMode(GL_MODELVIEW)    
#     glViewport(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
#     glCallList(1) 
#     glPushMatrix()
#     glLoadIdentity()
#     glCallList(2) 
#     glPopMatrix()
#       
#       glEnable(GL_SCISSOR_TEST)
#       glScissor(int(0.05*w),int(0.05*h),int(0.4*w),int(0.4*h))
#       glClearColor(0.4,0.4,0.6,0)
#       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#       glMatrixMode(GL_PROJECTION)
#       glLoadIdentity()
#       glFrustum(-1,1,-1,1,1,30)
#       gluLookAt(0,3,0,0,0,0,0,0,1)
#       glMatrixMode(GL_MODELVIEW)      
#       glViewport(int(0.05*w),int(0.05*h),int(0.4*w),int(0.4*h))
#       glCallList(1)
#       glPushMatrix()
#       glLoadIdentity()
#       glCallList(2) 
#       glPopMatrix()      
#       
#       glScissor(int(0.55*w),int(0.55*h),int(0.4*w),int(0.4*h))
#       glClearColor(0.4,0.4,0.6,0)
#       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      
#       glMatrixMode(GL_PROJECTION)
#       glLoadIdentity()
#       #glFrustum(-1,1,-1,1,1,30)
#       gluPerspective(45,.5,1,30)
#       gluLookAt(3,0,0,0,0,0,0,1,0)
#       glMatrixMode(GL_MODELVIEW)         
#       glViewport(int(0.55*w),int(0.55*h),int(0.4*w),int(0.4*h))
#       glCallList(1)  
#       glPushMatrix()
#       glLoadIdentity()
#       glCallList(2) 
#       glPopMatrix() 
#       
#       glScissor(int(0.55*w),int(0.05*h),int(0.4*w),int(0.4*h))
#       glClearColor(0.4,0.4,0.6,0)
#       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#       glMatrixMode(GL_PROJECTION)
#       glLoadIdentity()
#       glOrtho(-1,1,-1,1,1,30)
#       #glFrustum(-1,1,-1,1,1,30)
#       gluLookAt(2,2,2,0,0,0,0,1,0)
#       glMatrixMode(GL_MODELVIEW)      
#       glViewport(int(0.55*w),int(0.05*h),int(0.4*w),int(0.4*h))
#       glCallList(1)
#       glPushMatrix()
#       glLoadIdentity()
#       glCallList(2) 
#       glPopMatrix()      
#       
#       glFlush()
#       glutSwapBuffers()                 
#       
#       glLoadIdentity()
#       glRotated(Angle,0,1,0)
#       Angle = Angle + Incr


  
def keyHandler(Key, MouseX, MouseY):
      global Incr
      if Key == b'f' or Key == b'F':
            print (b"Speeding Up")
            Incr = Incr + 1
      elif Key == b's' or Key == b'S':
            if Incr == 0:
                  print ("Stopped")
            else:
                  print ("Slowing Down")
                  Incr = Incr - 1
      elif Key == b'q' or Key == b'Q':
            print ("Bye")
            sys.exit()
      else:
            print ("Invalid Key ",Key)

def timer(dummy):
      display()
      glutTimerFunc(30,timer,0)
  
def reshape(w, h):
      print ("Width=",w,"Height=",h)

b=OpenGL(height=640,width=640)       
b.glutInit(sys.argv)

glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(640,640)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"PyOpenGL Demo")
glClearColor(1,1,0,0)
# glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
# glEnable(GL_DEPTH_TEST)
# glDepthFunc(GL_LESS);

glutDisplayFunc(display)
# glutKeyboardFunc(keyHandler)
# glutTimerFunc(300,timer,0)
glMatrixMode (GL_PROJECTION)
glLoadIdentity ()
glOrtho (-1,1,-1,1,1,30)
gluLookAt ( 0, 0,10,
            0, 0, 0,
            0, 1, 0 )
glMatrixMode (GL_MODELVIEW)
glLoadIdentity ()
glutMainLoop   ()

