from backend.data import *

class Session:
    """
        the booking sesssion, created initally or after finishing one booking
    """

    def __init__(self, trip_length, n_people, min_date, max_date):
        self.destinations = []
        self.flights = []
        self.hotels = []
        self.n_people = n_people
        self.min_date = min_date
        self.max_daye = max_date
        self.trip_length = trip_length

    def new_destination(self, reason: str=None) -> Destination:
        if not reason:
            # first, generate random
            self.destinations.append(Destination("Country", "City", 100, 200, 'January', 'img://url'))
        else:
            # look in history and filter
            pass
        return self.destinations[-1]

    def new_flight(self, reason: str=None):
        if not reason:
            # first, generate random
            self.flights.append(Flight("Lufthansa", 50, "euro", 23.2))
        else:
            # look in history and filter
            pass
        return self.flights[-1]

    def new_hotel(self, reason: str=None):
        if not reason:
            # first, generate random
            self.hotels.append(Hotel("Hotel",4.2, 100, "wifi, bjs"))
        else:
            # look in history and filter
            pass
        return self.hotels[-1]

    def complete_booking(self):
        #complete booking from last destination, flight and hotel
        return Booking(self.destinations[-1], self.flights[-1], self.hotels[-1])

    def reset_booking(self):
        self.destinations = []
        self.flights = []
        self.hotels = []

    def reset_booking_to_destination(self):
        self.destinations.pop()
        self.flights = []
        self.hotels = []
