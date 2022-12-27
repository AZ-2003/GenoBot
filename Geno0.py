from urllib.request import urlopen


'''

Description: obtains the tempersture (in Celsius) for a set of cities
Parametrs:
    (1) cities: an array of cities
Returns:
    (1) full_temp: a dictionary of cities and their temperature

'''
#Variable Declarations
cities = ["Dammam", "Manama", "LosAngeles", "Dubai", "SanDiego"]

def get_temperature_full(cities):
    full_temp ={}
    for i in range(len(cities)):
        url = "http://wttr.in/"+cities[i]+"?format=%t"
        page= urlopen(url)
        page = page.read()
        tempC = page.decode("utf-8")
        full_temp[cities[i]]=tempC
    return full_temp


'''

Description: obtains the temperature (in Celsius) for a designated city
Parametrs:
    (1) city: city name (with no spaces in between: ex: LosAngeles)
Returns:
    (1) tempC: a string consisting of the city's temperature

'''
def get_temperature(city):
    url = "http://wttr.in/"+city+"?format=%t"
    page= urlopen(url)
    page = page.read()
    tempC = page.decode("utf-8")
    return tempC     
