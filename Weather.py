class Weather(object):

    # class for weather objects
    def __init__(self, temperature, feelsLike, minTemp, maxTemp, dt = '', weatherState = ''):
        self.__temperature = temperature
        self.__feelsLike = feelsLike
        self.__minTemp = minTemp
        self.__maxTemp = maxTemp
        self.__dt = dt
        self.__weatherState = weatherState

    # getter
    def getTemperature(self):
        return self.__temperature

    def getFeelsLike(self):
        return self.__feelsLike

    def getMinTemp(self):
        return self.__minTemp

    def getMaxTemp(self):
        return self.__maxTemp

    def getDt(self):
        return self.__dt

    def getWeatherState(self):
        return self.__weatherState