# WeatherApp - Zadanie 1.1

## Autor
Aneliia Henina

## Opis projektu
Aplikacja **WeatherApp** umożliwia sprawdzenie aktualnej pogody w wybranym mieście na podstawie API OpenWeatherMap. Użytkownik może wybrać kraj i miasto z predefiniowanej listy, a aplikacja wyświetli dane pogodowe, takie jak temperatura, opis pogody, wilgotność i prędkość wiatru.

Projekt został zrealizowany w ramach zadania 1.1 z przedmiotu "Programowanie aplikacji w chmurze obliczeniowej".

## Środowisko
- Python 3.10
- FastAPI
- Uvicorn
- Jinja2
- Requests
- python-dotenv
- python-multipart

## Struktura projektu

weather-app-zadanie1.1/
├── src/
│   ├── init.py
│   ├── main.py
│   ├── weather.py
│   ├── locations.py
├── templates/
│   ├── index.html
├── static/
│   ├── style.css
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── README.md
├── zadanie1.md
├── .env



Jak uruchomić aplikację?
1. Sklonuj repozytorium:
```bash
git clone https://github.com/Nela-cat/Zad_1_Aneliia_Henina.git
cd Zad_1_Aneliia_Henina/zad1/weather-app-zadanie1.1

2. Zbuduj obraz Docker:
docker build -t weather-app-zadanie1.1 .


3. Uruchom kontener:
   docker run -d -p 8000:8000 --name weather-app-container --env-file .env weather-app-zadanie1.1
   

4. Otwórz aplikację:
   - Przejdź do http://localhost:8000 w przeglądarce.
   - Wybierz kraj i miasto, a następnie wyświetl pogodę.

5. Sprawdź logi (opcjonalnie):
      docker logs weather-app-container
   
## Szczegóły wdrożenia
- Obraz Docker: weather-app-zadanie1.1
- Rozmiar obrazu: ~163MB
- Liczba warstw: 16
- Szczegółowe informacje, kod źródłowy i zrzuty ekranu znajdują się w pliku zadanie1.md.

## Linki
- GitHub: https://github.com/Nela-cat/Zad_1_Aneliia_Henina/tree/main/zad1/weather-app-zadanie1.1
- DockerHub: https://hub.docker.com/r/nelacot/zad_1