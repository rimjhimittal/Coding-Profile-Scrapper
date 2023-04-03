import requests
import pandas as pd
from bs4 import BeautifulSoup

def getStars(n):
    if (n<=1399): 
        return "1 star"
    elif (n<=1599):
        return "2 star"
    elif (n<=1799):
        return "3 star"
    elif (n<=1999):
        return "4 star"
    elif (n<=2199):
        return "5 star"
    elif (n<=2499):
        return "6 star"
    else:
        return "7 star"

url="https://www.codechef.com/users/chandravo"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

# name = soup.find("h1", class_="h2-style").text
# print(name)

# global_rank = soup.find("a", href="/ratings/all").text
# print(global_rank)

# country_rank = soup.find("a", href=r"/ratings/all?filterBy=Country%3DIndia").text
# print(country_rank)

# rating_tmp = soup.find("div", class_="rating-number").text
# rating = ""
# for (i, char) in enumerate(rating_tmp):
#     if char.isnumeric():
#         rating += char
#     else:
#         continue
# print(rating)
# print(getStars(int(rating)))


# img=soup.find("img",class_="profileImage").attrs['src']
# print(img)

numq = soup.find("section", class_="rating-data-section problems-solved")
numq = numq.find("div",class_="content").find("h5").text
numq = numq[:-1]

for i in range(len(numq)-1, 0, -1):
    if numq[i].isnumeric():
        continue
    else:
        numq = numq[i+1:]
        break
print(numq)