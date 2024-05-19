import requests
import json

# Your OpenWeatherMap API Key
api_key = "1716489117a1d2cf212f812df51cc396"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' 
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:  
            main_info = data['main']
            weather_info = data['weather'][0]
            print(f"Weather in {city}:")
            print(f"Temperature: {main_info['temp']}°C")
            print(f"Humidity: {main_info['humidity']}%")
            print(f"Weather Conditions: {weather_info['description']}")
        else:
            print(f"City {city} not found or API request failed. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the weather service. Error: {e}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
