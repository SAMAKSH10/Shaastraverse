import requests
import json
import sys

API_KEY = "66442a8d43deec66e5537b7a3ba39ab9"
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        # Parsing the weather data and displaying the forecast
        print(f"Weather forecast for {city}:")
        temperature = weather_data["main"]["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        print(f"Temperature: {temperature} K")
        print(f"Description: {weather_desc}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        sys.exit(1)
    except (KeyError, IndexError, json.JSONDecodeError):
        print("Failed to parse weather data.")
        sys.exit(1)

if __name__ == "__main__":
    
    city_name=input("Enetr The City Name")

    if len(city_name) < 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)

    get_weather(city_name)
