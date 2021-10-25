import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
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

list1=[]
link=[]
link2=[]
key=[]
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
#for page in range(1,20): #first 50 pages of the naukri search
driver.get("https://www.recruiter.com/careers/")
timeDelay = random.randrange(0, 5)
time.sleep(timeDelay) 
soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
data = soup.find('div', {'class': "careers__inner-new"})
#print(data)
rows = data.findChildren(['ul'])
#print(rows)

for row in rows:
    listu=row.findChildren(['li'])
    li=list1.append(listu)
    linkkk=row.find_all('a')
    for i in linkkk:
        link.append(i.get('href'))
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
dictonary={}
power=[]
for data in link2[:25]:
    if "https://can.recruiter.com/" in data:
        power.append(data[33:-1])
        driver.get(data)
        timeDelay = random.randrange(0, 5)
        time.sleep(timeDelay) 
        soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
        kewword=soup.find_all("p",{"class":"font-weight-bold"})
        for i in kewword:
            key.append(i.text)
            value=i.text
            dictonary.update({"{}".format(data[34:-1]): "{}".format(value[15:])})


    else:
        pass

#print(power)
#print(dictonary)
json_object = json.dumps(dictonary, indent = 4) 
print(json_object)
