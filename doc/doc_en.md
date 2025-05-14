# Relizene Weather

[![PyPI](https://img.shields.io/pypi/v/relizene-weather?color=blue)](https://pypi.org/project/relizene-weather/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## Overview
Python module for weather forecasting via OpenWeatherMap API. Key features:

- 🌍 Smart city validation using Nominatim
- 📍 Geo-coordinate search support
- 🛡️ Advanced error handling system
- ⚡ Request caching

---

## `run_city` Method
### Syntax
```python
run_city(city: str, appid: str, header: dict = None) -> dict
Parameters
Parameter	Type	Required	Description
city	str	Yes	City name (any language)
appid	str	Yes	OpenWeatherMap API key
header	dict	No	Custom HTTP headers
Workflow
City validation using Nominatim

Data normalization for OpenWeatherMap

API request processing

Example:

python
from relizene_weather import run_city

response = run_city(
    city="London",
    appid="your_api_key_here"
)
run_geo Method
Syntax
python
run_geo(lat: float, lon: float, appid: str) -> dict
Parameters
Parameter	Type	Required	Valid Range
lat	float	Yes	-90.0 to 90.0
lon	float	Yes	-180.0 to 180.0
appid	str	Yes	-
Example:

python
from relizene_weather import run_geo

response = run_geo(
    lat=51.5074,
    lon=0.1278,
    appid="your_api_key_here" 
)
Error Codes
Validation Errors (6xx)
Code	Message
601	Multiple cities found with this name
602	Missing required parameter city
603	City not found
Geo Errors (7xx)
Code	Message
701	Missing coordinates
702	Invalid coordinate values
API Errors (4xx)
Full list: OpenWeatherMap Errors

Error Format:

json
{
    "cod": "601",
    "message": "Found 3 locations matching 'Paris'"
}
Usage Recommendations
Always implement error handling:

python
try:
    result = run_city(...)
except Exception as e:
    print(f"Error: {e}")
For commercial use, obtain your own API key:
OpenWeatherMap API

Keep your package updated:

bash
pip install --upgrade relizene-weather
Support & Contribution
🐞 Bug Reports: GitHub Issues

📧 Contact: relizene.support@example.com

💡 Feature Requests: Open a Pull Request

License: MIT (see LICENSE)