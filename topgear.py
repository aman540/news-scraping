from typing import Text
import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re 



url = 'https://www.team-bhp.com/news'

page = requests.get(url)

time.sleep(2)

soup = BeautifulSoup(page.text, "html.parser")

news=soup.find_all("li")
print(len(news))

for i in news:
  newss=i.find("div",class_='clearfix listHolder').find("h2").find('a').text
#   img=i.find('strong').find('img')['src']
#   # print("https://www.team-bhp.com/"+img)
#   snipp=i.find("div",class_='past_shornote').text
#   link=i.find("div",class_='fright w460 ShortNews').find('h2').find('a')['href']
  # print(newss)
