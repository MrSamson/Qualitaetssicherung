from WeatherWrapper import WeatherWrapper


class IO(object):
    # Methoden
    # getCorrespondingWeatherData
    # outputWeather

    # Attribute
    # optionArray

    def getUserInput(self):
        userInput = input("[location], [current, today, forecast]")
        optionArray = {'location': '', 'option': 'current'}
        inputArray = userInput.lower().split(",")

        if len(inputArray) == 2:
            optionArray['location'] = inputArray[0].strip()
            optionArray['option'] = inputArray[1].strip()

        elif len(inputArray) == 1:
            optionArray['location'] = inputArray[0].strip()
        else:
            print("Please provide some input")

        return self.getWeather(optionArray)

    @staticmethod
    def getWeather(inputArray):
        weatherWrapper = WeatherWrapper()

        if inputArray['option'] == 'current':
            return weatherWrapper.getCurrentWeather(inputArray['location'])
        elif inputArray['option'] == 'today':
            return weatherWrapper.getTodayWeather(inputArray['location'])
        elif inputArray['option'] == 'forecast':
            return weatherWrapper.getFiveDaysForecast(inputArray['location'])
        else:
            return "something went wrong with the option"


io = IO()
print(io.getUserInput().getTemperature())

