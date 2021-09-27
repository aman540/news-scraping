from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

#ht auto  url
url='https://www.bikewale.com/news/'

page=requests.get(url)
#delay time req by 2 sec
time.sleep(2)
#parsering the url
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify)
news=soup.find_all("li",class_='post-content article-content')
print(len(news))
for i in news:
    head=i.find("a")['title']
    link=i.find("a")['href']
    # print("https://www.bikewale.com"+link)
    img=i.find("a").find("img").get('data-original')
    date=i.find("div",class_='article-date').text[61:-57]
    snipp=i.find("div",class_='font14 line-height skin-txt--black').text[:-15]
    print(date)