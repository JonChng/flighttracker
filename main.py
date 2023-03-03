#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
import requests
import dotenv
import os

dotenv.load_dotenv()


dm = DataManager(os.environ["SHEETY_API"])
fs = FlightSearch(os.environ['KIWI_API'])
email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

sheet_data = dm.get_data()

def update_code():
    global sheet_data
    for i in sheet_data:
        if 'lowestPrice' not in i.keys():
            i['lowestPrice'] = 10000
        id = i['id']
        to_search = i['city']
        code = fs.iata_code(to_search)
        data = {
            "city": i['city'],
            "iataCode": code,
            "lowestPrice": i['lowestPrice']
        }
        dm.update_sheet(id, data)
        sheet_data = dm.get_data()

def find_flights():
    global sheet_data

    for i in sheet_data:

        price = i['lowestPrice']
        cheapest_found = fs.flight_search(i['iataCode'])

        stopovers = 0
        while cheapest_found == []:
            stopovers += 1
            cheapest_found = fs.flight_search(i['iataCode'], stopovers=stopovers)


        cheapest_price = cheapest_found['price']

        if cheapest_price < price:
            print(i['iataCode'])
            print("CHEAP!")
            data = {
                "city": i['city'],
                "iataCode": i['iataCode'],
                "lowestPrice": cheapest_price
            }
            if stopovers >= 1:
                cheapest_found['stopovers'] = stopovers
                cheapest_found['via_city'] = cheapest_found['route'][0]['flyTo']


            dm.update_sheet(i['id'], data)

            d1 = requests.get(url=f"https://api.sheety.co/{os.environ['SHEETY_API']}/flightDeals/users")
            data = d1.json()['users']
            print(data)
            NotificationManager(cheapest_found, email, password, data)

update_code()
find_flights()









