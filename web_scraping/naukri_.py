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
Link1=[]
Link2=[]
link1=[]
Link=[]
key_skills=[]
description=[]
#for page in range(1,20): #first 50 pages of the naukri search
driver.get("https://www.naukri.com/top-skill-jobs#topJobsSection")
timeDelay = random.randrange(0, 5)
time.sleep(timeDelay) 
soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
for i in soup.findAll(attrs={'class':"slider colspan_four collapse"}):
    for j in i.findAll(attrs={'target':"_blank"}):
        Link1.append(j.get('title')) #stores all the link of the job postings
        Link2.append(j.get('href'))
        link1.append(j.get('href'))
Link1=pd.DataFrame(Link1)
Link2=pd.DataFrame(Link2)
data=pd.concat([Link1,Link2],axis=1)
data.to_csv('new_data.csv')
link1=link1[1:2]
for k in link1:
    for l in range(1,2):
        driver.get(k+'-'+str(l))
        timeDelay = random.randrange(0, 5)
        time.sleep(timeDelay) 
        soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
        for m in soup.findAll(attrs={'class':"jobTuple bgWhite br4 mb-8"}):
            for n in m.findAll(attrs={'class':"title fw500 ellipsis"}):
                Link.append(n.get('href')) #stores all the link of the job postings
#Link=pd.DataFrame(Link)
#Link.to_csv('all_jobs.csv')

for o in Link:
    driver.get(o)
    timeDelay=random.randrange(0,5)
    time.sleep(timeDelay)
    soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
    description.append(soup.find(attrs={'class':"job-desc"}).text)
    key_skills.append(soup.find(attrs={'class':'key-skill'}).text)
    

key_skills=pd.DataFrame(key_skills)
description=pd.DataFrame(description)
demand=pd.concat([key_skills,description],axis=1)
demand.to_csv('your_demand.csv')
print(demand)
