from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from numpy import *
from OpenGL.raw.GLUT import glutPostRedisplay
id=0
number_of_points=10
Angle = 45
Incr = 1
def create_points():
      #print("create_points")
      glPointSize(4)
      glBegin(GL_POINTS)
      glColor3f(1,1,0) # Set color to red
#       for angle in arange(0,2*pi,2*pi/number_of_points):
      glVertex3f(cos(0),sin(0),0)
               

      glEnd()
      glutPostRedisplay()
      point_number=1
      for angle in arange(0,2*pi,2*pi/number_of_points):
            display_message(cos(angle),sin(angle),str(point_number))
            point_number=point_number+1
def create_polygon():
      glBegin(GL_POLYGON)
      for angle in arange(0,2*pi,2*pi/number_of_points):
            glVertex3f(cos(angle),sin(angle),0)
      glEnd()
def set_camera():
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glOrtho(-2,2,-2,2,1,30)
      gluLookAt(0,0,10,0,0,0,0,1,0)
def display_message(x,y,message,font_size=24):
      #print("display_message")
      glColor3f( 1,1,0 );
      glRasterPos2f(x,y);
 
      for ch in message:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int( ord(ch) ))            

def display():
      global id
      global Angle
      global Incr      
      #print("display id=",id)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_MODELVIEW)
      glLoadIdentity()
      glRotated(Angle,0,1,0)
      if id==0:
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
            glDisable(GL_CULL_FACE)
            glColor3f(1,0,0) # Set color to red
            create_polygon()
            create_points()
            display_message(0,1.5,"GL_FRONT_AND_BACK")
            display_message(0,1.2,"GL_LINE")            
            display_message(0,-1.5,"Hit any key")

     
      elif id==1:
            glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
            glDisable(GL_CULL_FACE)
            glColor3f(1,0,0) # Set color to red
            create_polygon()
            create_points()
            display_message(0,1.5,"GL_FRONT_AND_BACK")
            display_message(0,1.2,"GL_FILL")            
            display_message(0,-1.5,"Hit any key")

      elif id==2:
            glPolygonMode(GL_FRONT,GL_FILL)
            glEnable(GL_CULL_FACE)
            glCullFace(GL_BACK); 
            display_message(0,0,"Polygon") 
            glColor3f(1,0,0) # Set color to red
            create_polygon()
            create_points()
            display_message(0,1.5,"GL_FRONT")
            display_message(0,1.2,"GL_FILL") 
            
            display_message(0,-1.5,"Hit any key")
      elif id==3:
            glPolygonMode(GL_FRONT,GL_FILL)
            glEnable(GL_CULL_FACE)
            glCullFace(GL_BACK); 
            display_message(0,0,"Polygon") 
            glColor3f(1,0,0) # Set color to red
            create_polygon()
            glCullFace(GL_FRONT); 
            display_message(0,0,"Polygon") 
            glColor3f(0,0,1) # Set color to blue
            create_polygon()            
            create_points()
            display_message(0,1.5,"Different Colors")
            display_message(0,1.2,"Using CullFace") 
            
            display_message(0,-1.5,"Hit any key")          
      else:
            id=0
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
            display_message(0,0,"Polygon")            
            create_polygon()
            create_points()
            display_message(0,1.5,"GL_FRONT_AND_BACK")
            display_message(0,1.2,"GL_LINE")            
            display_message(0,-1.5,"Hit any key")
           
      Angle = Angle + Incr
      glutSwapBuffers()
      glFlush()
def keyHandler(Key, MouseX, MouseY):
      global id
      global Incr   
      print("keyHandler")

      if Key == b'n' or Key == b'N':
            id=id+1
      elif Key == b'f' or Key == b'F':
            print ("Speeding Up")
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
            id=id+1
            
      display()
def timer(Dummy):
      glutPostRedisplay()
      glutTimerFunc(30,timer,0)


def main():
      glutInit(sys.argv)
      glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
      glutInitWindowSize(600, 600)
      glutInitWindowPosition(40, 40)          
      glutCreateWindow(b"PyOpenGL Demo")
      glutDisplayFunc(display)
      glutKeyboardFunc(keyHandler)
      glutTimerFunc(0,timer,0)
      set_camera()
      glutMainLoop()

if __name__ == "__main__":
      main()

