#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
import dotenv
import os

dotenv.load_dotenv()

dm = DataManager(os.environ["SHEETY_API"])
fs = FlightSearch(os.environ['KIWI_API'])

sheet_data = dm.get_data()
for i in range(len(sheet_data)):

    id = sheet_data[i]['id']
    to_search = sheet_data[i]['city']
    code = fs.iata_code(to_search)
    data = {
        "city": sheet_data[i]['city'],
        "iataCode":code,
        "lowestPrice":sheet_data[i]['lowestPrice']
    }
    dm.update_iata(id, data)









