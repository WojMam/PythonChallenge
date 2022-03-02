"""
Console Application: Exchange

User can use this application to:
    - Get the Exchange information from the banking API
    - Calculate the exchange rates
"""


import requests
import json


def get_gold_price():
    response_API = requests.get('http://api.nbp.pl/api/cenyzlota?format=json')
    data = response_API.text
    parse_json = json.loads(data)
    print("Data:", parse_json[0]['data'])
    print("Cena:", parse_json[0]['cena'])


if __name__ == "__main__":
    get_gold_price()