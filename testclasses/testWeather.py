import unittest
from Weather import Weather

# refering to: https://docs.python.org/3/library/unittest.html
# basic unit tests for weather class
class testWeather(unittest.TestCase):

    def testWeatherConstructor(self):
        w = Weather(1,2,3,4, '2000-12-31 20:00:00', 'cloudy')
        self.assertEqual(w.getTemperature(), 1)
        self.assertEqual(w.getFeelsLike(), 2)
        self.assertEqual(w.getMinTemp(), 3)
        self.assertEqual(w.getMaxTemp(), 4)
        self.assertEqual(w.getDt(), '2000-12-31 20:00:00')
        self.assertEqual(w.getWeatherState(), 'cloudy')

    def testWeatherConstructorEmptyState(self):
        w = Weather(1, 2, 3, 4)
        self.assertEqual(w.getWeatherState(), '')

if __name__ == '__main__':
    unittest.main()
