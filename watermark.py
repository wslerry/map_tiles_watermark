"""
Created on Mon Apr  8 11:09:29 2019

@author: lerryw
@description: Create watermark for map tiles.
"""

import os
from PIL import Image

#Note:Path should be directed to zoom level folder.
zoomlevel_path = r"/to/zoomlevel/folder/"
lgo = r"your_beautiful_logo_or_watermark.png"

logo = Image.open(lgo)
logoWidth = int(logo.width)
logoHeight = int(logo.height)

for root, dirs, files in os.walk(zoomlevel_path):
    for directory in dirs:
        folder_path = zoomlevel_path+'/'+directory
        for filename in os.listdir(folder_path):
            if (filename.endswith('.jpg') or filename.endswith('.png')):
                image = Image.open(folder_path + '/' + filename)
                imageWidth = int(image.width)
                imageHeight = int(image.height)
                image.paste(logo, (int((imageWidth - logoWidth)*0.5), int((imageHeight - logoHeight)*0.5)), logo)
                image.save(folder_path + '/' + filename)

print("Successful!")
