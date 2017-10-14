from backend.data import *
from backend.data_grabber import DataGrabber


class Session:
    """
        the booking sesssion, created initally or after finishing one booking
    """

    def __init__(self, trip_length, n_people, min_date, max_date, departure_country, departure_city):
        self.suggested_destinations = []
        self.suggested_flights = []
        self.suggested_hotels = []
        self.n_people = n_people
        self.min_date = min_date
        self.max_date = max_date
        self.trip_length = trip_length
        self.city = departure_city
        self.country = departure_country

        self.data_grabber = DataGrabber(self.country, self.city, trip_length, min_date, max_date)
        self.destinations = self.data_grabber.get_destinations()
        self.flights = self.data_grabber.get_flights()
        self.hotels = self.data_grabber.get_hotels()

    def back(self):
        if len(self.suggested_hotels):
            self.suggested_hotels.pop()
            if len(self.suggested_hotels):
                self.hotels += self.suggested_hotels[-1][1]
                return
        if len(self.suggested_flights):
            self.suggested_flights.pop()
            if len(self.suggested_flights):
                self.flights += self.suggested_flights[-1][1]
                return
        if len(self.suggested_destinations):
            self.suggested_destinations.pop()
            if len(self.suggested_destinations):
                self.destinations += self.suggested_destinations[-1][1]

    def new_destination(self, reason: str=None) -> Destination:
        if not reason:
            # first, generate
            self.suggested_destinations.append((self.destinations[-1], []))
        else:
            # fix reason
            pass
        return self.suggested_destinations[-1][0]

    def new_flight(self, reason: str=None):
        if not reason:
            # first, generate random
            self.suggested_flights.append((self.flights[-1], []))
        else:
            # fix reason
            pass
        return self.suggested_flights[-1][0]

    def new_hotel(self, reason: str=None):
        if not reason:
            # first, generate random
            self.suggested_hotels.append((self.hotels[-1], []))
        else:
            # fix reason
            pass
        return self.suggested_hotels[-1][0]

    def complete_booking(self):
        #complete booking from last destination, flight and hotel
        return Booking(self.suggested_destinations[-1][0], self.suggested_flights[-1][0], self.suggested_hotels[-1][0])

    def reset_booking(self):
        self.suggested_destinations = []
        self.suggested_flights = []
        self.suggested_hotels = []

    def reset_booking_to_destination(self):
        self.suggested_destinations.pop()
        self.suggested_flights = []
        self.suggested_hotels = []
