import requests
import datetime as dt
from dateutil.relativedelta import relativedelta


END_POINT = "https://api.tequila.kiwi.com/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers ={
            "apikey":api_key
        }
        self.fly_from = "SIN"


    def iata_code(self, city_name):
        addition = "locations/query"
        function_endpoint = END_POINT + addition
        params = {
            "term": city_name,
            "locale":"en-US",
            "location_types":"airport",
        }

        data = requests.get(url=function_endpoint, params=params, headers=self.headers)
        data.raise_for_status()
        print(data.json())
        return data.json()['locations'][0]['city']['code']

    def flight_search(self, dest, stopovers=0, via_city=""):
        addition = "search"
        function_endpoint = END_POINT + addition
        tomorrow = dt.datetime.now()
        return_from = tomorrow + relativedelta(days=+1)
        end_date = tomorrow + relativedelta(months=+6)

        params = {
            "fly_from":self.fly_from,
            "fly_to":dest,
            "date_from":tomorrow.strftime("%d/%m/%Y"),
            "date_to":end_date.strftime("%d/%m/%Y"),
            "return_from":return_from.strftime("%d/%m/%Y"),
            "return_to":end_date.strftime("%d/%m/%Y"),
            "select_airlines":"SQ,EK,QR,TR,CX,AY,LX,AF",
            "select_airlines_exclude":False,
            "flight_type":"round",
            "curr":"SGD",
            "max_stopovers":stopovers,
            "via_city":via_city
        }

        response = requests.get(url=function_endpoint, params=params, headers=self.headers)
        price_data = response.json()

        try:
            return price_data['data'][0]

        except IndexError:
            data = []
            return data






