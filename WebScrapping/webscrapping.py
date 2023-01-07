
import pandas as pd  # importar las librerias
from requests import get
from bs4 import BeautifulSoup
import re
from datetime import datetime

website="https://www.worldometers.info/coronavirus/"

#vamos a utilizar el metodo get de la libreria requests
response=get(website)

#llamar a beautifulsoup para convertir a texto

#print(response)

#Extraertodo el archivo html

mysoup=BeautifulSoup(response.text, 'html.parser')

#print(mysoup.find('p'))#find specific paragrahps
#print(mysoup.find('div'))#find some divitions
#print(mysoup.find('id=p'))#find some divitions

covid = mysoup.find_all("div",class_="main_table_countries_div")#find all the divitions and classes where =main table
#print(covid)#show it in console

table_Covid = mysoup.find_all("div", class_="main_table_countries_div")#find all the divitions where id=nav-today

table_Covid = str(table_Covid)
#print(type(table_Covid))
# #changing characters inside <> into uppercase
table_Covid = re.sub(r'<.*?>', lambda g: g.group(0).upper(), table_Covid)
table_Covid

df = pd.read_html(table_Covid)[0]
df.head()
