import pyowm
api_key = 'f9129773efcfc84c3e2c1bf63eb2f65c'
owm = pyowm.OWM(api_key)  # API Key


observation = owm.weather_at_place('Karlsruhe, Ger')
weather = observation.get_weather()
temperature = weather.get_temperature('celsius')
print('Wetter: ')
print(weather)
print('Temp:')
print(temperature)
