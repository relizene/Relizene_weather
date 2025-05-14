# Relizene Weather

[![PyPI](https://img.shields.io/pypi/v/relizene-weather?color=blue)](https://pypi.org/project/relizene-weather/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

> Простой и удобный Python-модуль для получения прогноза погоды через OpenWeatherMap API. 
> Поддерживает валидацию локаций через Nominatim и кеширование запросов.
> В особенности здесь реилизована сложная валдиация города. Для полной информации откройте файл из папки Doc.

---

## 🚀 Быстрый старт

### Установка
> ```bash
> pip install relizene-weather

Пример использования
> python
> from relizene_weather import main
> 
> # Инициализация с API-ключом
> fetcher = main.run_city(appid="ВАШ_КЛЮЧ_OPENWEATHERMAP")
> 
> # Получить погоду для города (автоматическая валидация через Nominatim)
> weather = main.run_city(city = "Москва")
> print(weather)

📚 Документация
Основные методы
get_weather(location: str) -> WeatherData – возвращает объект с данными о погоде.

validate_location(location: str) -> str – проверяет и нормализует название локации.

Пример с координатами
python
weather = fetcher.get_weather_by_coords(lat=55.75, lon=37.61)
🛠️ Для разработчиков
Установка из исходников
bash
git clone https://github.com/relizene/Relizene_weather.git
cd Relizene_weather
pip install -e .
Запуск тестов
bash
pytest tests/ -v
🤝 Как помочь проекту
Форкните репозиторий

Создайте ветку: git checkout -b feature/new-feature

Закоммитьте изменения: git commit -m 'Add awesome feature'

Запушьте ветку: git push origin feature/new-feature

Создайте Pull Request

📜 Лицензия
Распространяется под лицензией MIT. Подробнее в LICENSE.

📧 Контакты
Релиз Неизвестный – @relizene – relizene@example.com

Проект на GitHub: https://github.com/relizene/Relizene_weather
