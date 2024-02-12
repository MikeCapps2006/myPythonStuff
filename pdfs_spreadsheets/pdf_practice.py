import PyPDF2

f = open('working_business_proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)

print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(page_one_text)

f.close()