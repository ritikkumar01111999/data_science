from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import random


def openDriver(link):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    driver = webdriver.Chrome(
        executable_path="./drivers/chromedriver")

    # for page in range(1,20): #first 50 pages of the naukri search
    div = driver.get(link)
    print(div)
    return driver


# list1 = []


# key = []


# get links
def getCategories(rows):
    categories = []
    for row in rows:
        find_li = row.findChildren(['li'])
        # li = list1.append(listu)
        links = row.find_all('a')
        for i in links:
            categories.append(i.get('href'))

    return categories


def getData(link):

    driver = openDriver(link)
    timeDelay = random.randrange(0, 5)
    time.sleep(timeDelay)

    # returns html of the page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data = soup.find('div', {'class': "careers__inner-new"})
    # print(data)
    rows = data.findChildren(['ul'])
    # print(rows)

    return getCategories(rows)


def getSubCategroies(link):
    subcategories = []
    for j in link:
        driver = openDriver(j)
        # driver.get(j)
        timeDelay = random.randrange(0, 5)
        time.sleep(timeDelay)
        # returns html of the page
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        categoryName = soup.find_all('div', {'class': "card-title"})
        for i in categoryName:
            categoryLink = soup.find_all("a")
            for j in categoryLink:
                subcategories.append(j.get('href'))

        return subcategories


def GetCatogriesData(link2):
    dictonary = {}

    for data in link2[:15]:
        if "https://can.recruiter.com/" in data:
            # power.append(data[33:-1])
            # driver.get(data)
            driver = openDriver(data)
            timeDelay = random.randrange(0, 5)
            time.sleep(timeDelay)
            # returns html of the page
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            keyword = soup.find_all("p", {"class": "font-weight-bold"})
            
            for i in keyword:
                # # key.append(i.text)
                value = i.text
                key = data.split("/")[-2].split(".")[0]
                try:
                    subCat = value.split(":")[1].strip()
                except:
                    subCat = ""
                new_category=soup.find_all("u",{"class":"get-scouted get-scouted-css"})
                valu=new_category.text
                # dictonary.update(
                #     {"{}".format(data[34:-1]): "{}".format(value[15:])})
                # d = {
                #     "value": [data[34:-1]],
                #     "cateogiries": [value[15:]],
                # }
                dictonary.update({"{}".format(valu):{"{}".format(key): "{}".format(subCat)}})
        else:
            pass

    return dictonary


def getJson(data, fileName):
    with open(f"{fileName}.json", "w")as f:
        json.dump(data, f)
    print(f"done {fileName}")


def main():
    # step 1 ; open driver
    driver = openDriver("https://can.recruiter.com/careers/")
    # step 2 ; get categoires
    categoires = getData("https://can.recruiter.com/careers/")
    # step 3 : get subcateogires
    subCat = getSubCategroies(categoires)
    # step 4: get categoies data
    data = GetCatogriesData(subCat)
    # step 5: make json
    getJson(data, "data")


main()
