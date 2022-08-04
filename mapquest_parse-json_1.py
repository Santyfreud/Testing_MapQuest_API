#Importación de librerías necesarias:
#urllib.parse proporciona funciones para manipulación y análisis de JSON obtenidos en una respuesta HTTP:
import urllib.parse
#requests permite realizar peticiones HTTP:
import requests

#Construcción de la URL de la API:
main_api = "http://www.mapquestapi.com/directions/v2/route?"
key = "gAQG3TGrxa2u2P4uR4mtkjg4oC59iOIJ"

#Implementando funcionalidad para entrada de usuario:
while True:
    origin = input("Starting location: ")
    destination = input("Destination: ")
    #Uso del método urlencode() para dar formato al valor de la URL:
    url = main_api + urllib.parse.urlencode({"key": key, "from": origin, "to": destination})
    #Mostrando al usuario la URL de la petición:
    print("URL: {}".format(url))
    #Realizando la petición GET a la API:
    #Se almacena el body de la respuesta en una variable y se le da formato json:
    json_data = requests.get(url).json()
    #Extrayendo el valor de la key "statuscode" para comprobar el estado de la petición:
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: {} = A successful route call.\n".format(json_status))