from Tweeter import Tweeter


class TweeterAdapter(Tweeter):

    def transmitToTwitter(self, tweet):
        print(tweet)
