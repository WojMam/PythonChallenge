import json
import requests
import config


class TableA:
    def get_all_currencies_codes(self):
        currencies_codes = []
        for currency in self.get_all_exchange_rates():
            if currency['code'] is not None:
                currencies_codes.append(currency['code'])
        return currencies_codes

    def get_all_exchange_rates(self):
        response = requests.get(config.TABLE_URI)
        data = response.text
        parse_json = json.loads(data)
        return parse_json[0]['rates']

    def get_given_currency_by_code(self, code):
        for currency in self.get_all_exchange_rates():
            if currency['code'] == code:
                return currency

    def get_given_currency_rate_by_code(self, code):
        return self.get_given_currency_by_code(code)['mid']