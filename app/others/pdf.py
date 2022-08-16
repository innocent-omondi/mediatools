from pdf2docx import Converter

pdf_file = 'sample.pdf'
docx_file = 'sample.docx'


pages_list = [0]

cv = Converter(pdf_file)
cv.convert(docx_file)
# cv.convert(docx_file, pages=pages_list)
cv.close()