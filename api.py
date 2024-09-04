import json
import requests

def get_weather_data(location):
    api_key = "489cf306c218f90bc09f9539bd195c81"  # Reemplaza con tu API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric", "lang": "es"}
    response = requests.get(base_url, params=params)
    print(response.status_code)  # Imprime el código de estado HTTP
    print(response.json())  # Imprime el contenido de la respuesta
    if response.status_code == 200:
        return print(response.json() )
    else:
        return None


get_weather_data("Asuncion")
