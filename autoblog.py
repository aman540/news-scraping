from bs4 import BeautifulSoup
import requests 

 

url='https://www.autoblog.com/news/'

page=requests.get(url)



soup=BeautifulSoup(page.content,'html.parser')
news=soup.find_all("article",class_="list_record")
print(len(news))
for i in news:
    head=i.find("h6",class_="record-heading").find("span").text
    print(head)
    snippet=i.find("p",class_="subTitle hidden-tn").text
    print(snippet)
    time=i.find("span",class_="post-date").text
    print(time)
    link=i.find("a").get("href")
    print(link)
    img=i.find("img",class_="lazy img-responsive").get("data-original")[80:]
    print(img)
