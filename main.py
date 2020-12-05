#!/usr/bin/env python3

from wand.image import Image as wi
import os.path
from os import path

def get_file():
    while True:
        file = input(f"What is the pdf name: ") # Gets the file name from the user
        if path.exists(file) == True: # Checks if the file exists
            file_name = file[:-4]
            file_extension = file[-4:]
            return file, file_name, file_extension
        else: # Runs else statment if file does not exist
            print("File was not found. Please check the name and extension before trying again. (e.g. sample.pdf)")
            continue

def convert_file(file, file_name, file_extension):
    while True:
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