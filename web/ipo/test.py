#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

response = requests.get('http://ipo.csrc.gov.cn/infoByFileType.action?pageNo=1&temp=&fileType=1&flag=single&blockType=prepare')
soup = BeautifulSoup(response.text, "html.parser")

tableHeader = soup.find("tr", attrs={"class":"fontWeight"})
tableItems = soup.find_all("tr", attrs={"class":"typeborder"})

headings = [th.get_text().strip() for th in tableHeader.find_all("td")]
datasets = []
for row in tableItems:
    dataset = zip(headings, (td.get_text().strip() for td in row.find_all("td")))
    print(list(dataset))
    datasets.append(dataset)
