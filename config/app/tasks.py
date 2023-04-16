
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import User, leetcode_acc,codechef_acc
import requests
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
    

@shared_task
def scrape_leetcode():
    users = User.objects.all()
    accounts=[]
    for user in users:
        if (leetcode_acc.objects.filter(user=user).exists()):
            # print(leetcode_acc.objects.filter(user=user).first().username)
            accounts.append(leetcode_acc.objects.filter(user=user).first())
    # print(usernames)
    for account in accounts:
        k=account.username
        try:
            url = "https://leetcode.com/" + k
            r = requests.get(url)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            rank = soup.find("span", class_="ttext-label-1 dark:text-dark-label-1 font-medium").text
            last = soup.find("span", class_="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline")
            if (last):
                last = last.text
            else:
                last="Not Solved"
            numq = soup.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1").text
            name = soup.find("div", class_="text-label-1 dark:text-dark-label-1 break-all text-base font-semibold").get_text()
            images = soup.findAll('img', class_ = "h-20 w-20 rounded-lg object-cover")
            example = images[0]
            image = example.attrs['src']
            print(name," leetcode done")
            
            account.rank=rank
            account.name=name
            account.photo_url=image
            account.last_solved=last
            account.number_of_questions=numq
            account.save()
        except:
            pass
    
    return "done"


@shared_task
def scrape_codechef():
    users = User.objects.all()
    accounts=[]
    for user in users:
        if (codechef_acc.objects.filter(user=user).exists()):
            # print(leetcode_acc.objects.filter(user=user).first().username)
            accounts.append(codechef_acc.objects.filter(user=user).first())
    # print(usernames)
    for account in accounts:
        k=account.username
        print("username is "+k)
        try:
            url = "https://www.codechef.com/users/" + k
            print(url)
            r = requests.get(url)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            name = soup.find("h1", class_="h2-style").text
            print(1)
            global_rank = soup.find("a", href="/ratings/all").text
            print(2)
            country_rank = soup.find("a", href=r"/ratings/all?filterBy=Country%3DIndia").text
            print(3)
            rating_tmp = soup.find("div", class_="rating-number").text
            rating = ""
            for (i, char) in enumerate(rating_tmp):
                if char.isnumeric():
                    rating += char
                else:
                    break
            rating = int(rating)
            print(4)
            
            stars = getStars(rating)
            print(5)
            
            numq = soup.find("section", class_="rating-data-section problems-solved")
            numq = numq.find("div",class_="content").find("h5").text
            numq = numq[:-1]
            print(6)

            for i in range(len(numq)-1, 0, -1):
                if numq[i].isnumeric():
                    continue
                else:
                    numq = numq[i+1:]
                    break

            img=soup.find("img",class_="profileImage").attrs['src']
            print(name," codechef hahahahhah done")
            
            account.name=name
            account.global_rank=global_rank
            account.country_rank=country_rank
            account.rating=rating
            account.stars=stars
            account.photo_url=img
            account.number_of_questions=numq
            account.save()
            print(7)
        except:
            print("lauda bc")
            pass
    
    return ""


