import requests
from bs4 import BeautifulSoup
import re

def eliminar_figures(section):
    """Elimina todas las etiquetas <figure> dentro de una sección dada de BeautifulSoup."""
    for figure in section.find_all("figure"):
        figure.decompose()  

def calcular_media_edad(fallecimientos):
    """Calcula la media de las edades de los fallecimientos."""
    edades = [fallecido["edad"] for fallecido in fallecimientos if fallecido["edad"] is not None]
    if edades:
        return sum(edades) / len(edades)
    return 0

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
actualidad_section = soup.find("div", id="main-cur")

fallecimientos = []  
if actualidad_section:
    eliminar_figures(actualidad_section) 

    fallecimientos_dt = actualidad_section.find("dt")

    if fallecimientos_dt and "Fallecimientos" in fallecimientos_dt.text:
        fallecimientos_ul_list = fallecimientos_dt.find_all_next("ul")
        
        for ul in fallecimientos_ul_list:
            for li in ul.find_all("li"):
                texto = li.get_text(" ", strip=True)

                palabras_clave_conmemoraciones = ["aniversario", "conmemoración", "homenaje"]
                if any(palabra in texto.lower() for palabra in palabras_clave_conmemoraciones):
                    continue

                partes = texto.split(":")
                if len(partes) > 1:
                    fecha = partes[0].strip()
                    resto = partes[1].strip()
                else:
                    fecha = None
                    resto = texto

                edad = None
                edad_match = re.search(r'\((\d+)\)', resto)
                if edad_match:
                    edad = int(edad_match.group(1))
                else:
                    posibles_edades = [int(num) for num in re.findall(r'\b\d+\b', resto) if 0 < int(num) <= 150]
                    if posibles_edades:
                        edad = posibles_edades[0]

                if "," in resto:
                    nombre, profesion = resto.rsplit(",", 1)
                    nombre = nombre.strip()
                    profesion = profesion.strip()
                else:
                    nombre = resto.strip()
                    profesion = None

                fallecimientos.append({
                    "nombre": nombre,
                    "edad": edad,
                    "fecha": fecha,
                    "profesion": profesion
                })

                if "Dick Button" in nombre and "patinador sobre hielo" in texto:
                    break

            if fallecimientos[-1]["nombre"] == "Dick Button":
                break

        for fallecido in fallecimientos:
            print(fallecido)

        media_edad = calcular_media_edad(fallecimientos)
        print(f"\nLa media de edad de los fallecimientos es: {media_edad:.2f} años")

    else:
        print("No se encontró la sección de fallecimientos.")
else:
    print("No se encontró la sección de actualidad.")





