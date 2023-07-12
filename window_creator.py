from tkinter import *
from PIL import ImageTk, Image

def new(root,title,size):
    root.title(title)
    root.iconbitmap('./assets/icon.ico')

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - size[0] / 2)
    center_y = int(screen_height/2 - size[1] / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{size[0]}x{size[1]}+{center_x}+{center_y}')

    root.resizable(False, False) # not resizable    