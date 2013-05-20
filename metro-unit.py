import unittest
import metro
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
      self.response = """
    {
    "Trains": [{
        "Car": "6",
        "Destination": "NewCrltn",
        "DestinationCode": "D13",
        "DestinationName": "New Carrollton",
        "Group": "1",
        "Line": "OR",
        "LocationCode": "K01",
        "LocationName": "Court House",
        "Min": "1"
    }, {
        "Car": "6",
        "Destination": "Vienna",
        "DestinationCode": "K08",
        "DestinationName": "Vienna",
        "Group": "2",
        "Line": "OR",
        "LocationCode": "K01",
        "LocationName": "Court House",
        "Min": "2"
    }, {
        "Car": "8",
        "Destination": "NewCrltn",
        "DestinationCode": "D13",
        "DestinationName": "New Carrollton",
        "Group": "1",
        "Line": "OR",
        "LocationCode": "K01",
        "LocationName": "Court House",
        "Min": "8"
    }, {
        "Car": "8",
        "Destination": "Vienna",
        "DestinationCode": "K08",
        "DestinationName": "Vienna",
        "Group": "2",
        "Line": "OR",
        "LocationCode": "K01",
        "LocationName": "Court House",
        "Min": "9"
    }, {
        "Car": "6",
        "Destination": "Vienna",
        "DestinationCode": "K08",
        "DestinationName": "Vienna",
        "Group": "2",
        "Line": "OR",
        "LocationCode": "K01",
        "LocationName": "Court House",
        "Min": "19"
    }, {
        "Car": "6",
        "Destination": "Largo",
        "DestinationCode": "G05",
        "DestinationName": "Largo Town Center",
        "Group": "1",
        "Line": "OR",
        "LocationCode": "K01",
        "LocationName": "Court House",
        "Min": ""
    }]
}
"""

    def test_timeForNextWestTrain(self):
        metroData = json.loads(self.response)
        self.assertEqual("2", metro.timeForNextWestTrain(metroData))

    def test_timeForNextEastTrain(self):
        metroData = json.loads(self.response)
        self.assertEqual("1", metro.timeForNextEastTrain(metroData))

if __name__ == '__main__':
    unittest.main()