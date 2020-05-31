import unittest
from Weather import Weather

# refering to: https://docs.python.org/3/library/unittest.html
# basic unit tests for weather class
class testWeather(unittest.TestCase):

    def testWeatherConstructor(self):
        w = Weather(1,2,3,'cloudy')
        self.assertEqual(w.getFeelsLike(), 1)
        self.assertEqual(w.getMinTemp(), 2)
        self.assertEqual(w.getMaxTemp(), 3)
        self.assertEqual(w.getWeatherState(), 'cloudy')

    def testWeatherConstructorEmptyState(self):
        w = Weather(1, 2, 3)
        self.assertEqual(w.getWeatherState(), '')

if __name__ == '__main__':
    unittest.main()
