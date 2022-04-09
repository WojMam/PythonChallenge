import json
import requests
import config


def get_all_exchange_rates():
    response = requests.get(config.TABLE_URI)
    data = response.text
    parse_json = json.loads(data)
    return parse_json[0]['rates']


def get_given_currency_by_code(code):
    for currency in get_all_exchange_rates():
        if currency['code'] == code:
            return currency


def get_all_currencies_codes():
    currencies_codes = []
    for currency in get_all_exchange_rates():
        if currency['code'] is not None:
            currencies_codes.append(currency['code'])
    return currencies_codes


def get_given_currency_rate_by_code(code):
    return get_given_currency_by_code(code)['mid']


def calculate_exchange_rate(currency_rate, user_ammount):
    return user_ammount / currency_rate
