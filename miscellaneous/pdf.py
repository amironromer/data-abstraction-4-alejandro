import PyPDF2 as p
file = open("sample.pdf", "rb")
pd = p.PdfFileReader(file)

x = pd.getPage(0)

print(x.extractText())