import datetime as dt
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.price = data['price']
        self.depart_from = data['flyFrom']
        self.fly_to = data['flyTo']
        self.from_city = data['cityFrom']
        self.city_to = data['cityTo']
        self.from_date = dt.datetime.fromtimestamp(data['dTime']).strftime('%d-%m-%Y')
        self.to_date = (dt.datetime.fromtimestamp(data['dTime']) + dt.timedelta(days = data['nightsInDest'] + 1)).strftime('%d-%m-%Y')
        self.airline = data['airlines'][0]
        self.stopovers = data['stopovers']
        self.via_city = data['via_city']
        self.booking = data['deep_link']

