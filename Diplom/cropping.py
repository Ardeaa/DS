# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:33:46 2021

@author: User
"""
from PIL import Image
from tifffile import imread
import numpy
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

startx = 1025
starty = 1025
stopx = 1249
stopy = 1249
startfile = 1
stopfile = 36
for i in range(startfile,stopfile+1):
        image = Image.open("AerialImageDataset/train/images/vienna"+str(startfile)+".tif")
        cropped_image = image.crop((startx,starty,stopx,stopy))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/images2/vienna"+str(startfile)+"-1.tif")
        print("img1"+str(startfile)+" saved")
        cropped_image = image.crop((startx+1200,starty+1200,stopx+1200,stopy+1200))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/images2/vienna"+str(startfile)+"-2.tif")
        print("img2"+str(startfile)+" saved")
        cropped_image = image.crop((startx+3200,starty+3200,stopx+3200,stopy+3200))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/images2/vienna"+str(startfile)+"-3.tif")
        print("img3"+str(startfile)+" saved")
        cropped_image = image.crop((startx+1200,starty+3200,stopx+1200,stopy+3200))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/images2/vienna"+str(startfile)+"-4.tif")
        print("img3"+str(startfile)+" saved")
        
        #image = Image.open("AerialImageDataset/train/gt/chicago"+str(startfile)+".tif")
        img = imread("AerialImageDataset/train/gt/vienna"+str(startfile)+".tif")
        image = Image.fromarray(img)
        print(image)
        cropped_image = image.crop((startx,starty,stopx,stopy))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/gt2/vienna"+str(startfile)+"-1.tif")
        print("img1"+str(startfile)+" saved")
        cropped_image = image.crop((startx+1200,starty+1200,stopx+1200,stopy+1200))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/gt2/vienna"+str(startfile)+"-2.tif")
        print("img2"+str(startfile)+" saved")
        cropped_image = image.crop((startx+3200,starty+3200,stopx+3200,stopy+3200))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/gt2/vienna"+str(startfile)+"-3.tif")
        print("img3"+str(startfile)+" saved")
        cropped_image = image.crop((startx+1200,starty+3200,stopx+1200,stopy+3200))
        print("img"+str(startfile)+" cropped")
        image1 = cropped_image
        image1.save("AerialImageDataset/train/gt2/vienna"+str(startfile)+"-4.tif")
        print("img3"+str(startfile)+" saved")
        startfile = startfile + 1
        