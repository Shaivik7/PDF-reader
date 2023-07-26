import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("Annual_Report_2021.pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "project"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i))
    Text = PageObj.extractText()
    # print(Text)
    ReSearch = re.search(String, Text)
    print(ReSearch)



















