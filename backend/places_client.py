from backend.data import *
from backend.config.api_credentials import api_key
import urllib3

def __get_location(city: str, country: str):
    helper = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city + ',' + country + ',&key=' + api_key
    http = urllib3.PoolManager()
    r = http.request('GET', helper)
    j = json.loads(r.data.decode('utf-8'))
    lat = j['results'][0]['geometry']['location']['lat']
    lng = j['results'][0]['geometry']['location']['lng']

    return (lat, lng)


def __get_hotels(lat: float, lng: float):
    helper = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=' + api_key + \
             '&type=hotel&location=' + str(lat) + ',' + str(lng) +  '&radius=50000'
    http = urllib3.PoolManager()
    r = http.request('GET', helper)
    j = json.loads(r.data.decode('utf-8'))
    l = []
    photo_reference = j['results'][0]['photos'][0]['photo_reference']

    for a in j['results']:
        img = a['photos'][0]['photo_reference']
        img_helper = 'https://maps.googleapis.com/maps/api/place/photo?key=' + api_key + '&photoreference=' \
                     + img + '&maxwidth=1600'
        try:
            l.append(Hotel(a['name'], a['rating'], 50, 'wifi', img_helper))
        except:
            l.append(Hotel(a['name'], 0, 50, 'wifi', img_helper))

    return (l, photo_reference)

def get_hotels_and_city_image(country, city):
    lat, lng = __get_location(city, country)
    return __get_hotels(lat, lng)

get_hotels_and_city_image('Spain', 'Barcelona')