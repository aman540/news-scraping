from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

url='https://www.zigwheels.com/news#leadform'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",class_='col-lg-4 col-sm-4 col-xs-12 zw-sl-hover')
print(len(news))
for i in news:
    img=i.find("img").get('data-gsll-src')
    link=i.find("a").get("href")
    new=i.find("a").text
    date=i.find("li",class_='clr').text
    print(date)