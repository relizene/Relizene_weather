import requests
from settings.settings import configuration, configuration_2
import copy
from settings.validator import ValidateMeta





class City_api(metaclass=ValidateMeta):
    """Класс для обработки и вызовы апи на сайт Openweathermap. Поиск происходит
    по названию города."""
    def __init__(self, city=None, header=None, appid=None):
        self.city = city # Инициализация города, но перед созданием проходит валидация.
        self.header = header # Инициализация отпечатка владельца, его данные.
        self.appid = appid # если пользователь имеет свой api ключ, и хочет вызвать апи сам.
    
           
    def run(self):
        """Вызов функции, который делает запрос о погоде через Api по имени города"""
        params = configuration()
        params = copy.deepcopy(params)
        url = 'https://api.openweathermap.org/data/2.5/weather'   
        if self.city:
            params['q'] = self.city
        else:
            return None # крайние случаи, если валидатор вернулся с ошибкой и не создается нужный конфиг, БЕЗОПАСНОСТЬ.
        if self.appid:
            params['appid'] = self.appid
        if self.header:
            params['header'] = self.header
        s = requests.Session() #создание сесси для каждого апи вызова.
        response = s.get(url, params=params)
        result = response.json()
        return result
 

class Geo_api():
    """Поиск происходит по коориднатам шиорты и долготы
    при создании экземпляра """
    def __init__(self, lat=None, lon=None):
        self.lat = lat # это долгота lat''
        self.lon = lon # это широта 'lon'
    
    def run(self):
        """Посредественно после создания экзмемпляра, нужно вызвать метод run для поиска"""
        params = configuration_2()
        params = copy.deepcopy(params)
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params['lon'] = self.lat
        params['lat']= self.lon
        session = requests.Session()
        response = session.get(url=url, params=params)
        result = response.json()
        return result
        
        

if __name__ == '__main__':
    """first = City_api(city='Параньга')
    result = first.run()
    print(result)"""
    first = Geo_api(lat='', lon='')
    print(first.run())
    
    
    
    