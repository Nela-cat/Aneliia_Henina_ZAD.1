# src/locations.py
# Zadanie 1.1 - Aplikacje w chmurze
# Autor: Aneliia Henina

class LocationManager:
    
    LOCATIONS = {
        "Poland": ["Warsaw", "Krakow", "Wroclaw", "Gdansk"],
    "Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "France": ["Paris", "Lyon", "Marseille", "Nice"],
    "Japan": ["Tokyo", "Osaka", "Kyoto", "Hiroshima"],
    "Italy": ["Rome", "Milan", "Venice", "Florence"]
    }

    @classmethod
    def get_countries(cls):
        
        return list(cls.LOCATIONS.keys())

    @classmethod
    def get_cities(cls, country: str):
        
        return cls.LOCATIONS.get(country, [])

    @classmethod
    def is_valid_location(cls, country: str, city: str):
      
        return country in cls.LOCATIONS and city in cls.LOCATIONS[country]