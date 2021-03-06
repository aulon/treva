from datetime import date
from backend.data import *
from backend.session import Session

class Core:
    """
        core logic that implements the mainapi
    """
    def __init__(self):
        self.favorite_bookings = []
        self.completed_bookings = []
        self.session = None

    def new_trip(self, trip_length_days: int, n_people: int, min_date: date, max_date: date, departure_country: str, departure_city: str) -> Destination:
        self.session = Session(trip_length_days, n_people, min_date, max_date, departure_country, departure_city)
        return self.session.new_destination()

    def unlike_destination(self, reason: str) -> Destination:
        return self.session.new_destination(reason)

    def like_destination(self) -> Flight:
        return self.session.new_flight()

    def unlike_flight(self, reason: str):
        return self.session.new_flight(reason)

    def like_flight(self) -> Hotel:
        return self.session.new_hotel()

    def unlike_hotel(self, reason: str) -> Hotel:
        return self.session.new_hotel(reason)

    def like_hotel(self) -> Booking:
        return self.session.complete_booking()

    def complete_booking(self) -> Booking:
        self.completed_bookings.append(self.session.complete_booking())
        return self.completed_bookings[-1]

    def add_booking_to_favorites(self) -> Destination:
        self.favorite_bookings.append(self.session.complete_booking())
        self.session.reset_booking()
        return self.session.new_destination()

    def back(self):
        return self.session.back()
