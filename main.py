# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk() 
WIDTH, HEIGHT = 1000, 1000
root.geometry(f'{WIDTH}x{HEIGHT}')

# function to be called when mouse enters in a frame
def enter(event):
	Label(root, text = "Enter the death").pack()

# function to be called when mouse exits the frame
def exit_(event):
	exit()

# frame with fixed geometry
frame1 = Frame(root, height = HEIGHT, width = WIDTH)

# these lines are showing the
# working of bind function
# it is universal widget method
frame1.bind('<Enter>', enter)
frame1.bind('<Leave>', exit_)

frame1.pack()

mainloop()
