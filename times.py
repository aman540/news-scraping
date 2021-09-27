from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

url='https://www.timesnownews.com/auto/bike-news'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",class_='__cat_data_list')
print(len(news))

for i in news:
    head=i.find("div",class_='__story_detail').find('a').text
    date=i.find("span",class_='__publish_status').text[11:]
    snipp=i.find("div",class_='__story_slug').text
    link=i.find("a")['href']
    image=i.find('a',attrs={'class':'__image_pod'}).find('img')['data-src']
    print(image)
