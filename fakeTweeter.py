from WeatherReport import WeatherReport
from Tweeter import OutputInterface


# from TwitterAPI import TwitterAPI

class tweeterAdapter(OutputInterface):

    def transmitToTwitter(self, tweet=''):
        print(tweet)
