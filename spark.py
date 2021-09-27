from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

# url='https://www.drivespark.com/photos/'
for a in range(0,100):
    url='https://www.drivespark.com/photos/?page='+str(a)

    page=requests.get(url)

    # time.sleep(2)cle

    soup=BeautifulSoup(page.content,'html.parser')

    img=soup.find_all("li",class_="photo-gallery-container-block zoomIn")
    # print((img))
    for i in img:
        link=i.find("img").get('src')
        name=i.find("span",class_='photo-gallery-container-block-link').text[39:]
        linki=i.find("a").get('href')
        # print(linki)
        # print(name)
        # print(len(link))
        print("https://www.drivespark.com"+link)