from bs4 import BeautifulSoup
import requests 

url='https://www.thedrive.com/news'

page=requests.get(url)



soup=BeautifulSoup(page.content,'html.parser')
news=soup.find_all("div",class_="main-page-module regular clearfix")
print(len(news))
for i in news:
    head=i.find("h2",class_="title").text
    print(head)
    date=i.find("span",class_="date").text
    print(date)
    link=i.find("a",class_="linkable").get("href")
    print("https://www.thedrive.com"+link)
    img=i.find("div",class_="article-image").get("data-image")
    print("https://www.thedrive.com"+img)
    snippet=i.find("span",class_="dek").text
    print(date)