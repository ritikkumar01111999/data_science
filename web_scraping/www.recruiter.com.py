'''Aim is scrap skill keyword from www.recruiter.com'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from IPython.display import clear_output
import random
from selenium.common.exceptions import NoSuchElementException
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")

#taking link in the bot
driver.get("https://www.recruiter.com/careers/")
timeDelay = random.randrange(0, 5)
time.sleep(timeDelay) 
soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
data = soup.find('div', {'class': "careers__inner-new"})
#print(data)

#required list for storing data
list1=[]
link=[]
link2=[]
key=[]
rows = data.findChildren(['ul'])
#print(rows)
for row in rows:
    listu=row.findChildren(['li'])
    li=list1.append(listu)
    linkkk=row.find_all('a')
    for i in linkkk:
        link.append(i.get('href'))
#print(link)

for j in link:
    driver.get(j)
    timeDelay = random.randrange(0, 5)
    time.sleep(timeDelay) 
    soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
    new_class=soup.find_all('div', {'class': "card-title"})
    for i in new_class:
        new_link=soup.find_all("a")
        for j in new_link:
            link2.append(j.get('href'))
#print(link2)

for data in link2[:15]:#for example taking only 15 link
    if "https://can.recruiter.com/" in data:
        driver.get(data)
        timeDelay = random.randrange(0, 5)
        time.sleep(timeDelay) 
        soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
        kewword=soup.find_all("p",{"class":"font-weight-bold"})
        key.append(kewword)
    else:
        pass
    
print(key)
