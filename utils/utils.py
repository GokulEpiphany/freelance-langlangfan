from tesserocr import PyTessBaseAPI, PSM, OEM
import tesserocr
from PIL import Image
import pandas as pd
import os
from wand.image import Image as Img


#Helper class to read text using ocr
#First analyse layout and rotate if needed and extract text

def ocr_from_file_path(file_path,language):
    print("Performing OCR")
    text=""
    try:
        image = Image.open(file_path)
        text = tesserocr.image_to_text(image,lang=language)
    except Exception as e:
        print(e)
        pass
    return text


def convert_pdf_to_png(file_path,file_name):
    print("Converting pdf to png image for OCR")
    name_to_save = file_name[0:len(file_name) - 4]
    with Img(filename=full_path, resolution=300) as img:
        img.compression_quality = 99
        temp_name = file_path+'/'+name_to_save+".jpg"
        img.save(filename=temp_name)
    