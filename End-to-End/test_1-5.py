import unittest
import datetime

from ChannelControls import *

w_key = "NHGIKFM0VW4TGHDA"  # L3_T_4a2 write key
r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key


# Tests one instances of all basic communication messages in the system
class BasicCommunication(unittest.TestCase):
    '''
    # Test 1 - Simulate a person entering a room
    def test_person_entered_room(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test #1
        person_entered_room()

    # Test 2 - Simulate a person exiting a room
    def test_person_exited_room(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 2
        person_exited_room()
    '''

    # Test 3 - Simulate the max capacity being increased
    def test_max_capacity_increased(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 3
        self.assertEqual(uploadMaxCapChangeData("max_capacity_increased", 3, 10, datetime.datetime.now),200)


    '''
    # Test 4 - Simulate the max capacity being decreased
    def test_max_capacity_decreased(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 4
        uploadMaxCapChangeData(action, roomId, newMax, time)

    # Test 5 - Simulate the max capacity being reached
    def test_max_capacity_reached(self):
        # Delete all entries in ThinkSpeak
        clearChannel()

        # Run test # 5
        uploadMaxCapReachedData(action, roomId, time)
    '''
if __name__ == '__main__':
    unittest.main()
