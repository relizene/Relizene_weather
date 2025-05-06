import inspect
import requests
from settings.settings import Error_Not_Find_ciity, Error_Lot_City



def find_key_words(dicts):
    """Функция которая обьединяетя в одну строку название города,
    деревни, страны, штата и его Iso кода для корректного поиска
    местоположения для openweartheapi"""
    priority_keys = [
        'city', 'town', 'village', 
        'hamlet', 'municipality', 
        'state_district', 'state', 
        'country', 'ISO3166-2-lvl4'
    ]
    strong = ''
    for keys in priority_keys:
        if keys in dicts:
            strong += dicts[keys] + ', '
    strong = strong.rstrip(', ')        
    return strong


def validate_city_geopy(city_name):
    """Функция валидатор, вовзращает None если город не найден.
    Если метод находит более одного местоположения, то возбуждает исключение"""
    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': city_name,
        'format' : 'json',
        'addressdetails': 1,
        'limit': 3,
    }
    headers = {'User-agent' : 'relizene_map'}
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        response = response.json()
        if len(response) > 1:
            raise Error_Lot_City(city_name)
        if response:
            dicts = response[0]['address']
            key_words = find_key_words(dicts)
            return key_words
    return None
        


class ValidateMeta(type):
    """Мета класс для валидации, возбуждает исклюение, если валидация не прошла
    а если валидация прошла, то создает класс, для дальнешей работы."""

    def __call__(cls, *args, **kwargs):
        """init signature, перехватывает инизиализацию созданию экземпляра
        Так же собирает их в словарь с ключом или значением."""
        init_signature= inspect.signature(cls.__init__)
        bound_args = init_signature.bind_partial(None, *args, **kwargs)
        bound_args.apply_defaults()
        city = bound_args.arguments.get('city') # значение аргумента из аргумента "city"
        
        if city is None:
            raise ValueError(f"{cls.__name__} должен иметь именнованый аргумент 'city!' ") # в слуае если параметр city не был найден. 
        response = validate_city_geopy(city_name=city) # вызов функции валидатора для города
        if response is None:
            raise Error_Not_Find_ciity(city)
        
        kwargs['city'] = response # подставление аргумента city из location для корректного запроса к openweartheapi
        return super().__call__(*args, **kwargs)



  
if __name__ == '__main__':
    print(validate_city_geopy('Параньга'))
    #print(find_key_words({'state': 'Arkansas', 'ISO3166-2-lvl4': 'US-AR', 'country': 'United States', 'country_code': 'us'}))
    
