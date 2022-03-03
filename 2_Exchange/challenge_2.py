"""
Console Application: Exchange

User can use this application to:
    - Get the Exchange information from the banking API
    - Calculate the exchange rates
"""


import requests
import json


def get_gold_price():
    response = requests.get('http://api.nbp.pl/api/cenyzlota?format=json')
    data = response.text
    parse_json = json.loads(data)
    return parse_json[0]['cena']


def get_all_exchange_rates():
    response = requests.get('http://api.nbp.pl/api/exchangerates/tables/a?format=json')
    data = response.text
    parse_json = json.loads(data)
    return parse_json[0]['rates']


def get_given_currency_by_code(code):
    for currency in get_all_exchange_rates():
        if currency['code'] == code:
            return currency


def get_given_currency_rate_by_code(code):
    return get_given_currency_by_code(code)['mid']


if __name__ == "__main__":
    print(get_given_currency_by_code('EUR'))
    print(get_given_currency_rate_by_code('EUR'))