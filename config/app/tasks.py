
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import User, leetcode_acc
import requests
from bs4 import BeautifulSoup


@shared_task
def scrape():
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
            text = ""
            # for A in soup.select("/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]"):
            #     text = A.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1").getText()
            #     print(text)
            # print(soup.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]"))

            print(name," done")
            # rank2 = ""
            # for i in rank:
            #     if i.isnumeric():
            #         rank2 += i
            #     else:
            #         continue
            
            
            # df.loc[n, 'Username'] = k
            # df.loc[n, 'Rank'] = rank
            # df.loc[n, 'Photo'] = image
            # df.loc[n, 'Last Solved'] = last
            # df.loc[n, 'Name'] = name
            # df.loc[n, 'Number of Questions'] = int(numq)
            
            # n=n+1
            
            account.rank=rank
            account.name=name
            account.photo_url=image
            account.last_solved=last
            account.number_of_questions=numq
            account.save()
        except:
            pass
    
    return "done"