from OpenGL.Tk import *
from tkinter import Frame


b=Opengl(height=100,width=100)
root = b.master
f = Frame(root, width=100, bg='blue')
f.pack(side='left', fill='y')
b.pack(side='right', expand=1, fill='both')

root.mainloop()