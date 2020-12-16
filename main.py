#!/usr/bin/env python3

from wand.image import Image as wi
import os.path
from os import path
import argparse

def get_arguments(): # gets arguments and files from user
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="File to be converted, (e.g. sample.pdf, apple.png, baseball.jpg).")
    parser.add_argument("-ct" , "--convert_type", dest="convert_type", help="New file type to be converted to, (e.g. png or jpg).")
    (options) = parser.parse_args()
    if not options.file:
        parser.error("[-] Please specify a file, use --help for more info.")
    elif not options.convert_type:
        parser.error("[-] Please specify a file type to be converted to, use --help for more info.")
    return options

def check_file(options): # checks if file, and file type to be converted exsits
    try:
        print(f"[+] Checking if {options.file} exsits.")
        if path.exists(options.file) == True:
            print(f"[+] File {options.file} found.")
            file_name = options.file[:-4]
            # if options.convert_type == "png" or "jpg":
            try:
                extension_list = {"png": "png", "jpg": "jpeg"}
                file_extension = extension_list[options.convert_type]
                return file_name, file_extension
            except KeyError:
                print(f"[-] File type {options.convert_type} to be converted to was not found. Please check the extension before trying again, (e.g. png or jpg).")
        else: 
            print(f"[-] File {options.file} not found. Please check the name and extension before trying again. (e.g. sample.pdf).")
            exit()
    except Exception as msg:
        report_issue(msg)


def convert_file(options, file_name, file_extension): # converts files to other formats
    try:
        print(f"[+] Converting {options.file} to {file_name}.{options.convert_type}")
        pdf = wi(filename=options.file, resolution=300)
        pdfimage = pdf.convert(file_extension)
        i=1
        for img in pdfimage.sequence:
            page = wi(image=img)
            page.save(filename=f"{file_name}{str(i)}.{options.convert_type}")
            i +=1
        print("[+] File was successfully converted.")

    except Exception as msg:
        exception_ghostscript = 'FailedToExecuteCommand `"gswin64c.exe"'
        exception_ghostscript_compare = str(msg)
        if exception_ghostscript == exception_ghostscript_compare[:38]:
            print("[-] File was not successfully converted.\n")
            print("There is an issue with ghostscript. Reinstall or download latest version and try again.")
            print("Visit: https://github.com/PeanutTheAdmin/FileConverter for install instructions.\n")
        else:
            print("[-] File was not successfully converted.")
            report_issue(msg)

def report_issue(msg):
    print(f"[BUG] {msg}\n")
    print("To report this issue go to: https://github.com/PeanutTheAdmin/FileConverter/issues")
    print("When reporting this issue include the output after [BUG]\n")

def main(): # Main Function
    options = get_arguments()
    file_name, file_extension = check_file(options)
    convert_file(options, file_name, file_extension)

if __name__ == "__main__":
    main()