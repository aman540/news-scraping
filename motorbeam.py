from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

url='https://www.motorbeam.com/category/bikes/'

page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",class_='column post-column small-mb-2 large-mb-4 hor-sep-b')

for i in news:
    head=i.find('h2',class_='entry-title h4 small-mb-1').find('a').text.strip()
    link=i.find('h2',class_='entry-title h4 small-mb-1').find('a')['href'].strip()
    snipp=i.find('p').text.strip()
    date=i.find('time',class_='entry-date published').text.strip()
    imag=i.find('img')['src'].strip()
    print(imag)

