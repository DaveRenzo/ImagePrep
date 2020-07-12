#*****************************************************************************
#************************ Python Source Code *********************************
#******************* Copyright (C) 2020 - Dave Renzo *************************
#*****************************************************************************
#*****************************************************************************
#
# DESIGNER NAME: Dave Renzo (
#
# PROJECT NAME:  imagePrep
#
# FILENAME: ImagePrep.py
#
# DATE CREATED: 7/12/2020
#
# LICENSE: GPL3, see file COPYING for full license text
#
# ============================================================================
# Description:  traverse a directory of images and output thumbnails
#
#******************************************************************************
import os, sys
from PIL import Image
from resizeimage import resizeimage
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


input_path ='C:\\Users\\Dave\\Documents\\testPics\\'
output_path='C:\\Users\\Dave\\Documents\\testPics\\output\\'

dirContents =[]


def resizeImg(filename, xSize, ySize):
    try:
        with Image.open(input_path + filename) as im:
            im.thumbnail((xSize,ySize))
            im.save(output_path + os.path.splitext(filename)[0] +"_thumnail.jpg")
    except OSError as e:
        print("Cannot open "+filename)
    print(filename +" was converted!")


def getInputDir():
    global input_path
    input_path = open_dialog()
    print(input_path)

def getOutputDir():
    global output_path
    output_path = open_dialog()
    print(output_path)


def open_dialog():
   dirPath = filedialog.askdirectory()
   dirPath +='/'
   return dirPath
   
   
def processPhotos():
    dirContents = os.listdir(input_path)
    for root, dirs, files in os.walk(input_path):
        for filename in files:
            resizeImg(filename,256,256)
        break
    print("Done!")

#################### main() #################################################    
if __name__ == "__main__":

   
    ver_num = '0.0.1'

    root = tk.Tk()
    root.title('Look Up Table Utility '+ver_num)
    #root.geometry('270x160')

    input_button = tk.Button(root, text='Choose picture folder', command = getInputDir)
    input_button.pack()

    output_button = tk.Button(root, text='Choose output folder', command = getOutputDir)
    output_button.pack()

    start_button = tk.Button(root, text='convert images', command = processPhotos)
    start_button.pack()

    root.mainloop()





