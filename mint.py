import requests
from bs4 import BeautifulSoup

url='https://www.livemint.com/auto-news/'

page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')

news=soup.find_all("div",class_="listtostory clearfix")
print(len(news))
for i in news:
    link=i.find("a").get('href')
    # print("https://www.livemint.com/auto-news"+link)
    img=i.find("img").get("src")
    snippet=i.find("img").get("alt")
    head=i.find("h2",class_="headline").find("a").text[11:-9]
    time=i.find("span",class_="fl date").text
    print(time)