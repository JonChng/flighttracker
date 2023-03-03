from twilio.rest import Client
import datetime as dt
from flight_data import FlightData
import smtplib

class NotificationManager(FlightData):
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, data, email, password, to):

        super().__init__(data)

        link = self.booking

        price = self.price

        currency = "EUR"

        if self.stopovers >= 1:

            for i in to:
                print(i)
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=email, password=password)
                    connection.sendmail(to_addrs=i['email'], from_addr=email, msg=f"Subject:New Low Price Flight!\n\nLow price alert! Only {price} SGD to fly from Singapore-SIN to {self.city_to}-{self.fly_to}! from {self.from_date} to {self.to_date} on {self.airline}."
                                                                          f"\n\n{link}")
        else:
            for i in to:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=email, password=password)
                    connection.sendmail(to_addrs=i['email'], from_addr=email,
                                        msg=f"Subject:New Low Price Flight!\n\nLow price alert! Only {price} SGD to fly from Singapore-SIN to {self.city_to}-{self.fly_to}! from {self.from_date} to {self.to_date} on {self.airline}."
                                            f"{link}")




