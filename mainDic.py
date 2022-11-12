import fileHandle as file
import requests
from bs4 import BeautifulSoup
import re

data = file.itemsList();


def studentData():
    dataDic = {}
    print("Collecting data.....")
    for sl in data:
        SlNo = str(sl)
        roll = data[sl]["Roll"].strip()
        reg = data[sl]['Registration'].strip()
        vil = data[sl]['Village'].strip()
        post = data[sl]['Post'].strip()
        upa = data[sl]['Upazilla'].strip()
        zilla = data[sl]['Zilla'].strip()
        ses = data[sl]['Session'].strip()
        sData = {}
        sData["SlNo"] = SlNo
        sData['Registration'] = reg
        sData['Village'] = vil
        sData['Post'] = post
        sData['Upazilla'] = upa
        sData['Zilla'] = zilla
        sData['Session'] = ses

        url = "http://www.educationboardresults.gov.bd/index.php"

        with requests.Session() as s:
            r = s.get(url)
            # print(r.text)
            sop = BeautifulSoup(r.text, "lxml")
            # print("=============")
            tt = sop.findAll("tr")[22]
            td = tt.findAll("td")[1]
            td = td.get_text()
            equation = re.sub('[a-zA-z,.:;()" "]', '', td)
            # print(equation)
            x = eval(equation)
            # print(x);
            value_a = equation[0]
            value_b = equation[2]

            # x = int(input("x"))
            param = {
                "sr": "1",
                "et": "1",
                "exam": "ssc",
                "year": "2021",
                "board": "barisal",
                "roll": f"{roll}",
                "reg": f"{reg}",
                " value_a": f"{value_a}",
                " value_b": f"{value_b}",
                "value_s": f"{x}",
                "button2": "Submit"
            }
            p = s.post("http://www.educationboardresults.gov.bd/result.php", data=param)
            # print(p.text)
            # q=s.get("http://www.barisalboard.org/sscsif/result")
            # print(q.text)
            soup = BeautifulSoup(p.text, "lxml")
            # print("#############################")

            # 17,18,19

            tdt = soup.findAll("tr")
            for x in tdt:

                if len(x) == 9:
                    y = x.findAll("td")
                    # print((y[0].get_text()))
                    # print((y[1].get_text()))
                    # print((y[2].get_text()))
                    # print((y[3].get_text()))
                    sData[str(y[0].get_text()).title().replace(" ", "").replace("'", "")] = str(y[1].get_text()).title()
                    sData[str(y[2].get_text()).title().replace(" ", "").replace("'", "")] = str(y[3].get_text()).title()

                if len(x) == 5:
                    y = x.findAll("td")
                    sData[str(y[0].get_text())] = str(y[1].get_text())
        print(f"Data Collected. Roll-{sData['RollNo']}")
        dataDic[f"Roll_{roll}_{sData['Result']}_sl_{SlNo}"] = sData
        print(sData)
    print("Data Collected Successfully")
    fileds = []
    for i in sData:
        fileds.append(i)
    return dataDic,fileds




