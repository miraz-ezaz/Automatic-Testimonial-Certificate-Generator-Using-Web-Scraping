from docxtpl import DocxTemplate
import mainDic as m
import os
from docx import Document


data,field = m.studentData()

#print(data)
os.chdir("Files")
print(os.curdir)
doc = DocxTemplate("templete.docx")

fileNames = []
#print(data)
for f in data:
    context = data[f]
    fName = f"{f}.docx"
    fileNames.append(fName)
    doc.render(context)
    doc.save(fName)
    print(f"File Generated-{fName}")
