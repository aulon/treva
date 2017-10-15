from skyscanner.skyscanner import Flights
from skyscanner.skyscanner import FlightsCache
from datetime import date, timedelta
import requests
import json

from backend.data import *

class SkyClient:

    def __init__(self, apikey="ha289870274395207127444935114707"):
        self.apikey = apikey
        self.res_cache = None
        self.start_city = None
        self.country_to_city_price_range = {}

    def get_routes(self, start_country, start_city_name, leaving_date, returning_date):

        start_city = None
        # transform from city name to city sky id.
        url = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query={}&apiKey={}".format(start_city_name, self.apikey)
        #print(url)
        response = requests.get(url)
        #print(response.status_code)
        response = response.json()
        for place in response["Places"]:
            #print(place)
            if start_country == place["CountryName"]:
                start_city = place["PlaceId"].split('-')[0]
                break

        #print(start_city)


        url = "http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/UK/eur/en-US/{}/{}/{}/{}?apikey={}".format(
            start_city,
            'anywhere',
            leaving_date,
            returning_date,
            self.apikey)
        response = requests.get(url)
        # print(response.status_code)
        response = response.json()


        # find id of start_city
        start_city_id = None
        for place in response["Places"]:
            if "CityName" in place and place["SkyscannerCode"] == start_city:
                start_city_id = place["PlaceId"]
                break
        # print(start_city_id)


        # get country to city dictionary
        id_to_city = {}
        city_to_id = {}
        country_to_city = {}
        city_to_country = {}
        for place in response["Places"]:
            if place["Type"] == "Country":
                if place["Name"] not in country_to_city:
                    country_to_city[place["Name"]] = []
            else:
                if place["CountryName"] not in country_to_city:
                    country_to_city[place["CountryName"]] = []
                country_to_city[place["CountryName"]].append(place["CityName"])
                if place["CityName"] not in city_to_country:
                    city_to_country[place["CityName"]] = place["CountryName"]
                if place["CityName"] not in city_to_id:
                    city_to_id[place["CityName"]] = place["PlaceId"]
                if place["PlaceId"] not in id_to_city:
                    id_to_city[place["PlaceId"]] = place["CityName"]


        for quote in response["Quotes"]:
            outbound = quote["OutboundLeg"]
            if outbound["OriginId"] == start_city_id:
                to_city = id_to_city[outbound["DestinationId"]]
                to_country = city_to_country[to_city]
                if to_country not in self.country_to_city_price_range:
                    self.country_to_city_price_range[to_country] = {}
                if to_city not in self.country_to_city_price_range[to_country]:
                    self.country_to_city_price_range[to_country][to_city] = {"price_range": [2**32, 0]}
                self.country_to_city_price_range[to_country][to_city]["price_range"][0] = min(self.country_to_city_price_range[to_country][to_city]["price_range"][0], 2*quote["MinPrice"])
                self.country_to_city_price_range[to_country][to_city]["price_range"][1] = max(self.country_to_city_price_range[to_country][to_city]["price_range"][1], 2*quote["MinPrice"])

        # print(json.dumps(self.country_to_city_price_range, indent=2))



    def get_quotes(self, departure_country, departure_city, start_date, end_date):
        self.departure_country = departure_country
        self.departure_city = departure_city
        self.res_cache = self.flight_service.get_cheapest_routes(
            market='UK',
            currency='GBP',
            locale='en-GB',
            originplace=departure_city,
            destinationplace='anywhere',
            outbounddate=start_date,
            inbounddate=end_date).parsed
        return self.res_cache


    def get_date_range(self, start_date, end_date, trip_length):
        for days in range(int((end_date - start_date).days) - trip_length):
            yield start_date + timedelta(days)


    def get_trips(self, departure_country, departure_city, trip_length, start_date, end_date):


        for single_date in self.get_date_range(start_date, end_date, trip_length):
            return_date = single_date + timedelta(trip_length)
            self.get_routes(departure_country, departure_city, start_date, end_date)

        return self.country_to_city_price_range


    def get_flights(trip_length, start_date, end_date, departure_country, departure_city, target_country, target_city):
        return [Flight("lufthansa", 1, "euro", 22.1), Flight("lufthansa", 1, "euro", 22.1), Flight("lufthansa", 1, "euro", 22.1), Flight("lufthansa", 1, "euro", 22.1)]

#
# skc = SkyClient()
# # # '''
# # # res = skc.get_quotes(
# # #     departure_country = "SPA",
# # #     departure_city = "BCN",
# # #     start_date=date(2018, 1, 1),
# # #     end_date=date(2018, 1, 3))
# # #
# # # print(res.keys())
# #
#
# # # skc.get_routes(start_city="BCN", leaving_date="2017-10", returning_date="2017-11")
# #
# res = skc.get_trips(
#     departure_country="Spain",
#     departure_city="Barcelona",
#     start_date = date(2018,1,1),
#     end_date = date(2018,2,1),
#     trip_length = 20)
#
# print(json.dumps(res, indent=2))

