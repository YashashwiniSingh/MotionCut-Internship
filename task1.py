pip install beautifulsoup4
import pandas as pd
import requests
from bs4 import BeautifulSoup
wikiurl="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
df=pd.read_html(str(indiatable))
df=pd.DataFrame(df[0])
print(df.head())
data = df.drop(["Rank", "Population (2001)[3][a]"], axis=1)
data = data.rename(columns={"State or union territory": "State","Population(2011)[3]": "Population"})
print(data.head())
