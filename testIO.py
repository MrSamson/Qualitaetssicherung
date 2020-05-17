import unittest
from IO import IO

# refering to: https://docs.python.org/3/library/unittest.html
# basic unit tests for weather class

class testIO(unittest.TestCase):

    def testIO(self):
        IO.validateInput("test")

