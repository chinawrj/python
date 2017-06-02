#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup

response = requests.get('http://ipo.csrc.gov.cn/infoByFileType.action?pageNo=1&temp=&fileType=1&flag=single&blockType=prepare')
soup = BeautifulSoup(response.text, "html.parser")

tableHeader = soup.find("tr", attrs={"class":"fontWeight"})
tableItems = soup.find_all("tr", attrs={"class":"typeborder"})
totalFooter = soup.find("div", attrs={"class":"page"})

totalPageCountContainer = totalFooter.span
for pageLink in totalPageCountContainer.find_all("a"):
    if "尾页" == pageLink.get_text() :
        pageLastLink = pageLink['href']
        totalPageCount = (re.findall("pageNo=(\d+)", pageLastLink))[0]
print("总页数:",  totalPageCount)

totalFooter.span.decompose() #remove span
totalCountContainer = "".join(totalFooter.get_text().split())
totalItemCount = re.findall("(\d+)条记录", totalCountContainer)
print("总数目:",  totalItemCount)

headings = [th.get_text().strip() for th in tableHeader.find_all("td")]
datasets = []
for row in tableItems:
    dataset = zip(headings, (td.get_text().strip() for td in row.find_all("td")))
    print(list(dataset))
    datasets.append(dataset)
