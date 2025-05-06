
def configuration():
    """Конфигурация Api Вызова по названию города."""
    data = {
        'q' : 'Йошкар-Ола',
        'appid' : '2c44e9473514e691665d4f13e2a5f0a4',
        'units' : 'metric',
        'header': '',
        'lang' : 'ru'
    }
    return data

def configuration_2():
    """Конфигурация API вызова для функции с геоданными"""
    data = {
        'lat' : '',
        'lon' : '',
        'appid' : '2c44e9473514e691665d4f13e2a5f0a4',
        'units' : 'metric',
        'lang' : 'ru',    
    }
    return data


class Error_Not_Find_ciity(Exception):
    """Если ответ на Nominatium вернул None, то вызывается это исключение"""
    def __init__(self, some):
        self.some = some
    def __call__(self, *args, **kwds):
        dicts = {
            'cod' : '603',
            'problem' : f'к сожалению города с названием "{self.some}" не существует'
        }
        return dicts
    
class Error_Lot_City(Exception):
    """ошибка выходит, если запрос корректен, но к сожалению очень много городов."""
    def __init__(self, some):
        self.some = some
    def __call__(self, *args, **kwds):
        dicts = {
            'cod' : '601',
            'problem' : f'К сожалению слишком много городо с названием "{self.some}". ' + 
            'Пожалуйста напишите еще через запятую, область или район',
        }
        return dicts

def errors_argument_602():
    """ошибка если не задан именнованный параметр city"""
    dicts = {
        'cod' : '602',
        'problem' : 'К сожалению нету именнованного аргумента "city" '
    }
    return dicts



