# src/main.py
# Zadanie 1.1 - Aplikacje w chmurze
# Autor: Aneliia Henina

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from datetime import datetime
import logging
from src.locations import LocationManager  
from src.weather import WeatherService    

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="WeatherApp - Zadanie 1.1")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Informacje o autorze i porcie
AUTHOR = "Aneliia Henina"
PORT = 8000

@app.on_event("startup")
async def startup_event():
    """Logowanie podczas uruchamiania aplikacji (Zadanie 1.1)."""
    startup_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Uruchomienie aplikacji (Zadanie 1.1): {startup_time}")
    logger.info(f"Autor: {AUTHOR}")
    logger.info(f"Port TCP: {PORT}")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    """Wyświetla formularz do wyboru kraju i miasta."""
    countries = LocationManager.get_countries()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "countries": countries, "locations": LocationManager}
    )

@app.post("/weather", response_class=HTMLResponse)
async def post_weather(request: Request, country: str = Form(...), city: str = Form(...)):
    """Przetwarza wybór lokalizacji i wyświetla pogodę."""
    if not LocationManager.is_valid_location(country, city):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "countries": LocationManager.get_countries(),
                "locations": LocationManager,
                "weather": {"error": "Nieprawidłowa lokalizacja"}
            }
        )
    weather = WeatherService.get_weather(city, country)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "countries": LocationManager.get_countries(),
            "locations": LocationManager,
            "weather": weather
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)