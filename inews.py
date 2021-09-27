from bs4 import BeautifulSoup
import requests 

url='http://www.autonews.com/news'

page=requests.get(url)



soup=BeautifulSoup(page.content,'html.parser')
news=soup.find_all("div",class_="feature-view-mode-2-1-2-row")
print(news)
for i in news:
    img=i.find("a",class_='omnitrack').find('img').get("data-src")
    snippet=i.find('p').text
    link=i.find('a').get('href')
    # print("http://www.autonews.com"+link)
    # time=i.find("div",class_="feature-article-category-timestamp").
    # print(time)
    head=i.find("div",class_="top-stories-title").find("a").text
    