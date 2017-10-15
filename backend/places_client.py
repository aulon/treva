from backend.data import *
from backend.config.api_credentials import api_key
import urllib3


def __get_location(city: str, country: str):
    helper = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city + ',' + country + ',&key=' + api_key
    '''
    f = urllib.request.urlopen(helper)
    print(f.read())
    return f
    '''
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

    for a in j['results']:
        try:
            l.append(Hotel(a['name'], a['rating'], 50, 'wifi'))
        except:
            l.append(Hotel(a['name'], 0, 50, 'wifi'))


    return l

def get_hotels(country, city):
    lat, lng = __get_location(city, country)
    return __get_hotels(lat, lng)
#
# pc = PlacesClient()
# (lat, lng) = pc.get_location('Barcelona', 'Spain')
# pc.get_hotels(lat, lng)