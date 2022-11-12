import requests
from bs4 import BeautifulSoup
import re


url = "http://www.educationboardresults.gov.bd/index.php"

with requests.Session() as s:
    r=s.get(url)
    #print(r.text)
    sop = BeautifulSoup(r.text,"lxml")
    #print("=============")
    tt = sop.findAll("tr")[22]
    td = tt.findAll("td")[1]
    td=td.get_text()
    equation = re.sub('[a-zA-z,.:;()" "]', '', td)
    print(equation)
    x = eval(equation)
    print(x);
    value_a = equation[0]
    value_b = equation[2]

    #x = int(input("x"))
    param = {
        "sr": "1",
        "et": "1",
        "exam": "ssc",
        "year": "2021",
        "board": "barisal",
        "roll": "109502",
        "reg": "1815784908",
        " value_a": f"{value_a}",
        " value_b": f"{value_b}",
        "value_s": f"{x}",
        "button2": "Submit"
    }
    p=s.post("http://www.educationboardresults.gov.bd/result.php",data = param)
    #print(p.text)
    #q=s.get("http://www.barisalboard.org/sscsif/result")
    #print(q.text)
    soup = BeautifulSoup(p.text,"lxml")
    #print("#############################")

    #17,18,19

    result = {}


    tdt = soup.findAll("tr")
    for x in tdt:

        if len(x) == 9:
            y = x.findAll("td")
            # print((y[0].get_text()))
            # print((y[1].get_text()))
            # print((y[2].get_text()))
            # print((y[3].get_text()))
            result[str(y[0].get_text()).title().replace(" ","").replace("'","")] = str(y[1].get_text()).title()
            result[str(y[2].get_text()).title().replace(" ","").replace("'","")] = str(y[3].get_text()).title()

        if len(x) == 5:
            y = x.findAll("td")
            result[str(y[0].get_text())] = str(y[1].get_text())


print(result)





#r = requests.post(url,data=param)
#soup = BeautifulSoup(r.text, 'lxml')
#print(soup)