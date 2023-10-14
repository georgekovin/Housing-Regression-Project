import pandas as pd
from geopy.geocoders import Nominatim

data = pd.read_csv('data/data.csv')


address = (data['street'] + ' ' +
           data['city'] + ', ' +
           data['state'] + ' ' +
           data['zipcode'])

city = data['city'] + ', ' + data['state']


nom = Nominatim(timeout=None, user_agent='coord_loc')

house_coords = address.apply(nom.geocode).apply(lambda x: (x.latitude, x.longitude))
city_coords = city.apply(nom.geocode).apply(lambda x: (x.latitude, x.longitude))

house_coords.to_csv('data/house_coordinates.csv')
city_coords.to_csv('data/city_coordinates.csv') 