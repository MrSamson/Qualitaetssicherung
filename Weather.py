class Weather(object):

    def __init__(self, feelsLike, minTemp, maxTemp, weatherState):
        self.__feelsLike = feelsLike
        self.__minTemp = minTemp
        self.__maxTemp = maxTemp
        self.__weatherState = weatherState


    # getter
    def getFeelsLike(self):
        return self.__feelsLike

    def getMinTemp(self):
        return self.__minTemp

    def getMaxTemp(self):
        return self.__maxTemp

    def getWeatherState(self):
        return self.__weatherState

    # setter
    def setFeelsLike(self, feelsLike):
        self.__feelsLike = feelsLike

    def setMinTemp(self, minTemp):
        self.__minTemp = minTemp

    def setMaxTemp(self, maxTemp):
        self.__maxTemp = maxTemp

    def setFeelsLike(self, weatherState):
        self.__weatherState = weatherState