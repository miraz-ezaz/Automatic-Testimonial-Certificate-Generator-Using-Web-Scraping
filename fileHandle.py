import csv

def itemsList():
    file_handle = open(r"rollCSV.csv", "r", encoding="utf-8-sig")
    csv_reader = csv.DictReader(file_handle)
    items = {}
    x = 1
    for row in csv_reader:
        items[f"{x:03}"] = row
        x +=1
    file_handle.close()
    return items

