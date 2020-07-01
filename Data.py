import requests
from requests import RequestException


class Data:
    def __init__(self):
        self._confirmed_cases = ''
        self._recovered_cases = ''
        self._death_cases = ''

    def request_data(self, country):
        url = f'https://covid2019-api.herokuapp.com/country/{country}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except RequestException as error:
            print(error)