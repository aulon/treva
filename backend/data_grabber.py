from backend.sky_client import get_flights, get_trips
from backend.data import *
from backend.places_client import get_hotels_and_city_image

class DataGrabber:
    def __init__(self, country, city, trip_length, min_date, max_date):
        self.country = country
        self.city = city
        self.trip_length = trip_length
        self.min_date = min_date
        self.max_date = max_date
        self.destinations_dataset = get_trips(country, city, trip_length, min_date, max_date)
        self._prepare()

    def _prepare(self):
        for country, cities in self.destinations_dataset.items():
            for city, description in cities.items():
                flights = self._query_flights(country, city)
                hotels, city_img = self._query_hotels(country, city)
                min_hotel_price = 2 ** 31
                max_hotel_price = 0

                for h in hotels:
                    h.price *= self.trip_length
                    if h.price >= max_hotel_price:
                        max_hotel_price = h.price
                    if h.price <= min_hotel_price:
                        min_hotel_price = h.price

                if max_hotel_price:
                    s, l = description["price_range"]
                    description["price_range"] = min_hotel_price + s, max_hotel_price + l

                description["flights"] = flights
                description["hotels"] = hotels
                description["img"] = city_img

    def get_destinations(self):
        destinations = []
        for country, cities in self.destinations_dataset.items():
            for city, description in cities.items():
                destinations.append(Destination(country, city, description["price_range"][0], description["price_range"][1], description["img"]))
        return destinations

    def get_flights(self, country, city):
        return self.destinations_dataset[country][city]["flights"]

    def get_hotels(self, country, city):
        return self.destinations_dataset[country][city]["hotels"]

    def _query_flights(self, dest_country, dest_city):
        return [Flight("lufthansa", 1, "euro", 22.1)]

    def _query_hotels(self, dest_country, dest_city):
        return get_hotels_and_city_image(dest_country, dest_city)