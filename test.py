import csv
import mainDic as m

data,fields = m.studentData()

def insert():
    file_handle = open(r"data.csv", "a+", encoding="utf-8-sig")
    csv_writer = csv.DictWriter(file_handle, fields)
    for i in data:
        csv_writer.writerow(data[i])
    file_handle.close()
