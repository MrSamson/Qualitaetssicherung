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

    def getWeather(self, inputArray):
        if inputArray['option'] == 'current':
            return self.printCurrent(inputArray['location'])
        elif inputArray['option'] == 'today':
            return self.printToday(inputArray['location'])
        elif inputArray['option'] == 'forecast':
            return self.printforecast(inputArray['location'])
        else:
            return "something went wrong with the option"

    # Textausgabe
    def printToday(self, location):
        wrapper = WeatherWrapper()

        list = wrapper.getTodayWeather(location)
        for x in list:
            print("Uhrzeit: ")
            print(list[x].getDt())
            print("Temp: ")
            print(list[x].getTemperature())
            print("feels like: ")
            print(list[x].getFeelsLike())
            # print("min: ")
            # print(list[x].getMinTemp())
            # print("max: ")
            # print(list[x].getMaxTemp())
            print("Wetter: ")
            print(wrapper.getCurrentWeather(location).getWeatherState())
            print("------")

    def printforecast(self, location):
        wrapper = WeatherWrapper()
        list = wrapper.getFiveDaysForecast(location)
        for x in list:
            print("Datum: ")
            print(list[x].getDt())
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


io = IO()
print(io.getUserInput())
