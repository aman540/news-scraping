from bs4 import BeautifulSoup

import requests 


url='https://www.motortrend.com/auto-news/'
page=requests.get(url)


soup=BeautifulSoup(page.content,'html.parser')
news=soup.find_all("div",class_="_3mobD")
print(len(news))
for i in news:
    head=i.find("a",class_="_22VtJ").text.strip()
    link=i.find("a",class_="_22VtJ").get("href")
    # print("https://www.motortrend.com"+link)
    img=i.find("img",class_="_33FYh").get('src')[:-4]
    time=i.find("time")
    print(img+"439:254")