from urllib.request import urlopen


'''

Description: obtains the weather forecast (in Celsius) for a set of cities
Parametrs:
    1. cities: an array of cities
Returns:
    1. weather: a dictionary of cities and their weather

'''
def get_temperature_full(cities):
    full_temp ={}
    for i in range(len(cities)):
        url = "http://wttr.in/"+cities[i]+"?format=%t"
        page= urlopen(url)
        page = page.read()
        tempC = page.decode("utf-8")
        full_temp[cities[i]]=tempC
    return full_temp

def get_temperature(city):
    url = "http://wttr.in/"+city+"?format=%t"
    page= urlopen(url)
    page = page.read()
    tempC = page.decode("utf-8")
    return tempC     
