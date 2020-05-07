class Weather(object):

    # class for weather objects

    def __init__(self, temperature, feelsLike, minTemp, maxTemp, dt, weatherState = ''):
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

    # setter
    def setTemperature(self, temperature):
        self.__temperature = temperature

    def setFeelsLike(self, feelsLike):
        self.__feelsLike = feelsLike

    def setMinTemp(self, minTemp):
        self.__minTemp = minTemp

    def setMaxTemp(self, maxTemp):
        self.__maxTemp = maxTemp

    def setdt(self, dt):
        self.__dt = dt

    def setweatherState(self, weatherState):
        self.__weatherState = weatherState
