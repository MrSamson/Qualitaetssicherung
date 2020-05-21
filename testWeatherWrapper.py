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



if __name__ == '__main__':
    unittest.main()