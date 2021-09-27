from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

#ht auto  url

url='https://www.autocarindia.com/auto-images'

page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
link=soup.find_all("div",attrs={'class':"item"})
for i in link:
    image=i.find("img").get("src")
    name=i.find("p",class_="carousel-p").text[:-13]
    link=i.find("a").get('href')
    print(link)
    