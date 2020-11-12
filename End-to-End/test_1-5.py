import unittest
import datetime
import time

from ChannelControls import *

w_key = "NHGIKFM0VW4TGHDA"  # L3_T_4a2 write key
r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key


# Tests one instances of all basic communication messages in the system
class BasicCommunication(unittest.TestCase):

    # Wait 5 seconds before each test, since thingspeak has message limitations
    def setUp(self):
        time.sleep(5)

    # Test 1 - Simulate a person entering a room
    def test_person_entered_room(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test #1
        self.assertEqual(200, uploadPersonEntering(1, 2, datetime.datetime.now))

    # Test 2 - Simulate a person exiting a room
    def test_person_exited_room(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 2
        self.assertEqual(200, uploadPersonExiting(2, 1, datetime.datetime.now))

    # Test 3 - Simulate the max capacity being increased
    def test_max_capacity_increased(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 3
        self.assertEqual(200, uploadIncreasedCapacity(3, 10, datetime.datetime.now))

    # Test 4 - Simulate the max capacity being decreased
    def test_max_capacity_decreased(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 4

        self.assertEqual(200, uploadDecreasedCapacity(4, 9, datetime.datetime.now))

    # Test 5 - Simulate the max capacity being reached
    def test_max_capacity_reached(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 5
        uploadMaxCapReachedData(5, datetime.datetime.now)


if __name__ == '__main__':
    unittest.main()
