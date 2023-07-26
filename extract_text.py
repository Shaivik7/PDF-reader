import PyPDF2
import re

class extract_text:
    def __init__(self):
        filename = "Peyto.pdf"
        pdf_file_obj = open(filename, "rb")

        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        num_pages = pdf_reader.numPages

        count = 0
        text = ""

        while count < num_pages:
            page_obj = pdf_reader.getPage(count)
            count += 1
            text += page_obj.extractText()