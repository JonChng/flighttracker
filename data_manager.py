import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = f"https://api.sheety.co/{self.api_key}/flightDeals/prices/"

    def get_data(self):
        response = requests.get(self.endpoint)
        return response.json()['prices']

    def update_sheet(self, row, data):
        new_endpoint = self.endpoint + str(row)
        data = {
            "price": data
        }
        response = requests.put(url=new_endpoint, json=data)
        response.raise_for_status()
        return response.text


