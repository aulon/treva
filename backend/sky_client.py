from skyscanner.skyscanner import Flights
from skyscanner.skyscanner import FlightsCache


class Trip:
    def __init__(self, city):
        self.city = city
        self.country = 0
        self.start_date = 0
        self.end_date = 0
        self.airline = 0
        self.price = 0
        self.average_time = 0


flights_service = FlightsCache('ha289870274395207127444935114707')
result = flights_service.get_cheapest_q(
    market='UK',
    currency='GBP',
    locale='en-GB',
    originplace='BCN',
    destinationplace='anywhere',
    outbounddate='2018-01-01',
    inbounddate='2018-01-07').parsed

print(result)


url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/UK/eur/en-US/{start_city}/anywhere/{leaving_date}/{returning_date}?apikey=ha436381528989070115577726756838"
# The above url will give you all prices from {start_city} to all possible places at the dates
# the dates can be either both a month like 2018-02 and 2018-03 OR both are specific a day like 2018-02-23 and 2018-03-03
start_city = "BCN"
leaving_date = "2017-12"
returning_date = "2017-12"
url = url.format(start_city=start_city, leaving_date=leaving_date, returning_date=returning_date)
response = requests.get(url)
print(response.status_code)
list_of_quotes = response.json()['Quotes']
sorted_quotes = sorted(list_of_quotes, key=lambda k: k['MinPrice'])