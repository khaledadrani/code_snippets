#source: https://automatetheboringstuff.com/chapter13/
#basic reading text of pdf
import PyPDF2

pdfFileObj = open(directory / "2008_Book_GroupTheory.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(6)

print(pageObj.extractText())

#know if pdf is encrypted
pdfReader.isEncrypted

#encrypt pdf 
pdfReader.decrypt('rosebud')

#fitz pymupdf module
import fitz  

with fitz.open("my.pdf") as doc:
    text = ""
    for page in doc:
        text += page.getText()

print(text)

#fitz document object

doc = fitz.open(filename)
doc.metadata
doc.page_count

#fiz get table of content
#https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/csv2toc.py
doc.get_toc()

#fitz load page content
page = doc.load_page(0)  
page = doc[0]
text = page.getText()
text = page.get_text()

#pdf links annotations 
page.get_links()
page.annots()
page.widgets()

#pdf save page as image
pix = page.get_pixmap()
pix.save("page-%i.png" % page.number)

#pdf fitz extract and search for text
opt = ["text","blocks","words","html","dict","json"]
text = page.get_text(opt[0])

page.search_for("mupdf")



