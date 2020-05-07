import pyowm
import requests
from Weather import Weather
import json
import datetime
import time


class WeatherWrapper(object):
    dict = {}

    def __apicall(self, location):
        # Testing with API Call
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units={}&appid={}'.format(location, 'metric',
                                                                                              'f9129773efcfc84c3e2c1bf63eb2f65c', )
        res = requests.get(url)
        data = res.json()
        return data

    def publicapicall(self, location):
        json_data = self.__apicall(location)
        # currentWeather = json['list'][0]['dt']
        currentWeather = json.loads(json_data)
        return currentWeather

    def getCurrentWeather(self, location):
        json = self.__apicall(location)

        # Object format: temperature, feelsLike, minTemp, maxTemp, dt, weatherState = ''
        weatherlist = {}
        objName = str(json['list'][0]['dt'])
        temperature = json['list'][0]['main']['temp']
        temp_min = json['list'][0]['main']['temp_min']
        temp_max = json['list'][0]['main']['temp_max']
        temp_feels_like = json['list'][0]['main']['feels_like']
        temp_dt = json['list'][0]['dt_txt']
        weatherstate = json['list'][0]['weather'][0]['description']

        weatherlist[objName] = Weather(temperature, temp_feels_like, temp_min, temp_max, temp_dt, weatherstate)

        return weatherlist[objName]

    def getTodayWeather(self, location):
        json = self.__apicall(location)

        # Object format: temperature, feelsLike, minTemp, maxTemp, dt, weatherState = ''
        weatherlist = {}
        today = datetime.date.today()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        unixtime = time.mktime(tomorrow.timetuple())
        # while dt_text <= heute
        i = 0
        while float(json['list'][i]['dt']) <= unixtime:
            objName = str(json['list'][i]['dt'])
            temperature = json['list'][i]['main']['temp']
            temp_min = json['list'][i]['main']['temp_min']
            temp_max = json['list'][i]['main']['temp_max']
            temp_feels_like = json['list'][i]['main']['feels_like']
            temp_dt = json['list'][i]['dt_txt']
            weatherstate = json['list'][i]['weather'][0]['description']
            weatherlist[objName] = Weather(temperature, temp_feels_like, temp_min, temp_max, temp_dt, weatherstate)
            i += 1

        return weatherlist

    # Testausgabe
    def printToday(self, location):
        wrapper = WeatherWrapper()

        list = wrapper.getTodayWeather(location)
        # wrapper.getTodayWeather('Karlsruhe')
        for x in list:
            print("Uhrzeit: ")
            print(list[x].getDt())
            print("Temp: ")
            print(list[x].getTemperature())
            print("feels like: ")
            print(list[x].getFeelsLike())
            print("min: ")
            print(list[x].getMinTemp())
            print("max: ")
            print(list[x].getMaxTemp())
            print("------")

    def printCurrent(self, location):
        wrapper = WeatherWrapper()

        print("Datum: ")
        print(wrapper.getCurrentWeather(location).getDt())
        print("temperatur: ")
        print(wrapper.getCurrentWeather(location).getTemperature())
        print("temp_min: ")
        print(wrapper.getCurrentWeather(location).getMinTemp())
        print("temp_max: ")
        print(wrapper.getCurrentWeather(location).getMaxTemp())
        print("feels like: ")
        print(wrapper.getCurrentWeather(location).getFeelsLike())
        print("Wetter: ")
        print(wrapper.getCurrentWeather(location).getWeatherState())


wrapper = WeatherWrapper()
wrapper.printCurrent('Karlsruhe')
print("-----------------------------------")
wrapper.printToday('Neulingen')
