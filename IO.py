from WeatherReport import WeatherReport
from fakeTweeter import TweeterAdapter

class IO():

    def startTool(self):

        if (self.tweetWeather(self.getUserInput()) != 0):
            print("error")

    def getUserInput(self):
        userInput = input("""Please give us your location, and the option (current, today, forecast) you wish to know e.g. [stadt], [option]:
        """)
        optionArray = {'location': '', 'option': 'current'}
        inputArray = userInput.lower().split(",")

        if len(inputArray) == 2:
            optionArray['location'] = inputArray[0].strip()
            optionArray['option'] = inputArray[1].strip()

        elif len(inputArray) == 1:
            optionArray['location'] = inputArray[0].strip()
        else:
            print("Please provide some input")

        return optionArray

    def tweetWeather(self, inputArray):
        wrapper = WeatherReport()
        adpater = TweeterAdapter()

        if inputArray['option'] == 'current':
            weather = wrapper.getCurrentWeather(inputArray['location'])
            adpater.transmitToTwitter(self.buildCurrentWeatherTweet(weather))

        elif inputArray['option'] == 'today':
            weatherList = wrapper.getTodayWeather(inputArray['location'])
            adpater.transmitToTwitter(self.buildTodayWeatherTweet(weatherList))

        elif inputArray['option'] == 'forecast':
            weatherList = wrapper.getFiveDaysForecast(inputArray['location'])
            adpater.transmitToTwitter(self.buildForecastTweet(weatherList))

        else:
            return 1000

        return 0

    # Textausgabe
    def buildTodayWeatherTweet(self, list):

        outputString = ''

        # 280 chars allowed
        for x in list:
            outputString += '{}: Temperatur beträgt {} °C \n'.format(list[x].getDt()[-8: -3],
                                                                     round(list[x].getTemperature()))

        return outputString

    def buildForecastTweet(self, list):

        outputString = ''

        for x in list:
            outputString += '{}: Temperatur wird {} °C betragen\n'.format(list[x].getDt()[-0: -9],
                                                                          round(list[x].getTemperature()))
        return outputString

    def buildCurrentWeatherTweet(self, weather):

        outputString = ('Die aktuelle Temperatur beträgt {} °C. ' \
                        'Das Wetter zeichnet sich aus durch {}. ' \
                        'Die gefühlte Temperatur bertägt {} °C.'.format(round(weather.getTemperature()),
                                                                        weather.getWeatherState(),
                                                                        round(weather.getFeelsLike())))
        return outputString