import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
titulo = soup.title.text
print(f"El titulo es {titulo}")