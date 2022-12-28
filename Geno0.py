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


def get_temperature_full():
    full_temp ={}
    for i in range(len(cities)):
        url = "http://wttr.in/"+cities[i]+"?format=%t"
        Upage= urlopen(url)
        page = Upage.read()
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
    print("obtaining url")
    url = "http://wttr.in/"+city+"?format=%t"
    print("url obtained")
    Upage= urlopen(url)
    print("url opened")
    page = Upage.read()
    tempC = page.decode("utf-8")
    print("temp obtained")
    return tempC     

def get_time(city):
    url = "https://times.is/"+city
    Upage = urlopen(url)
    page = Upage.read()
    time = page.decode("utf-8")
    print(time)
    return time