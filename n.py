from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

#ht auto  url
url='https://www.timesnownews.com/auto/car-news'

page=requests.get(url)
#delay time req by 2 sec
time.sleep(2)
#parsering the url
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify)

news=soup.find_all("div",attrs={'class':'__cat_data_list'})
print(len(news))
for t in news:
    news=t.find('div',attrs={'class':'__story_detail'}).find('a').text
    snippet=t.find('div',attrs={'class':'__story_slug'}).text
    image=t.find('a',attrs={'class':'__image_pod'}).find('img')['src']
    date=t.find('span',attrs={'class':'__publish_status'}).text[-25:-1].strip()
    link=t.find('div',attrs={'class':'__story_detail'}).find('a').get('href').strip()
    print(link)

    