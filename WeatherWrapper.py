import pyowm
import requests

api_key = 'f9129773efcfc84c3e2c1bf63eb2f65c'  # API Key
owm = pyowm.OWM(api_key)


#location = 'karlsruhe'
location = input("Enter location:")
print("location is: " + location)
language = 'en'

# Testing with API Call
response = requests.get(
   'http://api.openweathermap.org/data/2.5/forecast?q=' + location + '&appid=' + api_key + '&lang=' + language)
print(response.status_code)
print(response.content)
print('########')

# Testing with API functions
observation = owm.weather_at_place('Karlsruhe, Ger')
weather = observation.get_weather()
temperature = weather.get_temperature('celsius')
print('Wetter: ')
print(weather)
print('Temp:')
print(temperature)
