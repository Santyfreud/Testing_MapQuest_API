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
    #Solicitando entrada de usuario para las variables de origen y destino:
    #Si la entrada del usuario es "q" ó "quit", el programa terminará (se cierra el bucle while):
    origin = input("Starting location: ")
    if origin == "q" or origin == "quit":
        break
    destination = input("Destination: ")
    if destination == "q" or destination == "quit":
        break
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

        #Extrayendo más datos de la key "route":
        print("=============================================")
        print("Directions from {0} to {1}".format(origin, destination))
        print("Trip Duration: {}".format(json_data["route"]["formattedTime"]))
        print ("Kilometers: {:.2f}".format(json_data["route"]["distance"]*1.61))
        print ("Fuel used [Ltr]: {:.2f}".format(json_data["route"] ["fuelUsed"]*3.78))
        print("=============================================")

        #Mostrando al usuario los datos de la key "maneuvers":
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print("{0} ({1:.2f} km)".format(each["narrative"], each["distance"]*1.61))
            print("=============================================")

    #Agregando funcionalidades para "statuscode" != 0:
    elif json_status == 402:
        print("**********************************************")
        print("API Status: {0}. {1} Invalid user entry for one or both of the locations".format(json_status, json_data["info"]["messages"][0]))
        print("**********************************************")
    elif json_status == 611:
        print("**********************************************")
        print("API Status: {0}. {1} Missing user entry for one or both of the locations".format(json_status, json_data["info"]["messages"][0]))
        print("**********************************************")
    else:
        print("************************************************************************")
        print("For Status code: {}; see:".format(json_status))
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")