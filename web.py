import os
import urllib.request
import sys

import ico

if len(sys.argv) == 3:
    shortcut = sys.argv[1]
    url = sys.argv[2]
else:
    shortcut = input("Enter Shortcut Name: ")
    url = input("Enter URL: ")

with open("dirs.txt","r") as f:
    #directory = (f.readlines()[0]+"\\").replace("\n","")
    directories = f.readlines()
with open("icondir.txt","r") as f:
    icon_dir = (f.readlines()[0]+"\\").replace("\n","")

favicon_url = "http://www.google.com/s2/favicons?domain="+url

os.makedirs(icon_dir ,exist_ok=True)
ico.resize_favicon(url, icon_dir+shortcut+".ico", (64,64))

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