#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import dotenv
import os

dotenv.load_dotenv()

dm = DataManager(os.environ["SHEETY_API"])
fs = FlightSearch(os.environ['KIWI_API'])

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
        cheapest_price = cheapest_found['price']

        if cheapest_price < price:
            print(i['iataCode'])
            print("CHEAP!")
            data = {
                "city": i['city'],
                "iataCode": i['iataCode'],
                "lowestPrice": cheapest_price
            }
            dm.update_sheet(i['id'], data)
            NotificationManager(os.environ["TWILIO_ID"], os.environ["TWILIO_API"], cheapest_found, os.environ['TWILIO_NO'], os.environ["MY_NO"])

update_code()
find_flights()









