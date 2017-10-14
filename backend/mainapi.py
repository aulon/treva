from flask import Flask, request
from flask_restful import Resource, Api
from backend.core import *
from datetime import date

app = Flask(__name__)
api = Api(app)
core = Core()


class NewTrip(Resource):
    def get(self):
        min_d = list(map(int, request.args.get('min_date').split("-")))
        max_d = list(map(int, request.args.get('max_date').split("-")))

        return core.new_trip(
                             n_people=request.args.get('n_people'),
                             trip_length_days=request.args.get('trip_length_days'),
                             min_date=date(min_d[0], min_d[1], min_d[2]),
                             max_date=date(max_d[0], max_d[1], max_d[2])).to_json()


class UnlikeDestination(Resource):
    def get(self):
        return core.unlike_destination(reason=request.args.get('reason')).to_json()


class LikeDestination(Resource):
    def get(self):
        return core.like_destination().to_json()


class LikeFlight(Resource):
    def get(self):
        return core.like_flight().to_json()


class UnlikeFlight(Resource):
    def get(self):
        return core.unlike_flight(reason=request.args.get('reason')).to_json()


class LikeHotel(Resource):
    def get(self):
        return core.like_hotel().to_json()


class UnlikeHotel(Resource):
    def get(self):
        return core.unlike_hotel(reason=request.args.get('reason')).to_json()


class CompleteBooking(Resource):
    def get(self):
        return core.complete_booking().to_json()


class AddBookingToFavorites(Resource):
    def get(self):
        return core.add_booking_to_favorites().to_json()


api.add_resource(LikeDestination, '/like_destination')
api.add_resource(UnlikeDestination, '/unlike_destination')
api.add_resource(NewTrip, '/new_trip')
api.add_resource(LikeFlight, '/like_flight')
api.add_resource(UnlikeFlight, '/unlike_flight')
api.add_resource(LikeHotel, '/like_hotel')
api.add_resource(UnlikeHotel, '/unlike_hotel')
api.add_resource(CompleteBooking, '/complete_booking')
api.add_resource(AddBookingToFavorites, '/add_booking_to_favorites')


if __name__ == '__main__':
    app.run(debug=True, port=5050)