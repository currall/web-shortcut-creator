import os
import shutil
import urllib.request
from PIL import Image

def download_favicon(url, output_path, format,target_size):
    urllib.request.urlretrieve("https://www.google.com/s2/favicons?sz=64&domain_url="+url,"favicon.ico")
    favicon_path = "favicon.ico"
    
    with Image.open(favicon_path) as img:
        resized_img = img.resize(target_size, Image.ANTIALIAS)
        resized_img.save(output_path, format=format, sizes=[target_size])
    os.remove(favicon_path)