import unittest
import http.client as httplib
from urllib.parse import urlencode

w_key = "NHGIKFM0VW4TGHDA"  # L3_T_4a2 write key
r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key


# Wipe all data from thingspeak - to be performed before each test
def clear_thingspeak():
    # Clears all past entries from thingspeak
    print("clear")


# Test 1 - Simulate a person entering a room
def person_entered_room():
    # Send person entered room data to thingspeak
    print("test")


# Test 2 - Simulate a person exiting a room
def person_exited_room():
    # Send person exited room data to thingspeak
    print("test")


# Test 3 - Simulate the max capacity being increased
def max_capacity_increased():
    # Send max capacity increased data to thingspeak
    print("test")


# Test 4 - Simulate the max capacity being decreased
def max_capacity_decreased():
    # Send max capacity decreased data to thingspeak
    print("test")


# Test 5 - Simulate the max capacity being reached
def max_capacity_reached():
    # Send person exited room data to thingspeak
    print("test")


# Tests one instances of all basic communication messages in the system
class BasicCommunication:

    # Test 1 - Simulate a person entering a room
    def test_person_entered_room(self):
        # Delete all entries in ThinkSpeak
        clear_thingspeak()

        # Run test #1
        person_entered_room()

    # Test 2 - Simulate a person exiting a room
    def test_person_exited_room(self):
        # Delete all entries in ThinkSpeak
        clear_thingspeak()

        # Run test # 2
        person_exited_room()


    # Test 3 - Simulate the max capacity being increased
    def test_max_capacity_increased():
        # Delete all entries in ThinkSpeak
        clear_thingspeak()

        # Run test # 3
        max_capacity_increased


    # Test 4 - Simulate the max capacity being decreased
    def test_max_capacity_decreased():
        # Delete all entries in ThinkSpeak
        clear_thingspeak()

        # Run test # 4
        max_capacity_decreased

    # Test 5 - Simulate the max capacity being reached
    def test_max_capacity_reached():
        # Delete all entries in ThinkSpeak
        clear_thingspeak()

        # Run test # 5
        max_capacity_reached()
