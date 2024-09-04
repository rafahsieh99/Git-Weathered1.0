import argparse
import requests
import json
import csv

def parse_arguments():
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación.")
    parser.add_argument("location", type=str, help="Nombre de la ciudad y país (Ej: Asuncion-PY)")
    parser.add_argument("-format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida")
    return parser.parse_args()

def get_weather_data(location):
    api_key =  # Reemplaza con tu propia API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric", "lang": "es"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_weather(data):
    if data:
        temp = round(data['main']['temp'], 2)
        feels_like = round(data['main']['feels_like'], 2)
        location = data['name']
        description = data['weather'][0]['description']
        
        print(f"Clima en {location}:")
        print(f"Temperatura: {temp}°C")
        print(f"Sensación térmica: {feels_like}°C")
        print(f"Condiciones: {description}")
        print(f"Humedad: {data['main']['humidity']}%")

def print_as_json(data):
    temp = round(data['main']['temp'], 2)
    feels_like = round(data['main']['feels_like'], 2)
    
    data_to_print = {
        'ubicacion': data['name'],
        'temperatura': temp,
        'sensacion_termica': feels_like,
        'descripcion': data['weather'][0]['description'],
        'humedad': data['main']['humidity']
    }
    print(json.dumps(data_to_print, indent=2, ensure_ascii=False))

def print_as_csv(data):
    temp = round(data['main']['temp'])
    feels_like = round(data['main']['feels_like'])
    location = data['name']
    description = data['weather'][0]['description']
    
    print(f"ubicacion,temperatura,sensacion_termica,descripcion,humedad")
    print(f"{location},{temp},{feels_like},{description},{data['main']['humidity']}")

def main():
    args = parse_arguments()
    weather_data = get_weather_data(args.location)

    if weather_data:
        if args.format == "json":
            print_as_json(weather_data)
        elif args.format == "csv":
            print_as_csv(weather_data)
        else:
            print_weather(weather_data)
    else:
        print("Error: No se pudo encontrar la ubicación especificada o hubo un problema con la solicitud.")

if __name__ == "__main__":
    main()
