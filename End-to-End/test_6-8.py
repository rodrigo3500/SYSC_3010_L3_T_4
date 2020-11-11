import unittest
import http.client as httplib
from urllib.parse import urlencode
import ChannelControls
import datetime

w_key = "NHGIKFM0VW4TGHDA"  # L3_T_4a2 write key
r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key

# Sends sample data log entries to ThingSpeak.
class TestDataRetrival(unittest.TestCase):

    def setUp(self):
        ChannelControls.clearChannel()

    # Test #
    # Describe test functions here
    def test_testname(self): # Sample test definition, to be updated
        uploadEnter = ChannelControls.uploadPersonEnterExitRoomData("enter", 1, 2, datetime.datetime.now())
        self.assertEqual(200,uploadEnter)
        
        uploadExit = ChannelControls.uploadPersonEnterExitRoomData("exit", 1, 1, datetime.datetime.now())
        self.assertEqual(200,uploadExit)
        
        uploadMaxIncrease = ChannelControls.uploadMaxCapChangeData("max capacity increased",1,10, datetime.datetime.now())
        self.assertEqual(200,uploadMaxIncrease)

        uploadMaxDecrease = ChannelControls.uploadMaxCapChangeData("max capacity decreased",1,9, datetime.datetime.now())
        self.assertEqual(200,uploadMaxDecrease)

        uploadMaxReached = ChannelControls.uploadMaxCapReachedData("max capacity reached", 1, datetime.datetime.now())
        self.assertEqual(200,uploadMaxReached)


if __name__=="__main__":
    unittest.main()

