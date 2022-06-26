import requests
from bs4 import BeautifulSoup

url = 'https://go.drugbank.com/covid-19#drugs'

r = requests.get(url)

htmlContent = r.content

# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')

#print(soup.prettify)  #print more readable if using prettify

title = soup.title

#print(title) #title print or tag

#print(type(title.string)) #tell name of attribute type (Navigational String)

#print(type(soup)) #BeautifulSoup

paras = soup.find_all('p') #search paragraph
#print (paras)

aas = soup.find_all('a') #search anchor tag
#print (aas)

#print (soup.find('p')) #find single thing if not use all or first element

print (soup.find('p'){'a':})

