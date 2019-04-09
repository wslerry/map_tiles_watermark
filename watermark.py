# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:25:23 2019

@author: lerryw
"""

import os
from PIL import Image

'''
NOTE: Map tiles dimension usually 256 X 256 px, so recommended watermark should be smaller than that.
'''

#Note:Path should be directed to tile folder.
tiles_path = r"path/to/map/tiles/folder"
logo = Image.open(r"path/to/your/beautiful/logo.png")
logoWidth = int(logo.width)
logoHeight = int(logo.height)

for root, dirs, files in os.walk(tiles_path):
    for directory in dirs:
        folder_path = tiles_path + '/' + directory
        for fd_root, fd_dirs, fd_files in os.walk(folder_path):
            for fd_directory in fd_dirs:
                fd_path = folder_path + '/' + fd_directory
                for filename in os.listdir(fd_path):
                    if (filename.endswith('.jpg') or filename.endswith('.png')):
                        
                        image = Image.open(fd_path + '/' + filename)
                        imageWidth = int(image.width)
                        imageHeight = int(image.height)
                        
                        #position
                        topleft = 0,0
                        topright = int(imageWidth - logoWidth),0
                        bottomleft = 0,int(imageHeight - logoHeight)
                        buttomright = int(imageWidth - logoWidth), int(imageHeight - logoHeight)
                        center = int((imageWidth - logoWidth)*0.5), int((imageHeight - logoHeight)*0.5)
                        
                        image.paste(logo, topleft, logo)
                        image.save(fd_path + '/' + filename)
                        print("Added watermark to " + fd_path + '/' + filename)

print("Successful!")
