# Relizene Weather

[![PyPI](https://img.shields.io/pypi/v/relizene-weather?color=blue)](https://pypi.org/project/relizene-weather/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

> Simple and user-friendly Python module for fetching weather forecasts via the OpenWeatherMap API.
> Supports location validation using Nominatim and request caching.
> Features advanced city validation logic. For full details, refer to the documentation in the Doc folder.
> 
> Key Features Highlighted:
> Easy Integration: Straightforward access to OpenWeatherMap API.
> 
> Location Validation: Ensures accurate city/region names via Nominatim.
> 
> Caching: Reduces API calls by caching frequent requests.
> 
> Robust Validation: Sophisticated checks for city name accuracy and geolocation.
> 
> Documentation: Comprehensive guides and details available in the Doc folder.

---

## 🚀 Fast start

### Installation
> ```bash
> pip install relizene-weather

Usage example
> ```bash
> python
> from relizene_weather import main
>

### Inicialization with API-key
> ```bash
> fetcher = main.run_city(appid="You_Key_OPENWEATHERMAP")
> 
> recieve weather for city (automatic validation via Nominatim)
> weather = main.run_city(city = "London")
> print(weather)
>

## 📚 Documentation. Basic methods
> ```bash
> run_cuty(location: str) -> WeatherData –  returns an object with weather data. 
> run_geo(location: str) -> str – returns an object with weather data. 
> 
> Examples with coordinates
> python
> weather = main.run_geo(lat=55.75, lon=37.61)
>

## 🛠️ For developers
> ```bash
> Source installation 
> bash
> git clone https://github.com/relizene/Relizene_weather.git
> cd Relizene_weather
> pip install -e .
>

## Tests run
> bash
> pytest tests/ -v
>

## 🤝 How to help project
> ```bash
> Fork repository
> Create branches: git checkout -b feature/new-feature
> Commit changes: git commit -m 'Add awesome feature'
> Push branches: git push origin feature/new-feature
> Create Pull Request

## 📜 License
Distributed under a license  MIT. more detailed in LICENSE.

## 📧 Contacts
Reliz unknouwn – telegramm@Valodyaaa – email@vovaegorov689@gmail.com
project in GitHub: https://github.com/relizene/Relizene_weather
