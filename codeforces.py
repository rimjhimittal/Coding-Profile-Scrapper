import requests
import pandas as pd
from bs4 import BeautifulSoup

usernames =["Chandravo","tourist"]

for user in usernames:
    url="https://codeforces.com/profile/"+user
    r=requests.get(url)
    htmlContent=r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    
    rank = soup.find("div", class_="user-rank").text
    print(rank)
    
    image_div=soup.find("div",class_="title-photo")
    # print(image_div)
    image = image_div.find("img")['src']
    print(image)
    
    rating_all = soup.find_all("ul")
    rating_ul=rating_all[3]
    rating_li=rating_ul.find("li")
    rating_span=rating_li.find("span")
    print(rating_li)