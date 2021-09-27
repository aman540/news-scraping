from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

url='https://www.rushlane.com/category/bikes-news'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",class_='tdb_module_loop td_module_wrap td-animation-stack')

for i in news:
    head=i.find('h3',class_='entry-title td-module-title').find('a').text
    print(head)
    date=i.find('time',class_='entry-date updated td-module-date').text
    snipp=i.find("div",class_='td-excerpt').text
    thumb=i.find("div",class_="td-image-container").find('span')['style'][22:-1]
    # print(thumb)
    link=i.find("div",class_="td-image-container").find('a')['href']
    # print(link)