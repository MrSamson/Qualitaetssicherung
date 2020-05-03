import unittest
from Weather import Weather

# refering to: https://docs.python.org/3/library/unittest.html
# basic unit tests for weather class

class testWeather(unittest.TestCase):

    def testWeather(self):
        w = Weather(1,2,3,'cloudy')
        self.assertEqual(w.getFeelsLike(), 1)
        self.assertEqual(w.getMinTemp(), 2)
        self.assertEqual(w.getMaxTemp(), 3)
        self.assertEqual(w.getWeatherState(), 'cloudy')

    def testWeatherEmptyState(self):
        w = Weather(1, 2, 3)
        self.assertEqual(w.getWeatherState(), '')

    def testWeatherEmptyState(self):
        w = Weather(1, 2, 3)
        w.setMaxTemp(20)
        self.assertEqual(w.getMaxTemp(), 20)

if __name__ == '__main__':
    unittest.main()
