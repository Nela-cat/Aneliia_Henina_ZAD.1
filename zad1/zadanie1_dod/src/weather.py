# src/weather.py
# Zadanie 1.1 - Aplikacje w chmurze
# Autor: Aneliia Henina

import requests
from dotenv import load_dotenv
import os

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

class WeatherService:
    """Usługa do pobierania pogody przez OpenWeatherMap."""
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(city: str, country: str):
        """Pobiera pogodę dla wskazanego miasta i kraju."""
        try:
            params = {
                "q": f"{city},{country}",
                "appid": WEATHER_API_KEY,
                "units": "metric",
                "lang": "pl"  
            }
            response = requests.get(WeatherService.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                "city": city,
                "country": country,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        except requests.RequestException as e:
            return {"error": f"Nie udało się pobrać pogody: {str(e)}"}