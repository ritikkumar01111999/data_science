from os import replace
import pandas as pd
from pandas.core.reshape.concat import concat
from requests import get
from bs4 import BeautifulSoup

def data():
    apge='https://www.mygov.in/corona-data/covid19-statewise-status/'
    page=get(apge)
    states=[]
    confirmed_cases=[]
    discharged=[]
    death=[]
    soup=BeautifulSoup(page.content,'html.parser')
    for i in soup.findAll("div",{"class":"field field-name-field-select-state field-type-list-text field-label-above"}):
        value=i.text
        value=value.replace(i[1:11]," ")
        states.append(value)
    for i in soup.findAll("div",{"class":"field field-name-field-total-confirmed-indians field-type-number-integer field-label-above"}):
        value=i.text
        confirmed_cases.append(value)
    
    for i in soup.findAll("div",{"class":"field field-name-field-cured field-type-number-integer field-label-above"}):
        value=i.text
        discharged.append(value)

    for i in soup.findAll("div",{"class":"field field-name-field-deaths field-type-number-integer field-label-above"}):
        value=i.text
        death.append(value)    
    states=pd.DataFrame(states)
    confirmed_cases=pd.DataFrame(confirmed_cases)
    discharged=pd.DataFrame(discharged)
    death=pd.DataFrame(death)
    
    result=concat([states,confirmed_cases,discharged,death],axis=1)
    result.columns=['states','confirmed_cases','discharged','death']
    print(result)

    new_data=result.to_csv('result.csv')

data()

