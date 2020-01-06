# Simple weleakinfo.com API Wrapper, has implemented only function I needed for simple OSINT toolkit
import requests


class WeLeakInfo():
    def __init__(self, api_key):
        self.API_KEY = api_key
        self.session = requests.Session()
        self.session.headers = {
                                    'Authorization':    f'Bearer {self.API_KEY}',
                                    'User-Agent':       'OSINT Toolkit'}

    def public(self, type_, query, details=False):
        if type_ not in ('username', 'email', 'password', 'hash', 'ip', 'name', 'phone', 'domain'):
            raise AttributeError
        args = {'details': str(details).lower()}
        url = f"https://api.weleakinfo.com/v3/public/{type_}/{query}"
        response = self.session.get(url, params=args)
        return response.json()


if __name__ == "__main__":
    x = WeLeakInfo('d717fc9054d16463181aaec41bd5598104aaa5ab')
    types = ('username', 'email', 'password', 'hash', 'ip', 'name', 'phone', 'domain')
    print('[?] What type of information you want to check?')
    for type_ in types:
        print(f'[{types.index(type_)+1}] {type_}')
    type_ = int(input('[?] Select 1-8: '))-1
    details = input('[?] Show details about breaches? [Y/N]: ')
    if details.upper() == 'Y':
        details = True
    elif details.upper() == 'N':
        details = False
    else:
        raise AttributeError
    query = input(f'[?] Enter {types[type_]}: ')
    data = x.public(types[type_], query)
    print(data)