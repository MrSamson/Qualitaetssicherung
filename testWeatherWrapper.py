import datetime
import unittest
from WeatherWrapper import WeatherWrapper


# refering to: https://docs.python.org/3/library/unittest.html
# basic unit tests for weather class
class testWeatherWrapper(unittest.TestCase):

    # checks if an object of WeatherWrapper is created
    # may be used for learning tests, to see how the constructor works
    def testWeatherWrapperConstructor(self):
        w = WeatherWrapper()
        self.assertIsInstance(w, WeatherWrapper)

    # gets the current weather for Karlsruhe and checks if there will be
    # a new object-type (weather-Object) delivered
    # may be used for learning tests
    def testGetCurrentWeatherKarlsruhe(self):
        location = 'Karlsruhe'
        weatherWrapper = WeatherWrapper()
        self.assertNotIsInstance(weatherWrapper.getCurrentWeather(location), WeatherWrapper)

    # gets the current weather for Heidelberg and puts the results into an object
    # checks if all needed values are set
    # may be used for learning tests to see what values we can get
    def testGetCurrentWeatherKarlsruheCheckValues(self):
        location = 'Heidelberg'
        weatherWrapper = WeatherWrapper()
        currentWeather = weatherWrapper.getCurrentWeather(location)
        self.assertIsNotNone(currentWeather.getMinTemp())
        self.assertIsNotNone(currentWeather.getFeelsLike())
        self.assertIsNotNone(currentWeather.getMinTemp())
        self.assertIsNotNone(currentWeather.getMaxTemp())
        self.assertIsNotNone(currentWeather.getDt())
        self.assertIsNotNone(currentWeather.getWeatherState())

    # gets the five day weather forecast for Mannheim and puts the results into a list
    # to check if there is more than one object delivered
    # may be used for learning tests
    def testGetCurrentWeatherKarlsruhe(self):
        location = 'Heidelberg'
        weatherWrapper = WeatherWrapper()
        forecastList = weatherWrapper.getFiveDaysForecast(location)

        self.assertGreater(len(forecastList), 1)
        self.assertEqual(len(forecastList), 40)

    # gets the five day weather forecast for Mannheim and puts the results into a list
    # checks if all values in all objects are set
    # may be used for learning tests
    def testGetCurrentWeatherHeidelbergCheckValues(self):
        location = 'Heidelberg'
        weatherWrapper = WeatherWrapper()
        forecastList = weatherWrapper.getFiveDaysForecast(location)

        for i in forecastList:
            self.assertIsNotNone(forecastList[i].getMinTemp())
            self.assertIsNotNone(forecastList[i].getFeelsLike())
            self.assertIsNotNone(forecastList[i].getMinTemp())
            self.assertIsNotNone(forecastList[i].getMaxTemp())
            self.assertIsNotNone(forecastList[i].getDt())
            self.assertIsNotNone(forecastList[i].getWeatherState())

    # todo: fix this
    # gets todays weather and checks if the date is really at least today
    def testGetTodayWeatherSchwetzingen(self):
        location = 'Schwetzingen'
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        weatherWrapper = WeatherWrapper()
        todaysWeather = weatherWrapper.getTodayWeather(location)

        # for i in todaysWeather:

if __name__ == '__main__':
    unittest.main()
