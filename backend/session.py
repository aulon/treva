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
        self.flights = self.data_grabber.get_flights(self.country, self.city)
        self.hotels = self.data_grabber.get_hotels(self.country, self.city)

    def back(self):
        if len(self.suggested_hotels):
            self.suggested_hotels.pop()
            if len(self.suggested_hotels):
                self.hotels += self.suggested_hotels[-1][1]
                self.suggested_hotels[-1][1] = []
                return
        if len(self.suggested_flights):
            self.suggested_flights.pop()
            if len(self.suggested_flights):
                self.flights += self.suggested_flights[-1][1]
                self.suggested_flights[-1][1] = []
                return
        if len(self.suggested_destinations):
            self.suggested_destinations.pop()
            if len(self.suggested_destinations):
                self.destinations += self.suggested_destinations[-1][1]
                self.suggested_destinations[-1][1] = []

    def new_destination(self, reason: str=None) -> Destination:
        if reason:
            if reason == "country":
                remaining_dest = []
                for d in self.destinations:
                    if d.country == self.suggested_destinations[-1][0].country:
                        self.suggested_destinations[-1][1].append(d)
                    else:
                        remaining_dest.append(d)
                self.destinations = remaining_dest
            else:
                self.suggested_destinations[-1][1].append(self.suggested_destinations[-1][0])

        self.suggested_destinations.append((self.destinations.pop(), []))

        return self.suggested_destinations[-1][0]

    def new_flight(self, reason: str=None):
        if reason:
            remaining_flights = []

            if reason == "carrier":
                for f in self.flights:
                    if f.carrier == self.suggested_flights[-1][0].carrier:
                        self.suggested_flights[-1][1].append(f)
                    else:
                        remaining_flights.append(f)
            elif reason == "price":
                for f in self.flights:
                    if f.price >= self.suggested_flights[-1][0].price:
                        self.suggested_flights[-1][1].append(f)
                    else:
                        remaining_flights.append(f)
            elif reason == "date":
                for f in self.flights:
                    if f.start_flight_date == self.suggested_flights[-1][0].start_flight_date:
                        self.suggested_flights[-1][1].append(f)
                    else:
                        remaining_flights.append(f)
            elif reason == "duration":
                for f in self.flights:
                    if f.avg_time >= self.suggested_flights[-1][0].avg_time:
                        self.suggested_flights[-1][1].append(f)
                    else:
                        remaining_flights.append(f)

            if remaining_flights:
                self.flights = remaining_flights

        self.suggested_flights.append((self.flights.pop(), []))

        return self.suggested_destinations[-1][0]

    def new_hotel(self, reason: str=None):
        if reason:
            remaining_hotels = []

            if reason == "review":
                for h in self.hotels:
                    if h.review == self.suggested_hotels[-1][0].review:
                        self.suggested_hotels[-1][1].append(h)
                    else:
                        remaining_hotels.append(h)
            elif reason == "price":
                for h in self.hotels:
                    if h.price >= self.suggested_hotels[-1][0].price:
                        self.suggested_hotels[-1][1].append(h)
                    else:
                        remaining_hotels.append(h)
            else:
                self.suggested_hotels[-1][1].append(self.suggested_hotels[-1][0])

            if remaining_hotels:
                self.hotels = remaining_hotels

        self.suggested_flights.append((self.flights.pop(), []))

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
