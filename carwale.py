from bs4 import BeautifulSoup
import sys
import requests 
import pandas as pd
import time

url='https://www.carwale.com/news/'

page=requests.get(url)

time.sleep(2)

soup=BeautifulSoup(page.content,'html.parser')
print(soup)