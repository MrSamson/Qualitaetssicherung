import pyowm
import requests
import Weather
import json



class WeatherWrapper(object):
    dict = {}


    def __apicall(self, location):
        # Testing with API Call
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units={}&appid={}'.format(location, 'metric',
                                                                                              'f9129773efcfc84c3e2c1bf63eb2f65c', )
        res = requests.get(url)
        data = res.json()
        return data

        #print(res)

    def publicapicall(self, location):
        json_data = self.__apicall(location)
        #currentWeather = json['list'][0]['dt']
        currentWeather = json.loads(json_data)
        return currentWeather


    def initWeather(self,json_data ):
        data = json.dumps(json_data)

        for x in json_data:
            json_data['list'][x]['dt'] = Weather()
            json_data['list'][x]['dt'].setTemperature(json_data['list'][x]['main']['temp'])
            json_data['list'][x]['dt'].setFeelsLike(json_data['list'][x]['main']['feels_like'])
            json_data['list'][x]['dt'].setMinTemp(json_data['list'][x]['main']['temp_min'])
            json_data['list'][x]['dt'].setMaxTemp(json_data['list'][x]['main']['temp_max'])
            dict[x] =json_data['list'][x]['dt']


    def callDict(self):
        print(dict)

    def getCurrentWeather(self, location):

        json = self.__apicall(location)

        #return json
        # todo: json auseinanderpfrimeln
        currentWeather = json['list'][7]['dt']

        return currentWeather


        # todo: create object with values from json
        #weather = Weather()




w = WeatherWrapper()

#w.getCurrentWeather('Karlsruhe')
#print(w.getCurrentWeather('Karlsruhe'))
print(w.publicapicall('Karlsruhe'))
#w.initWeather(w.publicapicall('Karlsruhe'))
#print(w.callDict())






