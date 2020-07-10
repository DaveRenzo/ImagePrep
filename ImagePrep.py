import os, sys
from PIL import Image
from resizeimage import resizeimage
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


input_path ='C:\\Users\\Dave\\Documents\\testPics\\'
output_path='C:\\Users\\Dave\\Documents\\testPics\\output\\'

dirContents =[]

#size = (128, 128)

#for infile in sys.argv[1:]:
#    outfile = os.path.splitext(infile)[0] + ".thumbnail"
#    if infile != outfile:
#        try:
#            with Image.open(infile) as im:
#                im.thumbnail(size)
#                im.save(outfile, "JPEG")
#        except OSError:
#            print("cannot create thumbnail for", infile)

def resizeImg(filename):
    try:
        with Image.open(input_path + filename) as im:
            im.thumbnail((256,256))
            im.save(output_path + os.path.splitext(filename)[0] +"_thumnail.jpg")
    except OSError as e:
        print("Cannot open "+filename)
    print(filename +" was converted!")

#dirContents = os.listdir(input_path)


#for root, dirs, files in os.walk(input_path):
#    for filename in files:
#        resizeImg(filename)
#    break

#################### main() #################################################    
if __name__ == "__main__":

   
    ver_num = '0.0.1'

    root = tk.Tk()
    root.title('Look Up Table Utility '+ver_num)
    #root.geometry('270x160')

    input_button = tk.Button(root, text='Choose picture folder')
    input_button.pack()

    output_button = tk.Button(root, text='Choose output folder')
    output_button.pack()

    start_button = tk.Button(root, text='convert images')
    start_button.pack()

    root.mainloop()





