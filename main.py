#!/usr/bin/env python3

from wand.image import Image as wi
import os.path
from os import path

def get_file():
    while True:
        file = input(f"What is the pdf name: ")
        if path.exists(file) == True:
            file_name = file[:-4]
            file_extension = file[-4:]
            return file, file_name, file_extension
        else:
            continue

def convert_file(file, file_name, file_extension):
    pdf = wi(filename=file, resolution=300)
    pdfimage = pdf.convert("png")
    i=1
    for img in pdfimage.sequence:
        page = wi(image=img)
        page.save(filename=f"{file_name}{str(i)}.png")
        i +=1

def main():
    file, file_name, file_extension = get_file()
    convert_file(file, file_name, file_extension)

if __name__ == "__main__":
    main()