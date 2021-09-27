import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re 
import lxml


url = 'https://auto.hindustantimes.com/'

page = requests.get(url)

time.sleep(2)

soup = BeautifulSoup(page.text, "lxml")

links=soup.find_all('section',attrs={'class':'cardHolder expandObject page-view-candidate'})
print(len(links))

for j in links:
            Statement = j.find("a").text.strip()
        #     print("Snippet:",Statement)
            Image = j.find('figure', attrs ={'class':'linkclick-candidate'}).find('img',attrs={'class':'lozad'}).get('data-src').strip()
        #     print("Images:",Image)
            Date = j.find('span').text.strip()
        #     print("Date:",Date)
            Read_more = j.find('aside', attrs={'class':'fr'}).find('a',attrs={'class':'readmore'}).get('data-url')
            news=j.find("ul",attrs={'class':'highlights'}).find('li').text.strip()
        #     print(news)
            print("Read More:",'https://auto.hindustantimes.com',Read_more,sep="")
#     print("*************************************")    
#     print("Snippet:",Statement,"Images:",Image,"Date:",Date," ","readmore:",'https://auto.hindustantimes.com',Read_more,sep="")  
     

       
        
            
        

    




