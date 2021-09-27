import requests
from bs4 import BeautifulSoup
import lxml
import re
url='https://auto.hindustantimes.com/'

headers = {
        "User-Agent" :  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-languae" : "en",
    }

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")

news = soup.find_all('section',attrs={'class':'cardHolder expandObject page-view-candidate'})
top_snippet = []
for i in range(10):
    for s in news:

        start = s.find("h2").text
    
        substring = s[start].strip()
        top_snippet.append(substring)

        print(top_snippet)


