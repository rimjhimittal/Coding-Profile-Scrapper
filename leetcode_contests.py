import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.leetcode.com/contest/"
r=requests.get(url)
htmlContent=r.content
soup = BeautifulSoup(htmlContent,'html.parser')

contests=soup.find_all('div',class_='truncate')
print(len(contests))
for i in contests:
    print(i)
    print()
    print()
    print()
    print()

contest1=contests[0].text
contest2=contests[1].text
print(contest1,contest2)
# print(len(table))