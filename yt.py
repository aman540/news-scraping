from selenium import webdriver
from bs4 import BeautifulSoup
import lxml

url='https://www.youtube.com/user/CARWALE/videos'

def main():
    driver= webdriver.Chrome()
    driver.get(url)
    content=driver.page_source.encode('utf-8').strip()
    soup=BeautifulSoup(content,'lxml')
    title=soup.find_all('a',id='video-title')
    time= soup.find_all('span',class_='style-scope ytd-grid-video-renderer')
    
    # time=time[i]
    for i in time:
        print(i.text)
    
    
    thumbnail=soup.find_all('img',class_='style-scope yt-img-shadow')
    
    link=soup.find_all('a',id='video-title')
    # for i in range(10):
    #     print(thumbnail[i].get('src'))
    
        # print("https://www.youtube.com"+link[i].get('href'))
    
    
main()    