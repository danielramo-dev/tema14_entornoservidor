import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titulo = soup.title.text
print(f"El título de la página es: {titulo}")

actualidad_section = soup.find("div", id="main-cur")

if actualidad_section:
    noticias = actualidad_section.find_all("li") 

    print("\n Noticias de Actualidad en Wikipedia:")
    for index, noticia in enumerate(noticias, 1):
        texto_noticia = noticia.get_text(" ", strip=True)  
        print(f"{index}. {texto_noticia}")

else:
    print("No se encontró la sección de actualidad.")
