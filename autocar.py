from bs4 import BeautifulSoup
import sys
import requests 
import time

url='https://www.autocarindia.com/car-news'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')
news=soup.find_all("div",class_="new-section border-bottom-dark")
print(len(news))
for i in news:
    head=i.find("h6",class_="new-heding-h6").text

    date=i.find("p",class_="pub-date-p").text[13:]
    snippet=i.find("p",class_="new-pare-p").text
    image=i.find("img").get("src")
    link=i.find("a").get("href")
    print(head)