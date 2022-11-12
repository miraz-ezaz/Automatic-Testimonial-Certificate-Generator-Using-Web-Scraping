from docxtpl import DocxTemplate
import mainDic as m
import os
from docx import Document


data,field = m.studentData()

#print(data)
os.chdir("Test")
print(os.curdir)
doc = DocxTemplate("final.docx")

print(os.curdir)

fileNames = []
pages = []
#print(data)
for f in data:
    page = DocxTemplate("templete.docx")
    context = data[f]
    fName = f"{f}.docx"
    fileNames.append(fName)
    page.render(context)
    sd = doc.new_subdoc()
    sd.subdocx = page.docx
    pages.append(sd)
    print(f"File Generated-{fName}")
print(pages)
context = {"pages": pages}
doc.render(context)

doc.save("finalx.docx")