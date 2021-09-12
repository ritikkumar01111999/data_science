from bs4 import BeautifulSoup as bs4
from requests import get

def data(i):
    page='https://twitter.com/search?q=%23{}&src=typeahead_click'
    page1=page.format(i)
    #print(page)
    load=get(page1)
    data=bs4(load.text,'html.parser')
    print(data)

    
i=input('enter the job you want with a hastag')
data(i)