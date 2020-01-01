import requests


class Weather():
    def __init__(self, api_key):
        self._API_KEY = api_key

    def get_by_city_name(self, city_name, units=None, _format=None):
        if units not in ('imperial', 'metric', None) and _format not in ('xml', 'html', None):
            raise AttributeError
        args = {'q': city_name,
                'APPID': self._API_KEY}
        if units:
            args['units'] = units
        if _format:
            args['mode'] = _format
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=args)
        if not _format:
            return r.json()
        else:
            return r.text()


if __name__ == "__main__":
    API_KEY = "9fa16bd5078ca8dffdf54339845e08e6"
    w = Weather(API_KEY)