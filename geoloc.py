import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myApp")


lat = 45.443330
long = 10.995400

query = str(lat) + ", " + str(long)
location = geolocator.reverse(query)

print("address: " + location.address)
print("latitude: " + str(location.latitude) + ", longitude: " + str(location.longitude))
print(location.raw["address"]["city"])

#
# info = location.address.split(', ')
#
# print(info[4])
#
# my_house = geolocator.geocode("via Fama 5, Verona")
# print(my_house.address)

def get_city(lat, long):
    geoloc = Nominatim(user_agent="myApp")
    query = str(lat) + ", " + str(long)
    loc = geoloc.reverse(query)
    return loc.address

lat = 45.443330
long = 10.995400

address = get_city(lat, long)

print("my address is: " + address)