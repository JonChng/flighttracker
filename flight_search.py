import requests

END_POINT = "https://api.tequila.kiwi.com/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):
        self.api_key = api_key

    def iata_code(self, city_name):
        addition = "locations/query"
        function_endpoint = END_POINT + addition
        params = {
            "term": city_name,
            "locale":"en-US",
            "location_types":"airport",
        }
        headers = {
            "apikey":self.api_key
        }
        data = requests.get(url=function_endpoint, params=params, headers=headers)
        data.raise_for_status()
        return data.json()['locations'][0]['city']['code']


