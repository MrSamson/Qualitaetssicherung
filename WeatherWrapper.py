import pyowm
import requests

api_key = 'f9129773efcfc84c3e2c1bf63eb2f65c'  # API Key
owm = pyowm.OWM(api_key)
location = input("Enter location:")
print("location is: " + location)
language = 'en'

# Testing with API Call
url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&lang={}'.format(location, api_key, language)
res = requests.get(url)
data = res.json()

print(res)
print(data)
print('########')

# Testing with API functions
observation = owm.weather_at_place('Karlsruhe, Ger')
weather = observation.get_weather()
temperature = weather.get_temperature('celsius')
print('Wetter: ')
print(weather)
print('Temp:')
print(temperature)
