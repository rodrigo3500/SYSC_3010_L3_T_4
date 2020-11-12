import unittest
import ChannelControls
import datetime
import requests
import json
import time

w_key = "NHGIKFM0VW4TGHDA"  # L3_T_4a2 write key
r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key
URL = 'https://api.thingspeak.com/channels/1224300/feeds.json?api_key='

# Sends sample data log entries to ThingSpeak.
class TestDataRetrival(unittest.TestCase):
    def setUp(self):
        # Given that the only the test data is present in the thingspeak channel
        clearResponse= ChannelControls.clearChannel()
        self.assertEqual(200, clearResponse)
        uploadEnter = ChannelControls.uploadPersonEntering(1, 2, datetime.datetime.now())
        self.assertEqual(200,uploadEnter)
        time.sleep(5)
        uploadExit = ChannelControls.uploadPersonExiting(3, 1, datetime.datetime.now())
        self.assertEqual(200,uploadExit)
        time.sleep(5)
        uploadMaxIncrease = ChannelControls.uploadIncreasedCapacity(1,10, datetime.datetime.now())
        self.assertEqual(200,uploadMaxIncrease)
        time.sleep(5)
        uploadMaxDecrease = ChannelControls.uploadDecreasedCapacity(3,9, datetime.datetime.now())
        self.assertEqual(200,uploadMaxDecrease)
        time.sleep(5)
        uploadMaxReached = ChannelControls.uploadMaxCapReachedData(3, datetime.datetime.now())
        self.assertEqual(200,uploadMaxReached)


    # Test #6
    # Asserting to ensure all uploaded data can be retreived. The setup function uploads 5 data points for testing
    def test_getAllData(self):
        fullURL = URL+r_key
        getData = requests.get(fullURL).json()
        entries = getData['feeds']
        self.assertEqual(5,len(entries))

    # Test #7
    # Testing to ensure that just the last three data points can be retreived
    def test_getSpecificEntries(self):
        HEADER = '&results=3'
        fullURL = URL+r_key+HEADER
        getData = requests.get(fullURL).json()
        entries = getData['feeds']
        self.assertEqual(3,len(entries))

if __name__=="__main__":
    unittest.main()

