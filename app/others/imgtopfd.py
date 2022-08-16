# Python3 program to convert image to pfd
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import Image
import os

imge = Image.open('Output.gif')
im = imge.convert('RGB')
im.save('out1.pdf')

# storing image path
# img_path = "C:/Users/Admin/Desktop/GfG_images/do_nawab.png"

# storing pdf path
# pdf_path = "C:/Users/Admin/Desktop/GfG_images/file.pdf"

# opening image
# image = Image.open(img_path)

# # converting into chunks using img2pdf
# pdf_bytes = img2pdf.convert(image.filename)

# # opening or creating pdf file
# file = open(pdf_path, "wb")

# # writing pdf files with chunks
# file.write(pdf_bytes)

# # closing image file
# image.close()

# # closing pdf file
# file.close()

# # output
# print("Successfully made pdf file")
# S