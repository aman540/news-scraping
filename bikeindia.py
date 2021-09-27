from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time


url='http://bikeindia.in/news/latest_news/'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')

news= soup.find_all("article")
print(len(news))

for i in news:
    # head=i.find("h2",class_='entry-title').find('a').text.strip()
    # date=i.find("p",class_='entry-meta').find("time",class_='entry-time').text
    # snip=i.find("p",class_="").text
    imge=i.find('img')
    img=imge.get('src')

   
    # link=i.find("div",class_='entry-content').find('a').get('href').strip()
    print(img)