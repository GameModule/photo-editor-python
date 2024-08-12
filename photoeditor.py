from PIL import Image,ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut= '/editedImgs'   #assigned input and output paths to variables

for filename in os.listdir(path):
    img=Image.open(f"{path}/{filename}")  #opens the image saved in the imgs folder

    edit=img.filter(ImageFilter.SHARPEN).convert('L') #sharpens the image and converts it to greyscale

    factor = 2
    enhancer= ImageEnhance.Contrast(edit)
    edit=enhancer.enhance(factor)   #enhances the contrast of the image

    clean_name=os.path.splitext(filename)[0]   #selects the 'root' part of file (name without extension of file)

    edit.save(f'.{pathOut}/{clean_name}_edited.png') #takes the root part of filename from input folder, and adds edited.png to the name in output