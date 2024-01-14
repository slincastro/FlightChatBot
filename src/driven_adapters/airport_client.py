
import requests


class AirportClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def search_airports(self, search_term):
        url = 'https://www.air-port-codes.com/api/v1/multi'
        headers = {
            'APC-Auth': self.api_key,
            'APC-Auth-Secret' : self.api_secret 
        }
        params = {
            'term': search_term
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            airports = response.json()

            return airports
        else:
            return None
        
    def get_airport_values(self, city):
        response = self.search_airports(city)
        airports_number = len(response['airports'])
        informacion_aeropuertos = [{'iata': aeropuerto['iata'], 'city': aeropuerto['city'], 'name': aeropuerto['name']} for aeropuerto in response['airports']]
        
        return informacion_aeropuertos, airports_number
