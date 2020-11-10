import unittest
import http.client as httplib
from urllib.parse import urlencode

w_key = "NHGIKFM0VW4TGHDA"  # L3_T_4a2 write key
r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key



# Tests one instances of all basic communication messages in the system
class BasicCommunication:

    # TEST #3
    # Send a message emulating the max capacity of a room being reached to ThingSpeak
    def test_person_entered_room(self):
        # Write test code here
