from Tweeter import OutputInterface


class TweeterAdapter(OutputInterface):

    def transmitToTwitter(self, tweet):
        print(tweet)
