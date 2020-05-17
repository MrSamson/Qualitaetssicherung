class IO(object):
    # Methoden
    # getCorrespondingWeatherData
    # outputWeather


    # Attribute
    # optionArray



    def getUserInput(self):
        userInput = input("[location], [current, today, forecast]")

        validateInput(userInput)


def validateInput(self, userInput):
    optionArray = {'location': '', 'option': 'current'}
    inputArray = userInput.lower().split(",")

    if len(inputArray) > 1:
        optionArray['location'] = inputArray[0]
        optionArray['location'] = inputArray[1]
    elif len(inputArray) > 0:
        optionArray['location'] = inputArray[0]
    else
        print("Please provide some input")