#!/usr/bin/env python3

from wand.image import Image as wi

def get_file():
    pass
file = input(f"What is the pdf name: ")
print(file[-4:])
filename = file[:-4]
pdf = wi(filename=file, resolution=300)
pdfimage = pdf.convert("jpeg")
i=1

for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=f"{filename}{str(i)}.jpg")
    i +=1