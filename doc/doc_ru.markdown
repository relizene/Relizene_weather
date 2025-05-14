# Relizene Weather

## Краткое описание
Python-модуль для получения прогноза погоды через OpenWeatherMap API. Основные возможности:

- 🌍 Интеллектуальная валидация городов через Nominatim
- 📍 Поиск по координатам (широта/долгота)
- 🛡️ Расширенная система обработки ошибок
- ⚡ Кеширование запросов

## Метод `run_city`
### Синтаксис
```python
run_city(city: str, appid: str, header: dict = None) -> dict
Параметры
Параметр	Тип	Обязательный	Описание
city	str	Да	Название города
appid	str	Да	API-ключ OpenWeatherMap
header	dict	Нет	Заголовки HTTP-запроса
Логика работы
Валидация названия города через Nominatim

Нормализация данных для OpenWeatherMap

Запрос к API и возврат результата

Пример:

python
from relizene_weather import run_city

response = run_city(
    city="Москва",
    appid="your_api_key_here"
)
Метод run_geo
Синтаксис
python
run_geo(lat: float, lon: float, appid: str) -> dict
Параметры
Параметр	Тип	Обязательный	Диапазон
lat	float	Да	-90.0 до 90.0
lon	float	Да	-180.0 до 180.0
appid	str	Да	-
Пример:

python
from relizene_weather import run_geo

response = run_geo(
    lat=55.7558,
    lon=37.6176,
    appid="your_api_key_here" 
)
Коды ошибок
Ошибки валидации (6xx)
Код	Сообщение
601	Найдено несколько городов с таким названием
602	Не указан параметр city
603	Город не найден
Ошибки геопозиции (7xx)
Код	Сообщение
701	Не переданы координаты
702	Некорректные координаты
Ошибки API (4xx)
Полный список: OpenWeatherMap Errors

Формат ошибки:

json
{
    "cod": "601",
    "message": "Найдено 5 городов с названием 'Москва'"
}
Рекомендации по использованию
Всегда обрабатывайте возможные ошибки:

python
try:
    result = run_city(...)
except Exception as e:
    print(f"Ошибка: {e}")
Для коммерческого использования получите собственный API-ключ на OpenWeatherMap

Актуальная версия всегда доступна через PyPI:

bash
pip install --upgrade relizene-weather
Поддержка и сотрудничество
🐞 Сообщения об ошибках: GitHub Issues

📧 Контакты: relizene.support@example.com

💡 Идеи по развитию: создавайте Pull Request