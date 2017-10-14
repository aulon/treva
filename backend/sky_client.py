from skyscanner.skyscanner import Flights
from skyscanner.skyscanner import FlightsCache


class QueryFlight:
    def __init__(self):
        self.start_flight_date = 0
        self.airline = 0
        self.price = 0
        self.average_time = 0


def get_trips(departure_country, departure_city, trip_length, start_date, end_date):
    return {
        "Spain": {
            "Barcelona": (300, 500),
            "Madrid": (200, 500),
        },

        "Romania": {
            "Bucharest": (100, 300),
            "Sibiu": (100, 200)
        }
    }

def get_flights(trip_length, start_date, end_date, departure_city, target_city):
    return [QueryFlight(), QueryFlight(), QueryFlight(), QueryFlight()]

