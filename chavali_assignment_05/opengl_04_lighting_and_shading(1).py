# This is a sample program to demonstrate OpenGL lighting and
# shading models. 
# This program also demonstrates how to create different viewports
# in OpenGL and how to handle mouse and keyboard interactions.
# Farhad Kamangar
# Mar. 2015

import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from numpy import *

Angle = 0
increment = 0
material_ambient_and_diffuse_r=0.5
material_ambient_and_diffuse_g=0.0
material_ambient_and_diffuse_b=0.3
material_specular_rgb=1
material_shininess=50
rotation_around_x=0
rotation_around_y=0
rotation_around_z=0
radius=.7
inner_radius=0.2
number_of_slices=30
number_of_inner_slices=30
rotation_direction=1
model_number=0
models=["Torus","Teapot","Sphere","Cone","Cube"]
parallel_projection=True
wire_frame=False
flat_shading=False
enable_lighting=True
light_position_x=5
light_position_y=5
light_position_z=10
eye_x=3
eye_y=3
eye_z=3
u_min=-1.5
u_max=1.5
v_min=-1.5
v_max=1.5
front=2
back=30
last_mouse_down_motion_x=0
last_mouse_down_motion_y=0
mouse_button=0
mouse_state=0
def vec(*args):
      #Function to create ctpe array
      return (GLfloat * len(args))(*args)        
def display_message(x,y,message,color=[1,0,0],font_size=24):
      #//  Fonts supported by GLUT are: 
      # GLUT_BITMAP_8_BY_13,
      # GLUT_BITMAP_9_BY_15, 
      # GLUT_BITMAP_TIMES_ROMAN_10,
      # GLUT_BITMAP_TIMES_ROMAN_24, 
      # GLUT_BITMAP_HELVETICA_10,
      # GLUT_BITMAP_HELVETICA_12, 
      # GLUT_BITMAP_HELVETICA_18. 
      lighting_mode=glGetBooleanv(GL_LIGHTING)
      glDisable(GL_LIGHTING)
      glPushAttrib(GL_COLOR_BUFFER_BIT)
      glPushAttrib(GL_CURRENT_BIT)
      glColor3f( color[0],color[1],color[2] );
      glRasterPos2f(x,y);
      for ch in message:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ctypes.c_int( ord(ch) ))
      glPopAttrib()
      glPopAttrib()
      if lighting_mode:
            glEnable(GL_LIGHTING)
      else:
            glDisable(GL_LIGHTING)      
def create_pyramid():
      glNewList(1,GL_COMPILE)
      glBegin(GL_TRIANGLES)

      glVertex3f(0,0,0)
      glVertex3f(1,1,0)
      glVertex3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(1,0,0)
      glVertex3f(1,1,0)
      
      glColor3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(0,1,0)
      glVertex3f(0.5,0.5,1)
      
      glColor3f(0,0,1)
      glVertex3f(0,1,0)
      glVertex3f(1,1,0)
      glVertex3f(0.5,0.5,1)
      
      glColor3f(1,1,0)
      glVertex3f(1,1,0)
      glVertex3f(1,0,0)
      glVertex3f(0.5,0.5,1)
      
      glColor3f(1,0,1)
      glVertex3f(1,0,0)
      glVertex3f(0,0,0)
      glVertex3f(0.5,0.5,1)
      
      
      glEnd() 
      glEndList()

def create_3d_axes():
      glNewList(2,GL_COMPILE)
      glBegin(GL_LINES)
      glColor3f(1,0,0)
      glVertex3f(0,0,0)
      glVertex3f(2,0,0)
      glEnd() 
      
      glBegin(GL_LINES)
      glColor3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(0,2,0)
      glEnd() 
      
      glBegin(GL_LINES)
      glColor3f(0,0,1)
      glVertex3f(0,0,0)
      glVertex3f(0,0,2)
      glEnd() 
      glEndList()         
def create_xyz_axis():
      lighting_mode=glGetBooleanv(GL_LIGHTING)
      glDisable(GL_LIGHTING)
      glPushAttrib(GL_LINE_BIT)
      glLineWidth(4)
      glBegin(GL_LINES)
      glColor3f(1,0,0)
      glVertex3f(0,0,0)
      glVertex3f(1,0,0)
      glColor3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(0,1,0)
      glColor3f(0,0,1)
      glVertex3f(0,0,0)
      glVertex3f(0,0,1)
      glEnd()
      display_message(1,0,"x")
      display_message(0,1,"y")
      glPushMatrix()
      glTranslate(0,0,1)
      display_message(0,0,"z")
      glPopMatrix()          
      glPopAttrib()
      if lighting_mode:
            glEnable(GL_LIGHTING)
      else:
            glDisable(GL_LIGHTING)      
def create_torus(radius, inner_radius, number_of_slices, number_of_inner_slices):


      vertices = []
      normals = []
      #glClearColor(1, 1, 1, 1)
      glColor3f(1, 0, 0)
            
      nis=number_of_inner_slices+1;
      #print("nis=",nis)
      u_step = 2 * pi / (number_of_slices)
      v_step = 2 * pi / (nis - 1)
      u = 0.
      for i in range(number_of_slices+1):
            temp_x = cos(u)
            temp_y = sin(u)
            v = 0.
            for j in range(nis):
                  d = (radius + inner_radius * cos(v))
                  x = d * temp_x
                  y = d * temp_y
                  z = inner_radius * sin(v)
              
                  nx = temp_x * cos(v)
                  ny = temp_y * cos(v)
                  nz = sin(v)
              
                  vertices.append([x, y, z])
                  normals.append([nx, ny, nz])
                  v += v_step
            u += u_step

      # Create a list of triangle.
      #glNewList(3,GL_COMPILE)
      glBegin(GL_TRIANGLES)
      indices = []
      
      for i in range(number_of_slices):
            for j in range(nis - 1):
                  p = i * nis + j
                  # Create first triangle
                  glNormal(normals[p][0],normals[p][1],normals[p][2])
                  glVertex(vertices[p][0],vertices[p][1],vertices[p][2])
                  glNormal(normals[p + nis][0],normals[p + nis][1],normals[p + nis][2])
                  glVertex(vertices[p + nis][0],vertices[p + nis][1],vertices[p + nis][2])
                  glNormal(normals[p + nis + 1][0],normals[p + nis + 1][1],normals[p + nis + 1][2])
                  glVertex(vertices[p + nis + 1][0],vertices[p + nis + 1][1],vertices[p + nis + 1][2])
                  
                  
                  # Create second triangle
                  glNormal(normals[p][0],normals[p][1],normals[p][2])
                  glVertex(vertices[p][0],vertices[p][1],vertices[p][2])
                  glNormal(normals[p + nis + 1][0],normals[p + nis + 1][1],normals[p + nis + 1][2])
                  glVertex(vertices[p + nis + 1][0],vertices[p + nis + 1][1],vertices[p + nis + 1][2])
                  glNormal(normals[p + 1][0],normals[p + 1][1],normals[p + 1][2])
                  glVertex(vertices[p + 1][0],vertices[p + 1][1],vertices[p + 1][2])           
                  
      glEnd()
      #glEndList()
def display_help_text():
      global Angle
      global increment
      global material_ambient_and_diffuse_r
      global material_ambient_and_diffuse_g
      global material_ambient_and_diffuse_b
      global material_specular_rgb
      global material_shininess      
      global rotation_around_x
      global rotation_around_y
      global rotation_around_z      
      global radius
      global inner_radius
      global number_of_slices
      global number_of_inner_slices
      global rotation_direction
      global parallel_projection
      global wire_frame
      global flat_shading
      global enable_lighting
      global light_position_x
      global light_position_y
      global light_position_z
      global model_number
      global eye_x
      global eye_y
      global eye_z
      global u_min
      global u_max
      global v_min
      global v_max
      global front
      global back      
      ######################################################
      # Text viewport      
      w=glutGet(GLUT_WINDOW_WIDTH)
      h=glutGet(GLUT_WINDOW_HEIGHT)
      lighting_mode=glGetBooleanv(GL_LIGHTING)
      #glPushAttrib(GL_ENABLE_BIT)
      glDisable(GL_LIGHTING)
      matrix_mode=glGetIntegerv(GL_MATRIX_MODE)
      glEnable(GL_SCISSOR_TEST)
      glScissor(int(0.02*w),int(0.02*h),int(0.4*w),int(0.96*h))
      glClearColor(1,1,1,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glPushMatrix()
      glLoadIdentity()     
      glOrtho(0,1,0,1,1,10)      
      gluLookAt(0,0,3,0,0,0,0,1,0)
      
      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glViewport(int(0.05*w),int(0.05*h),int(0.4*w),int(0.9*h))
      distance_between_test_lines=.05
      text_margin=0.01
      line_number=0
      #Display radius (size)
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"a/A: Radius/Size of the object = {0:.2f}".format(radius))      
      if flat_shading:
            temp_text='glShadeModel(GL_FLAT)'
      else:
            temp_text='glShadeModel(GL_SMOOTH)'
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"f: flat shading is {0:s}".format(temp_text))
      #Display inner_radius
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"i/I: Inner radius = {0:.2f}".format(inner_radius))
      #Display number_of_inner_slices
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"k/K: Number of inner slices = {0:d}".format(number_of_inner_slices))
      #Display number_of_slices
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"l/L: Number of slices = {0:d}".format(number_of_slices))
      #Display model name
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"m/M: Current model is : {0:s}".format(models[model_number]))
      #Display Enable_lighting
      if enable_lighting:
            temp_text='glEnable(GL_LIGHTING)'
      else:
            temp_text='glDisable(GL_LIGHTING)'
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"o: Lighting mode is: {0:s}".format(temp_text))
      #Display front palne
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"p/P: Front plane = {0:.2f}".format(front))
      #Display material ka and kd
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"r/R: Material ambient and diffuse (R) = {0:.2f}".format(material_ambient_and_diffuse_r))
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"g/G: Material ambient and diffuse (G) = {0:.2f}".format(material_ambient_and_diffuse_g))
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"b/B: Material ambient and diffuse (B) = {0:.2f}".format(material_ambient_and_diffuse_b))
      #Display material ks
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"s/S: Material specular coefficient (RGB) = {0:.2f}".format(material_specular_rgb))      
      #Display material shininess
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"n/N: Material shininess = {0:d}".format(material_shininess))   
      #Display wireframe
      if wire_frame:
            temp_text='glPolygonMode(GL_LINE)'
      else:
            temp_text='glPolygonMode(GL_FILL)'
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"w: Wireframe  mode is: {0:s}".format(temp_text))
      #Display rotation around x
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"x/X: Rotation around x = {0:d} degrees".format(rotation_around_x))
      #Display rotation around y
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"y/Y: Rotation around y = {0:d} degrees".format(rotation_around_y))
      #Display rotation around z
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"z/Z: Rotation around z = {0:d} degrees".format(rotation_around_z))
      # Display eye location
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"Eye location: ({0:.2f}, {1:.2f}, {2:.2f})".format(eye_x,eye_y,eye_z))      
      # Display umin, umax, vmin ,vmax
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"umin, umax, vmin, vmax: ({0:.2f}, {1:.2f}, {2:.2f}, {3:.2f})".format(u_min,u_max,v_min,v_max))
      # Display eye location
      line_number=line_number+1
      display_message(text_margin,1-line_number*distance_between_test_lines,"Light location: ({0:.2f}, {1:.2f}, {2:.2f})".format(light_position_x,light_position_y,light_position_z))                   
      glPopMatrix()
      glMatrixMode(GL_PROJECTION)
      glPopMatrix()
      #glPopAttrib()
      glMatrixMode(matrix_mode)
      if lighting_mode:
            glEnable(GL_LIGHTING)
      else:
            glDisable(GL_LIGHTING)

def display():
      global Angle
      global increment
      global material_ambient_and_diffuse_r
      global material_ambient_and_diffuse_g
      global material_ambient_and_diffuse_b
      global material_specular_rgb
      global material_shininess      
      global rotation_around_x
      global rotation_around_y
      global rotation_around_z      
      global radius
      global inner_radius
      global number_of_slices
      global number_of_inner_slices
      global rotation_direction
      global parallel_projection
      global wire_frame
      global flat_shading
      global enable_lighting
      global light_position_x
      global light_position_y
      global light_position_z
      global model_number
      global eye_x
      global eye_y
      global eye_z
      global u_min
      global u_max
      global v_min
      global v_max
      global front
      global back      
      display_help_text()
      glMatrixMode(GL_MODELVIEW)
      glLoadIdentity()
#       glEnable(GL_DEPTH_TEST)
      #glDisable(GL_CULL_FACE)
#       if enable_lighting:
#             glEnable(GL_LIGHTING)
#       else:
#             glDisable(GL_LIGHTING)
#       if wire_frame:
#             glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
#       else:
#             glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
#             glEnable(GL_LIGHT0)           
#             glLightfv(GL_LIGHT0, GL_POSITION, vec(light_position_x, light_position_y, light_position_z, 0))
#             glLightfv(GL_LIGHT0, GL_SPECULAR, vec(1, 1, 1, 1))
#             glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
# 
#             #glEnable(GL_LIGHT1)
#             #glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
#             #glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(1,1, 1, 1))
#             #glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))            
#         
#             glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(material_ambient_and_diffuse_r, material_ambient_and_diffuse_g, material_ambient_and_diffuse_b, 1))
#             glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(material_specular_rgb, material_specular_rgb, material_specular_rgb, 1))
#             glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, material_shininess) 
#             glEnable(GL_NORMALIZE)
#             if flat_shading:                 
#                   glShadeModel(GL_FLAT)
#             else:
#                   glShadeModel(GL_SMOOTH)      
      w=glutGet(GLUT_WINDOW_WIDTH)
      h=glutGet(GLUT_WINDOW_HEIGHT)
     
      ######################################################
      # Parallel viewport      
      glScissor(int(0.43*w),int(0.51*h),int(0.56*w),int(0.47*h))
      glClearColor(.2,.2,.2,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glOrtho(u_min,u_max,v_min,v_max,front,back)
      gluLookAt(eye_x,eye_y,eye_z,0,0,0,0,1,0)
      glMatrixMode(GL_MODELVIEW)         
      glViewport(int(0.43*w),int(0.51*h),int(0.56*w),int(0.47*h))
      glPushMatrix()      
      glLoadIdentity()
#       glRotated(Angle,0,1,0)
      glRotated(rotation_around_z,0,0,1)
      glRotated(rotation_around_y,0,1,0)
      glRotated(rotation_around_x,1,0,0)
      if model_number==0:
            create_torus(radius, inner_radius, number_of_slices, number_of_inner_slices)
      elif model_number==1:
            glutSolidTeapot(radius)
      elif model_number==2:
            glutSolidSphere(radius,number_of_slices, number_of_inner_slices)
      elif model_number==3:
            glutSolidCone(radius,inner_radius,number_of_slices, number_of_inner_slices)
      elif model_number==4:
            glutSolidCube(radius)      
      glPopMatrix()
      display_message(0,1.5,"Parallel",[1,1,0])

      create_xyz_axis()
  
      ########################################################
      ## Perspective viewport      
      glScissor(int(0.43*w),int(0.02*h),int(0.56*w),int(0.47*h))
      glClearColor(0.2,0.2,0.2,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(u_min,u_max,v_min,v_max,front,back)
      gluLookAt(eye_x,eye_y,eye_z,0,0,0,0,1,0)
      glMatrixMode(GL_MODELVIEW)         
      glViewport(int(0.43*w),int(0.02*h),int(0.56*w),int(0.47*h))
      glPushMatrix()      
      glLoadIdentity()
#       glRotated(Angle,0,1,0)
      glRotated(rotation_around_z,0,0,1)
      glRotated(rotation_around_y,0,1,0)
      glRotated(rotation_around_x,1,0,0)
      if model_number==0:
            create_torus(radius, inner_radius, number_of_slices, number_of_inner_slices)
      elif model_number==1:
            glutSolidTeapot(radius)
      elif model_number==2:
            glutSolidSphere(radius,number_of_slices, number_of_inner_slices)
      elif model_number==3:
            glutSolidCone(radius,inner_radius,number_of_slices, number_of_inner_slices)
      elif model_number==4:
            glutSolidCube(radius)    
      glPopMatrix()
      
      display_message(0,1.5,"Perspective",[1,1,0])
      create_xyz_axis()
      
      #glEnable(GL_LIGHTING)
      glFlush()
      glutSwapBuffers()                 
      glScissor(0,0,w,h)
      glClearColor(1,1,1,0)
      glClear(GL_COLOR_BUFFER_BIT)
      
      glLoadIdentity()
#       glRotated(Angle,0,1,0)
#       Angle = Angle + increment


def keyHandler(Key, MouseX, MouseY):
      global increment
      global material_ambient_and_diffuse_r
      global material_ambient_and_diffuse_g
      global material_ambient_and_diffuse_b
      global material_specular_rgb
      global material_shininess      
      global rotation_around_x
      global rotation_around_y
      global rotation_around_z      
      global radius
      global inner_radius
      global number_of_slices
      global number_of_inner_slices
      global rotation_direction
      global parallel_projection
      global wire_frame
      global flat_shading
      global enable_lighting
      global model_number
      global models
      global front
      print("keyHandler")
      if Key == b'a':
            radius=radius-0.1
            if radius<0.1:
                  radius=0.1
      elif Key == b'A':
            radius=radius+0.1
      elif Key == b'f':
                        flat_shading= not flat_shading
                        #set_camera()
                        display()        
      elif Key == b'i':
            inner_radius=inner_radius-0.1
            if inner_radius<0.1:
                  inner_radius=0.1
      elif Key == b'I':
            inner_radius=inner_radius+0.1      
      elif Key == b'k':
            number_of_inner_slices=number_of_inner_slices-1
            if number_of_inner_slices<3:
                  number_of_inner_slices=3
            print("number_of_inner_slices=",number_of_inner_slices)
      elif Key == b'K':
            number_of_inner_slices=number_of_inner_slices+1
            print("number_of_inner_slices=",number_of_inner_slices)
      elif Key == b'l':
            number_of_slices=number_of_slices-1
            if number_of_slices<3:
                  number_of_slices=3
            print("number_of_slices=",number_of_slices)
      elif Key == b'L':
            number_of_slices=number_of_slices+1
            print("number_of_slices=",number_of_slices)
      elif Key == b'm':
            model_number=(model_number-1)%len(models)
      elif Key == b'M':
            model_number=(model_number+1)%len(models)
      elif Key == b'p':
            front=front-0.1
            if front <0.1:
                  front=0.1
      elif Key == b'P':
            front=front+0.1
      elif Key == b'r':
            material_ambient_and_diffuse_r=material_ambient_and_diffuse_r-0.1
            if material_ambient_and_diffuse_r<0:
                  material_ambient_and_diffuse_r=0
      elif Key == b'R':
            material_ambient_and_diffuse_r=material_ambient_and_diffuse_r+0.1
            if material_ambient_and_diffuse_r>1:
                  material_ambient_and_diffuse_r=1
      elif Key == b'r':
            material_ambient_and_diffuse_r=material_ambient_and_diffuse_r-0.1
            if material_ambient_and_diffuse_r<0:
                  material_ambient_and_diffuse_r=0
      elif Key == b'R':
            material_ambient_and_diffuse_r=material_ambient_and_diffuse_r+0.1
            if material_ambient_and_diffuse_r>1:
                  material_ambient_and_diffuse_r=1
      elif Key == b'g':
            material_ambient_and_diffuse_g=material_ambient_and_diffuse_g-0.1
            if material_ambient_and_diffuse_g<0:
                  material_ambient_and_diffuse_g=0
      elif Key == b'G':
            material_ambient_and_diffuse_g=material_ambient_and_diffuse_g+0.1
            if material_ambient_and_diffuse_g>1:
                  material_ambient_and_diffuse_g=1
      elif Key == b'b':
            material_ambient_and_diffuse_b=material_ambient_and_diffuse_b-0.1
            if material_ambient_and_diffuse_b<0:
                  material_ambient_and_diffuse_b=0
      elif Key == b'B':
            material_ambient_and_diffuse_b=material_ambient_and_diffuse_b+0.1
            if material_ambient_and_diffuse_b>1:
                  material_ambient_and_diffuse_b=1
      elif Key == b's':
            material_specular_rgb=material_specular_rgb-0.1
            if material_specular_rgb<0:
                  material_specular_rgb=0
      elif Key == b'S':
            material_specular_rgb=material_specular_rgb+0.1
            if material_specular_rgb>1:
                  material_specular_rgb=1
      elif Key == b'n':
            material_shininess = material_shininess - 1
            if material_shininess < 0:
                  material_shininess=0
      elif Key == b'N':
            material_shininess=material_shininess+1
            if material_shininess > 127:
                  material_shininess=127

      elif Key == b'd':
            rotation_direction=(rotation_direction+1)%3
      #elif Key == b's':
            #increment = increment - 1
            #print ("Slowing Down")
            #if increment < 0:
                  #increment=0
                  #print ("Stopped")
      #elif Key == b'S':
            #increment=increment+1
            #print ("Speeding Up")
      elif Key == b'o':
                  enable_lighting= not enable_lighting
                  #set_camera()
                  display()
      elif Key == b'p':
            parallel_projection= not parallel_projection
            #set_camera()
            display()
      elif Key == b'w':
            wire_frame= not wire_frame
            #set_camera()
            display()
      elif Key == b'q' or Key == b'Q':
            print ("Bye")
            sys.exit()
      elif Key == b'x':
            rotation_around_x=rotation_around_x-1
      elif Key == b'X':
            rotation_around_x=rotation_around_x+1
      elif Key == b'y':
            rotation_around_y=rotation_around_y-1
      elif Key == b'Y':
            rotation_around_y=rotation_around_y+1
      elif Key == b'z':
            rotation_around_z=rotation_around_z-1
      elif Key == b'Z':
            rotation_around_z=rotation_around_z+1
      sys.stdout.flush()
      display()

def timer(dummy):
      display()
      glutTimerFunc(30,timer,0)
def reshape(w, h):
      print ("Width=",w,"Height=",h)
def mouse_click(button,state, x,y):
      global last_mouse_down_motion_x
      global last_mouse_down_motion_y
      global mouse_button
      global mouse_state
      last_mouse_down_motion_x=x
      last_mouse_down_motion_y=y
      mouse_button=button
      print(button,state, x,y)
def mouse_down_motion(x,y):
      global rotation_around_x
      global rotation_around_y
      global rotation_around_z      
      global last_mouse_down_motion_x
      global last_mouse_down_motion_y
      global mouse_button
      global light_position_x
      global light_position_y
      global light_position_z
      global eye_x
      global eye_y
      global eye_z
      if mouse_button==GLUT_LEFT_BUTTON:
            if abs(x-last_mouse_down_motion_x)>1:
                  light_position_x= light_position_x+0.1*(x-last_mouse_down_motion_x)

            if abs(y-last_mouse_down_motion_y)>1:
                  light_position_y= light_position_y-0.1*(y-last_mouse_down_motion_y)

      if mouse_button==GLUT_RIGHT_BUTTON: 
            if abs(x-last_mouse_down_motion_x)>1:
                  eye_x= eye_x+0.1*(x-last_mouse_down_motion_x)
            if abs(y-last_mouse_down_motion_y)>1:
                  eye_y= eye_y-0.1*(y-last_mouse_down_motion_y)        
      last_mouse_down_motion_x=x
      last_mouse_down_motion_y=y
def mouse_passive_motion(x,y):
      pass
      #print("Mouse passive motion: ",x,y)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(800, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"OpenGL Lighting and Shading Demo")
glClearColor(0,0,0,0)
glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS);

glutDisplayFunc(display)
glutKeyboardFunc(keyHandler)
glutTimerFunc(300,timer,0)
glutReshapeFunc(reshape)
glutMouseFunc(mouse_click)
glutMotionFunc(mouse_down_motion)
glutPassiveMotionFunc(mouse_passive_motion)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
create_pyramid()
create_3d_axes()
#create_torus(radius, inner_radius, number_of_slices, number_of_inner_slices)
glutMainLoop()

