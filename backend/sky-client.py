from skyscanner.skyscanner import Flights
from skyscanner.skyscanner import FlightsCache


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
