import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re 
import lxml

url='https://www.carandbike.com/videos/all'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')


vidio=soup.find_all("li")

print(vidio)

for i in vidio:
    thumbnail=i.find('img',attrs={'loading':'lazy'}).get('data-src')
    vidio=i.find('div',attrs={'class':'video-card__title h__truncate-line'}).text
    duration=i.find('div',attrs={'class':'video-card__duration'}).text
    link=i.find('a',attrs={'class':'video-card__content grid-flex grid-sb js-href-target'}).get('href')
    print("https://www.carandbike.com/videos"+link)