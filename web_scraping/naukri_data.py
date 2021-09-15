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
Link=[]
for page in range(1,20): #first 50 pages of the naukri search
    driver.get("https://www.naukri.com/business-analyst-jobs-in-bangalore-"+str(page))
    timeDelay = random.randrange(0, 5)
    time.sleep(timeDelay) 
    soup=BeautifulSoup(driver.page_source, 'html.parser')#returns html of the page
    for i in soup.findAll(attrs={'class':"jobTuple bgWhite br4 mb-8"}):
        for j in i.findAll(attrs={'class':"title fw500 ellipsis"}):
            Link.append(j.get('href')) #stores all the link of the job postings
Link=pd.DataFrame(Link)
Link.to_csv('new_data.csv')
print(Link)