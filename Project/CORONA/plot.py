import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

url='https://www.mohfw.gov.in/' 
# make a GET request to fetch the raw HTML content
web_content=requests.get(url).content
# parse the html content
soup=BeautifulSoup(web_content, "html.parser")
extract_contents=lambda row:[x.text.replace('\n','') for x in row]
stats=[]
new_cols=["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
all_rows=soup.find_all('tr') # find all table rows
for row in all_rows: 
    stat=extract_contents(row.find_all('td')) # find all data cells
    # notice that the data that we require is now a list of length 5
    if len(stat)==5: 
        stats.append(stat)
state_data = pd.DataFrame(data=stats,columns=new_cols)
# converting the 'string' data to 'int'
state_data['Confirmed']=state_data['Confirmed'].map(int)
state_data['Recovered']=state_data['Recovered'].map(int)
state_data['Deceased']=state_data['Deceased'].map(int)

plt.figure(figsize=(15,10))
plt.barh(state_data['States/UT'],state_data['Confirmed'].map(int),align='center',color='lightblue',edgecolor='blue')
plt.xlabel('No. of Confirmed cases',fontsize = 18)
plt.ylabel('States/UT',fontsize=18)
plt.gca().invert_yaxis()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Total Confirmed Cases Statewise',fontsize=18 )
for index, value in enumerate(state_data['Confirmed']):
    plt.text(value,index,str(value),fontsize=12)
plt.show()
