from abc import ABCMeta
import json

class Serializable:
    __metaclass__ = ABCMeta

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Destination(Serializable):
    def __init__(self, country, city, min_price, max_price, img_url):
        self.country = country
        self.city = city
        self.min_price = min_price
        self.max_price = max_price
        self.img_url = img_url

class Flight(Serializable):
    def __init__(self, carrier, price, currency, avg_time):
        self.carrier = carrier
        self.price = price
        self.currency = currency
        self.avg_time = avg_time
        self.start_flight_date = 0

class Hotel(Serializable):
    def __init__(self, name, review, price, facilities, image_url):
        self.name = name
        self.review = review
        self.price = price
        self.facilities = facilities
        self.image_url = image_url


class Booking(Serializable):
    def __init__(self, destination, flight, hotel):
        self.destination = destination
        self.flight = flight
        self.hotel = hotel

