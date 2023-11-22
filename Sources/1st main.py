from PyPDF2 import PdfReader

pdf = PdfReader("./data/test.pdf")
pages = pdf.pages
text = ""
words = []

for page in pages:
    text += page.extract_text()

words = text.split()
print(words)