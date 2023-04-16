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
    

def datatransform():
    n = 1
    # username = ["rimjhimittal", 'chandravob', 'rdotjain','askandola', 'tijilm', 'mhardik003_', 'shreeyachatzz', 'yashmittal', 'gunjeevsingh', 'anshbajaj07', 'happy2901', 'aitchessbee', 'samikm']
    
    username = ['chandravo','kyiv','sdfdghfdrewthgjgtrethj']
    df = pd.DataFrame(columns=['Name', 'Username', 'Global Rank', 'Country Rank', 'Photo', 'Rating', 'Stars', 'Number of Questions'])
    
    for k in username:
        
        try:
            
            url = "https://www.codechef.com/users/" + k
            r = requests.get(url)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            
            name = soup.find("h1", class_="h2-style").text
            
            global_rank = soup.find("a", href="/ratings/all").text
            
            country_rank = soup.find("a", href=r"/ratings/all?filterBy=Country%3DIndia").text
            
            rating_tmp = soup.find("div", class_="rating-number").text
            rating = ""
            for (i, char) in enumerate(rating_tmp):
                if char.isnumeric():
                    rating += char
                else:
                    break
            
            stars = getStars(int(rating))
            
            
            numq = soup.find("section", class_="rating-data-section problems-solved")
            numq = numq.find("div",class_="content").find("h5").text
            numq = numq[:-1]

            for i in range(len(numq)-1, 0, -1):
                if numq[i].isnumeric():
                    continue
                else:
                    numq = numq[i+1:]
                    break
            
            img=soup.find("img",class_="profileImage").attrs['src']
            
            print(name)
            print(global_rank)
            print(country_rank)
            print(rating)
            print(stars)
            print(numq)
            print(img)
            print(name," done")
            # # rank2 = ""
            # # for i in rank:
            # #     if i.isnumeric():
            # #         rank2 += i
            # #     else:
            # #         continue
            # df.loc[n, 'Username'] = k
            # df.loc[n, 'Rank'] = rank
            # df.loc[n, 'Photo'] = image
            # df.loc[n, 'Last Solved'] = last
            # df.loc[n, 'Name'] = name
            # df.loc[n, 'Number of Questions'] = int(numq)
            # n=n+1
        except:
            pass
        
    a = df.sort_values(by='Number of Questions', ascending=False)
    print(a)
    b = a.to_csv('details.csv', index=False)
    return a

datatransform()

