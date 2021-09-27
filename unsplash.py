from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

url='https://unsplash.com/images/things/car'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",class_="_1g5Lu _2gKr0")
print(len(news))
for i in news:
    image=i.find("img").get('src')
    # link=i.find("a",class_="_2Mc8_")
    print(image)
    
