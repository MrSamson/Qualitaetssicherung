from WeatherWrapper import WeatherWrapper


class IO(object):

    def startTool(self):

       if (self.printWeather(self.getUserInput()) != 0):
           print("error")



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

        return optionArray

    def printWeather(self, inputArray):
        wrapper = WeatherWrapper()

        if inputArray['option'] == 'current':

            weather = wrapper.getCurrentWeather(inputArray['location'])

            self.printCurrent(weather)

            #self.printCurrent(inputArray['location'])
        elif inputArray['option'] == 'today':
            weatherList = wrapper.getTodayWeather(inputArray['location'])
            self.printToday(weatherList)
        elif inputArray['option'] == 'forecast':
            weatherList = wrapper.getFiveDaysForecast(inputArray['location'])
            self.printforecast(weatherList)
        else:
            return 1000

        return 0

    # Textausgabe
    def printToday(self, list):

        print("------")
        for x in list:
            print("Um",                                list[x].getDt(), "Uhr beträgt die Temperatur",
                                                        list[x].getTemperature(), "°C")
            print("Das Wetter zeichnet sich aus durch", list[x].getWeatherState())
            print("Die gefühlte Temperatur beträgt",    list[x].getFeelsLike(), "°C")
            print("Die Temperatur schwankt zwischen",   list[x].getMinTemp(), "°C und ",
                                                        list[x].getMaxTemp(), "°C")
            print("------")


    def printforecast(self, list):

        print("------")
        for x in list:
            print("Um", list[x].getDt(), "Uhr beträgt die Temperatur",
                  list[x].getTemperature(), "°C")
            print("Das Wetter zeichnet sich aus durch", list[x].getWeatherState())
            print("Die gefühlte Temperatur beträgt", list[x].getFeelsLike(), "°C")
            print("------")

    def printCurrent(self, weather):

        print("------")
        print("Die aktuelle Temperatur beträgt",        weather.getTemperature(), "°C")
        print("Das Wetter zeichnet sich aus durch",     weather.getWeatherState())
        print("Die gefühlte Temperatur beträgt",        weather.getFeelsLike(), "°C")
        print("------")

io = IO()
io.startTool()
# io.getUserInput()