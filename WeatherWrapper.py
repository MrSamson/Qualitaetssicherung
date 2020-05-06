import pyowm
import requests
import Weather
import json


class WeatherWrapper(object):




    def __apicall(self, location):
        # Testing with API Call
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units={}&appid={}'.format(location, 'metric',
                                                                                              'f9129773efcfc84c3e2c1bf63eb2f65c', )
        res = requests.get(url)
        data = res.json()
        return data

        #print(res)

    def publicapicall(self, location):
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units={}&appid={}'.format(location, 'metric', 'f9129773efcfc84c3e2c1bf63eb2f65c',)
        res = requests.get(url)
        data = res.json()
        print(data)

    def getCurrentWeather(self, location):

        json = self.__apicall(location)

        #return json
        # todo: json auseinanderpfrimeln
        feelsLike = (json['list'][0]['main']['feels_like'])
        print(feelsLike)


        # todo: create object with values from json
        #weather = Weather()




w = WeatherWrapper()
w.getCurrentWeather('Karlsruhe')
#print(w.getCurrentWeather('Karlsruhe'))




