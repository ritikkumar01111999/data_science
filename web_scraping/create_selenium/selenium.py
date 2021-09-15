#first step
#Prerequisites:
#To try out the commands and examples from this article, you must have,

#1) A Linux distribution (preferably Ubuntu) installed on your computer.
#2) Python 3 installed on your computer.
#3) PIP 3 installed on your computer.
#4) Google Chrome installed on your computer


sudo pip3 install virtualenv
mkdir -pv chrome-headless/drivers
cd chrome-headless /
virtualenv .venv
source .venv/bin/activate
pip3 install selenium


#STEP2
'''download chrome driver from te official link. before that check for the chrome version(like I ma having 93.3.....)'''
ls -lh ~/Downloads
unzip ~/Downloads/chromedriver_linux64.zip -d drivers/

#Now run the first program
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chromeOptions)
browser.get("http://linuxhint.com")
print("Title: %s" % browser.title)
browser.quit()
