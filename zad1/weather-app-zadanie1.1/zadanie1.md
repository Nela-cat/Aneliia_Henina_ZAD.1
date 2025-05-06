# Zadanie 1.1 - Aplikacje w chmurze

## Autor
Aneliia Henina

## Opis projektu
Aplikacja WeatherApp pozwala na sprawdzenie aktualnej pogody w wybranym mieście na podstawie API OpenWeatherMap.

## Środowisko
- Python 3.10
- FastAPI
- Uvicorn
- Jinja2
- Requests
- python-dotenv
- python-multipart

## Dockerfile
Plik `Dockerfile` został zoptymalizowany zgodnie z wymaganiami zadania:
- **Optymalizacja keszowania**: Plik `requirements.txt` kopiowany jest osobno przed instalacją zależności.
- **Minimalizacja warstw**: Instalacja `curl` i czyszczenie keszu APT w одной komendzie.
- **HEALTHCHECK**: Sprawdzanie stanu kontenera za pomocą `curl -f http://localhost:8000` z 3 próbami.
- **Metadane OCI**: Dodano etykiety `LABEL` z informacjami o autorze, tytule, opisie i wersji obrazu.
- **Rozmiar obrazu**: ~163MB, dzięki użyciu `python:3.10-slim`.



# Etap 1: Instalacja zależności
FROM python:3.10-slim AS builder

# OCI Metadata
LABEL org.opencontainers.image.author="Aneliia Henina"
LABEL org.opencontainers.image.title="WeatherApp"
LABEL org.opencontainers.image.description="Weather application for Zadanie 1.1"
LABEL org.opencontainers.image.version="1.0"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

# Etap 2: Obraz finalny
FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . /app

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000 || exit 1

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
