import os
import urllib.request
import sys

import ico

def new(shortcut,url,desktop,start,custom):

    # shortcut dir

    directories = []

    if desktop or start: 
        with open("setdirs.txt","r") as f:
            set_dirs = f.readlines()
        
        if desktop:
            directories.append(set_dirs[0])
        if start:
            directories.append(set_dirs[1])

    if custom: # create shortcuts in custom directories
        with open("dirs.txt","r") as f:
            directories_file = f.readlines()
        for i in range(len(directories_file)):
            directories.append(directories_file[i])

    # icon dir

    with open("icondir.txt","r") as f:
        icon_dir = (f.readlines()[0]+"\\").replace("\n","")

    favicon_url = "http://www.google.com/s2/favicons?domain="+url

    os.makedirs(icon_dir ,exist_ok=True)
    ico.download_favicon(url, icon_dir+shortcut+".ico", "ICO",(64,64))

    for i in range(len(directories)):

        directory = directories[i].replace("\n","")+"\\"

        os.makedirs(directory ,exist_ok=True)

        with open(directory + shortcut + ".url","w") as f:

            f.write("[{000214A0-0000-0000-C000-000000000046}]\n")
            f.write("Prop3=19,2\n")
            f.write("[InternetShortcut]\n")
            f.write("IDList=\n")
            f.write("URL="+url+"\n")
            f.write("IconIndex=0\n")
            f.write("HotKey=0\n")
            f.write("IconFile="+icon_dir+shortcut+".ico\n")