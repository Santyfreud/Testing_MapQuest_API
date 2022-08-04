#Importación de librerías necesarias:
#urllib.parse proporciona funciones para manipulación y análisis de JSON obtenidos en una respuesta HTTP:
import urllib.parse
#requests permite realizar peticiones HTTP:
import requests

#Construcción de la URL de la API:
main_api = "http://www.mapquestapi.com/directions/v2/route?"
origin = "Rome, Italy"
destination = "Frascati, Italy"
key = "gAQG3TGrxa2u2P4uR4mtkjg4oC59iOIJ"
#Uso del método urlencode() para dar formato al valor de la URL:
url = main_api + urllib.parse.urlencode({"key": key, "from": origin, "to": destination})
#print(url)

#Realizando la petición GET a la API:
#Se almacena el body de la respuesta en una variable y se le da formato json:
json_data = requests.get(url).json()
print(json_data)