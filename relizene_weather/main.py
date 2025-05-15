from .api_call import City_api, Geo_api
from .settings.settings import Error_Not_Find_ciity, Error_Lot_City, errors_argument_602




def run_city(header=None, city=None, appid=None):
    """При вызове именновнанного параметра, вызывается блок Run
    Этот метод только для поиска по городу. Вся подрбоная информация находится в разделе Readme"""
    if city:
        try:
            example = City_api(header=header, city=city, appid=appid)
        except Error_Lot_City as error_601:
            return error_601()
        except Error_Not_Find_ciity as error_603:
            return error_603()   
        else:
            result_2 = example.run()
            return result_2
    else: 
        return errors_argument_602()
         
    
def run_geo(lon=None, lat=None):
    """При вызове этого метода происходит поиск по координатам широты и долготы
    Вся подробная информация находится в Readme"""
    if lat and lon:
        """Посредственно сам поиск и результат поиска,
        если параметры не даны, то ответ 701"""
        example = Geo_api(lon=lon, lat=lat)
        result = example.run()
        return result
    else:
        return {
            'cod' : '701',
            'problem': 'К сожалению геоданные не были переданы'
        }



if __name__ == '__main__':
    a = run_city(city='Куракино, Параньгинский район',header='lang-ru')
    print(a)
    
    



