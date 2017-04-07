#Chavali,Srinivas Mukund 
#1001-242-350
#2016-04-20
#Assignment_04
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog


from chavali_widgets_04 import *
from chavali_graphics_04 import *
from chavali_camera_04 import *

def close_window_callback(root):
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()


ob_root_window = Tk()
ob_root_window.protocol("WM_DELETE_WINDOW", lambda root_window=ob_root_window: close_window_callback(root_window))
# ob_world=cl_world()
#invoke camera and get ob_world array 

ob_world,camera= camera().load_camera()
cl_widgets(ob_root_window,ob_world,camera)

ob_root_window.mainloop()    
    

