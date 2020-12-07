#!/usr/bin/env python3

from wand.image import Image as wi
import os.path
from os import path
import argparse

def get_arguments(): # gets arguments and files from user
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="File to be converted, (e.g. sample.pdf, apple.png, baseball.jpg)")
    parser.add_argument("-ct" , "--convert_type", dest="convert_type", help="New file type to be converted to, (e.g. png or jpg)")
    (options) = parser.parse_args()
    if not options.file:
        parser.error("[-] Please specify a file, use --help for more info.")
    elif not options.convert_type:
        parser.error("[-] Please specify a file type to be converted to, use --help for more info.")
    return options

def check_file(options): # selects settings based on user choice
    if path.exists(options.file) == True:
        file_name = options.file[:-4]
        extension_list = {"png": "png", "jpg": "jpeg"}
        file_extension = extension_list[options.convert_type]
        if file_extension == "png" or "jpeg":
            return file_name, file_extension
        else:
            print("File type to be converted to was not found or not supported. Please check the extension before trying again, (e.g. png or jpg)")
            exit()
    else: 
        print("File specified was not found. Please check the name and extension before trying again. (e.g. sample.pdf)")
        exit()

def convert_file(options, file_name, file_extension): # converts files to other formats
    while True:
        pdf = wi(filename=options.file, resolution=300)
        pdfimage = pdf.convert(file_extension)
        i=1
        for img in pdfimage.sequence:
            page = wi(image=img)
            page.save(filename=f"{file_name}{str(i)}.{options.convert_type}")
            i +=1
        break

def main(): # Main Function
    options = get_arguments()
    file_name, file_extension = check_file(options)
    convert_file(options, file_name, file_extension)

if __name__ == "__main__":
    main()