# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:15:40 2019

@author: Manoj
"""

from wand.image import Image
import os
import pytesseract

def pdf_to_img(pdf_dir): 
    
    try:
        for pdf_file in os.listdir(pdf_dir):
            if pdf_file.endswith('.pdf'):
                with(Image(filename=pdf_file, resolution=120)) as source: 
                    images = source.sequence
                    for image in images:
                        pages = len(images)
                        for i in range(pages):
                            n = i + 1
                            image.format = 'png'
                            image.background_color = 'white'
                            image.alpha_channel = 'remove'
                            newfilename = pdf_file[:-4] + str(n) + '.png'
                            os.chdir(temp_dir)
                            Image(images[i]).save(filename=newfilename)
                            os.chdir(pdf_dir)
    except Exception as e:
        print("Error in PDF to Image conversion", e)
        return None
                    
pdf_dir = "F:\PDFs"   #Folder containing PDFs
os.mkdir('F:\img')
os.mkdir(r"F:\TXT")

temp_dir = "F:\img"   #Temporary folder to store images
text_dir = "F:\TXT"
os.chdir(pdf_dir)     #Changing current directory to PDFs directory

pdf_to_img(pdf_dir)   #Calling pdf to image method
        
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'  #Tesseract path
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'   

import PIL.Image

def extract_text(temp_dir):
    try:
        i = 0
        for file in os.listdir(temp_dir):
            if file.endswith('.png'):
            
                fn=file[:-4]+str(i)+".txt"   #Naming the files
            
                output = pytesseract.image_to_string(PIL.Image.open(file).convert("RGB"), lang='eng')
                os.chdir(text_dir)
                fh=open(fn,'w')
                fh.write(output)   #Writing the extracted text into files
                fh.close()         #Closing the files
                os.chdir(temp_dir)
        
            i += 1
    except Exception as e:
        print("Error in OCR", e)
        return None
        
os.chdir(temp_dir)
extract_text(temp_dir)   #Calling image to text extraction method

def Image1(flag):
    try:
        if(flag == 1):
            exit(0)
        elif(flag == 0):
            tempFiles=[i for i in os.listdir(temp_dir) if ".png" in i]
            for i in tempFiles:
                if os.path.exists(i):
                    os.remove(i)
                else:
                    print("The file does not exist")
        
        else:
            return None
    except:
        None

print("Do you want to save the images?")
print("If Yes, press 1 else 0")
flag = int(input("Enter: "))
os.chdir(temp_dir)
Image1(flag)   #Method to save the image or delete 
os.chdir(pdf_dir)
if not os.listdir(temp_dir) :
    os.rmdir(temp_dir)
else:    
    print("Directory is not empty")  
