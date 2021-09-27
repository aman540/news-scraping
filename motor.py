from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time
#ondrive
url='https://www.overdrive.in/news-cars-auto/1/'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",attrs={'class':'block-cell'})
print(news)

# print(news)
for o in news:
    news=o.find('h3').find('a')['title'].strip()
    image=o.find('img',attrs={'class':'lazy'}).get('data-src')
    date=o.find('span').text
    link=o.find('h3').find('a')['href']
    snippet=o.find('img',attrs={'class':'lazy'}).get("alt")
    print(snippet)
      
