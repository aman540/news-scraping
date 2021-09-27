import requests
from bs4 import BeautifulSoup
url="https://motoroctane.com/news"



#geting html content from site
r=requests.get(url)
htmlContent=r.content
print(htmlContent)

#Parse the html

soup= BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

#HTML tree travel

# title= soup.title
# print(title) #title 
# print(type(soup)) #beautiful soup
# print(type(title))#tags
# print(type(title.string))#navigable string

#getting title of html page
# title= soup.title
# print(title)

#geting all the paras
# paras =soup.find_all('p')
# print(paras)

#geting all the anchor
# anchors =soup.find_all('a')
# print(anchors)

#get fist element of html page
# print(soup.find('p'))

# print(soup.get_text())

#to get the link

# anchors =soup.find_all('a')
# for link in anchors:
#     print(link.get('href'))
    