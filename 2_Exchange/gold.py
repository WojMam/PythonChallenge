import json
import config
import requests


def get_gold_price():
    response = requests.get(config.GOLD_INFORMATION_URI)
    data = response.text
    parse_json = json.loads(data)
    return parse_json[0]['cena']
