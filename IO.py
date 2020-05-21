from WeatherWrapper import WeatherWrapper


class IO(object):

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

    def getWeather(self, inputArray):
        if inputArray['option'] == 'current':
            return self.getCurrentWeather(inputArray['location'])
        elif inputArray['option'] == 'today':
            return self.getTodayWeather(inputArray['location'])
        elif inputArray['option'] == 'forecast':
            return self.getForecast(inputArray['location'])
        else:
            return "something went wrong with the option"

    def getCurrentWeather(self, location):
        weatherWrapper = WeatherWrapper()
        return weatherWrapper.printCurrent(location)

    def getTodayWeather(self, location):
        weatherWrapper = WeatherWrapper()
        return weatherWrapper.printToday(location)

    def getForecast(self, location):
        weatherWrapper = WeatherWrapper()
        return weatherWrapper.printforecast(location)


io = IO()
print(io.getUserInput())
