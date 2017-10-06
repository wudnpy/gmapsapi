# Using Python requests and the Google Maps Geocoding API.
#
# References:
#
# * http://docs.python-requests.org/en/latest/
# * https://developers.google.com/maps/
from time import sleep

import requests

class GParser():
    def __init__(self):
        self.API_KEY = ''
        self.GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'  # 'https://maps.googleapis.com/maps/api/place/details/json'
        self.checked = None
        self.get_first_page()

    def get_first_page(self):
        params = {
            # 'input': 'Медицинская клиника',
            'key': self.API_KEY,
            'location': '55.7520233, 37.6174994',
            'radius': '50000',
            'region': 'ru',
            'type': 'dentist',
        }

        req = requests.get(self.GOOGLE_MAPS_API_URL, params=params)
        res = req.json()
        result = res
        for item in result['results']:
            print(item['name'])
        if 'next_page_token' in result:
            self.checked = result['next_page_token']

    def get_next_page(self):
            print('NEXT PAGE')
            print('TOKEN: '+self.checked)
            params = {
                # 'input': 'Медицинская клиника',
                'key': self.API_KEY,
                'location': '55.7520233, 37.6174994',
                'radius': '50000',
                'region': 'ru',
                'type': 'hospital',
                'pagetoken': self.checked
            }

            self.checked = None

            req = requests.get(self.GOOGLE_MAPS_API_URL, params=params)
            res = req.json()
            result = res

            for item in result['results']:
                print(item['name'])
            if 'next_page_token' in result:
                self.checked = result['next_page_token']

gparser = GParser()

while gparser.checked:
    sleep(5)
    gparser.get_next_page()
    sleep(5)

#geodata = dict()

#geodata['lat'] = result['geometry']['location']['lat']
#geodata['lng'] = result['geometry']['location']['lng']
#geodata['address'] = result['formatted_address']

#print(geodata)

#print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
# 221B Baker Street, London, Greater London NW1 6XE, UK. (lat, lng) = (51.5237038, -0.1585531)
