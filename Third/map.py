"""
MAP PROJECT
"""
import random
import folium
from cachetools import cached, TTLCache
from geopy.geocoders import Nominatim

cache = TTLCache(maxsize=100, ttl=86400)


def map(data):
    """
    MAIN FUNCTION
    """
    # Creating the folium map, base of the project
    maper = folium.Map(tiles="Stamen Terrain",
                         zoom_start=10)

    # Creating later with friends locations
    friend_locations = folium.FeatureGroup(name="Friends location")
    for name in data:
        print(name)
        print(data[name])
        friend_locations.add_child(folium.Marker(location=[(data[name][0] + \
        random.uniform(-0.001, 0.001)), (data[name][1] + random.uniform(-0.001, 0.001))],
                                    popup=name,
                                    fill_opacity = 0.5,
                                    icon=folium.Icon(color=random.choice(['darkpurple',\
'cadetblue', 'darkred', 'green', 'lightgray', 'darkgreen', 'pink', 'purple', 'beige', \
'lightgreen', 'red', 'darkblue', 'lightblue', 'gray', 'blue', 'white', 'orange', 'black', \
'lightred']))))

    # Adding all layers to the main map
    maper.add_child(friend_locations)
    maper.save("templates/map.html")
    print("The program finished its work. Enjoy your map!")


@cached(cache)
def coordinate_finder(location):
    """
    Function, that finds coordinates of addresses.
    Is cached, so you don't have to contact with server for every address, that is using again
    >>> coordinate_finder('Ashland, New Hampshire, USA')
    (43.69568, -71.630859)
    >>> coordinate_finder('University of New Mexico, Albuquerque, New Mexico, USA')
    (35.08663275, -106.62020940505188)
    """
    geolocator = Nominatim(user_agent="my_application")
    locator = geolocator.geocode(location)
    return (locator.latitude, locator.longitude)
