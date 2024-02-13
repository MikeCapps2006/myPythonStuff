import PyPDF2
import re

f = open('Find_the_Phone_Number.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)

page_one = pdf_reader.pages[0]

for n in range(1, 17):
    page = pdf_reader.pages[n]
    text = page.extract_text()
    regex_pattern = r'\d\d\d\D\d\d\d\D\d\d\d\d'
    phone_number = re.search(regex_pattern, text)
    if phone_number:
        print(phone_number.group())
    else:
        pass