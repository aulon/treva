from abc import ABCMeta, abstractmethod
import json

class Serializable:
    __metaclass__ = ABCMeta

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Destination(Serializable):
    def __init__(self, country, city, min_price, max_price, month, img_url):
        self.country = country
        self.city = city
        self.min_price = min_price
        self.max_price = max_price
        self.month = month
        self.img_url = img_url


class Flight(Serializable):
    def __init__(self, carrier, price, currency, avg_time):
        self.carrier = carrier
        self.price = price
        self.currency = currency
        self.avg_time = avg_time


class Hotel(Serializable):
    def __init__(self, name, review, price, facilities):
        self.name = name
        self.review = review
        self.price = price
        self.facilities = facilities

