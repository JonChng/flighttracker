from twilio.rest import Client
import datetime as dt
from flight_data import FlightData

class NotificationManager(FlightData):
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, api_id, api_key, data,from_no, to_no):
        print(data)
        super().__init__(data)

        self.client = Client(api_id, api_key)
        price = self.price
        currency = "EUR"

        if self.stopovers >= 1:

            message = self.client.messages \
                .create(
                body= f'Low price alert! Only {price} SGD to fly from Singapore-SIN to {self.city_to}-{self.fly_to},'
                     f' from {self.from_date} to {self.to_date} on {self.airline}.'
                      f'\nFlight has {self.stopovers} stop overs, via {self.via_city}',
                from_= from_no,
                to=to_no
            )
        else:
            message = self.client.messages \
                .create(
                body=f'Low price alert! Only {price} SGD to fly from Singapore-SIN to {self.city_to}-{self.fly_to},'
                     f' from {self.from_date} to {self.to_date} on {self.airline}.',
                from_=from_no,
                to=to_no
            )



