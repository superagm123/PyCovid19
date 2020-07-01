import requests
from requests import RequestException


class Data:
    def request_data(self, country):
        url = f'https://covid2019-api.herokuapp.com/country/{country}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except RequestException as error:
            print(error)