from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

# def compileAndInstallShaders ():
#   
#   program  = glCreateProgram ()
#   vertex   = glCreateShader (GL_VERTEX_SHADER)
#   fragment = glCreateShader (GL_FRAGMENT_SHADER)
#   
#   # set shader source
#   vertex_code   = """
#     
#     attribute vec2 position ;
#     attribute vec4 color    ;
#     
#     void main ()
#     {
#       gl_Position = vec4 ( position , 0.0, 1.0 ) ;
#     }
#     
#   """
#   
#   fragment_code = """
#     
#     void main ()
#     {
#       gl_FragColor = vec4 (1.0, 0.0, 1.0, 1.0) ;
#     }
#     
#   """
#   
#   glShaderSource (vertex,   vertex_code  )
#   glShaderSource (fragment, fragment_code)
#   
#   
#   # compile shaders
#   glCompileShader (vertex)
#   glCompileShader (fragment)
#   
#   glAttachShader (program, vertex)
#   glAttachShader (program, fragment)
#   glLinkProgram (program)
#   
#   #glDetechShader (program, vertex)
#   #glDetechShader (program, fragment)
#   
#   glUseProgram (program)
#   

def display ():
  glClear (GL_COLOR_BUFFER_BIT)
  
  glBegin (GL_TRIANGLES)
  glColor3f  ( 1,1, 1)
  glVertex3f (-1, 0, 0)
  glVertex3f ( 1, 0, 0)
  glVertex3f ( 0, 1, 0)
  glEnd   ()
  glFlush ()
  glutSwapBuffers ()

glutInit(sys.argv)
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow (b"PyOpenGL Demo")
glutDisplayFunc  (display)

# compileAndInstallShaders ()

glMatrixMode (GL_PROJECTION)
glLoadIdentity ()
glOrtho (-1,1,-1,1,1,10)
gluLookAt ( 0, 0,5,
            0, 0, 0,
            0, 1, 0 )
glMatrixMode (GL_MODELVIEW)
glLoadIdentity ()
glutMainLoop   ()
