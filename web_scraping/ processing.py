from os import replace
import pandas as pd 
df=pd.read_csv('result.csv')
state=[]
confirmed_cases=[]
discharged=[]
death=[]
for i in df['states']:
    value=i.replace(i[0:11]," ")
    state.append(value)

for j in df['confirmed_cases']:
    value=j.replace(j[0:17]," ")
    confirmed_cases.append(value)
    
for k in df['discharged']:
    value=k.replace(k[0:29]," ")
    discharged.append(value)
for l in df['death']:
    value=l.replace(l[0:6]," ")
    death.append(value)

state=pd.DataFrame(state)
confirmed_cases=pd.DataFrame(confirmed_cases)
discharged=pd.DataFrame(discharged)
death=pd.DataFrame(death)
result=pd.concat([state,confirmed_cases,discharged,death],axis=1)
result.columns=['state','confirmed_cases','discharged','death']
result=result.to_csv('result.csv')