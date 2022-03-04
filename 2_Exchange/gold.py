import json

import requests


class Gold:
    GOLD_INFORMATION_URI = 'http://api.nbp.pl/api/cenyzlota?format=json'

    def get_gold_price(self):
        response = requests.get(self.GOLD_INFORMATION_URI)
        data = response.text
        parse_json = json.loads(data)
        return parse_json[0]['cena']