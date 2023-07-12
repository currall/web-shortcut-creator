import ico
import web
import window_creator

import os
import time
from tkinter import *
from PIL import ImageTk, Image

title = "Web Shortcut Creator"
size = [300,400]
root = Tk()

window_creator.new(root,title,size)

def preview(root,imagebox,preview_name,url_input_box,name_input_box):

    print("previewing") # debug output

    # download favicon

    url=url_input_box.get()
    ico.download_favicon(url,"assets\\web.ico","ICO",(64,64))
    ico.download_favicon(url,"assets\\web.png","PNG",(64,64))

    # update preview image & name

    img = ImageTk.PhotoImage(Image.open("assets\\web.png"))
    imagebox.configure(image = img)
    imagebox.image = img

    name=name_input_box.get()
    preview_name.configure(text=name)

    # update

    root.update()

def create(name_input_box,url_input_box,desktop,start,custom):
    print("creating") # debug output
    print(desktop.get())
    print(start.get())
    print(custom.get())
    web.new(name_input_box.get(),url_input_box.get(), desktop.get(),start.get(),custom.get())

preview_label = Label(root,text="Preview:")
preview_label.pack(anchor=W)
img = ImageTk.PhotoImage(Image.open("assets/icon.ico").resize((64, 64), Image.ANTIALIAS))
imagebox = Label(root,image=img)
imagebox.pack(pady=10)
preview_name= Label(root,text="App Name")
preview_name.pack()
    
name_label = Label(root,text="Name:")
name_label.pack(padx=2,pady=2,anchor=W)
name_input_box = Entry(root,width=30)
name_input_box.pack(padx=2,pady=2,anchor=W)

url_label = Label(root,text="URL:")
url_label.pack(padx=2,pady=2,anchor=W)
url_input_box = Entry(root,width=30)
url_input_box.pack(padx=2,pady=2,anchor=W)
#input_box.bind("<Return>", favicon_download(url))  # Bind Enter key press event

preview_button = Button(root,text="Preview",command=lambda: preview(root,imagebox,preview_name,url_input_box,name_input_box))
preview_button.pack(padx=2,pady=10,anchor=W)

desktop = IntVar()
desktop_cb = Checkbutton(root,text="Desktop",variable=desktop)
desktop_cb.pack(padx=2,anchor=W)
start = IntVar()
start_cb = Checkbutton(root,text="Start Menu",variable=start)
start_cb.pack(padx=2,anchor=W)
custom = IntVar()
custom_cb = Checkbutton(root,text="Custom Directories",variable=custom)
custom_cb.pack(padx=2,anchor=W)

create_button = Button(root,text="Create Shortcut",command=lambda: create(name_input_box,url_input_box,desktop,start,custom))
create_button.pack(padx=2,pady=10,anchor=W)

root.mainloop()



