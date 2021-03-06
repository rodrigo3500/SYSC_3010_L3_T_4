from unittest import TestCase, main
from sqlite3 import connect, Error
from json import loads

db_file = "system.db" # path to database
conn = None # to store database connection

"""
Returns the current occupancy of room (currentSize) from database
"""
def getCurrentOccupancy(roomID):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command = '''SELECT currentSize FROM Room WHERE roomID = ?'''
    csr.execute(command, (str(roomID),)) # Executing read here
    row = csr.fetchall() # Storing read data into a list
    conn.close()

    return row[0][0]

"""
Returns the max occupancy of room (capacity) from database
"""
def getMaxOccupancy(roomID):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command = '''SELECT capacity FROM Room WHERE roomID = ?'''
    csr.execute(command, (str(roomID),)) # Executing read here
    row = csr.fetchall() # Storing read data into a list
    conn.close()

    return row[0][0]

"""
Updates the current occupancy of room (currentSize) in database
"""
def updateCurrentOccupancy(roomID, currentSize):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database
    command = '''UPDATE Room SET currentSize = ? WHERE roomID = ?'''
    csr.execute(command, (str(currentSize), str(roomID))) # Executing write here
    conn.commit() # Finalizing changes

    conn.close()

"""
Updates the max occupancy of room (capacity) in database
"""
def updateMaxOccupancy(roomID, capacity):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database
    command = '''UPDATE Room SET capacity = ? WHERE roomID = ?'''
    csr.execute(command, (str(capacity), str(roomID))) # Executing write here
    conn.commit() # Finalizing changes

    conn.close()

"""
Returns the first name, last name, email, and phone number of manager (from database) as a dictionary
"""
def getManagerDetails(managerID):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database
    command = '''SELECT * FROM Manager WHERE managerID = ?'''
    csr.execute(command, str(managerID)) # Executing read here
    row = csr.fetchall() # Storing read data as a list
    conn.close()

    # Checking if manager was found in database
    if (row): # If manager found extract tuple containing data from list
        attributes = row[0]
    else: # Else exit
        print("Manager not found")
        return

    # Parsing manager details into dictionary
    details = {}
    details["firstName"] = attributes[1]
    details["lastName"] = attributes[2]
    details["email"] = attributes[3]
    details["phoneNumber"] = attributes[4]

    return details

"""
Puts JSON entry from ThingSpeak into a dictionary
"""
def getThingSpeak(entry):
    #URL = 'https://api.thingspeak.com/channels/1224300/feeds.json?api_key='
    #r_key = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key
    #HEADER = '&results=3'
    data = loads(entry)
    return data
    

# Resetting values before running tests
updateCurrentOccupancy(1000, 0) # Resetting current occupancy to 0
updateMaxOccupancy(1000, 0) # Resetting max occupancy to 0

"""
Test Cases for:
    updateCurrentOccupancy(roomID, currentSize)
    updateMaxOccupancy(roomID, capacity)
    getManagerDetails(managerID)
    getThingSpeak(entry)
"""
class DatabaseTests(TestCase):
    
    """
    First updates current occupancy in database then reads and compares against test
    """
    def test_update_currentOccupancy(self):
        roomID = 1000
        newCurrOccupancy = 4
        updateCurrentOccupancy(roomID, newCurrOccupancy)
        self.assertEqual(getCurrentOccupancy(roomID), newCurrOccupancy)

    """
    First updates max occupancy in database then reads and compares against test
    """
    def test_update_maxOccupancy(self):
        roomID = 1000
        newMaxOccupancy = 5
        updateMaxOccupancy(roomID, newMaxOccupancy)
        self.assertEqual(getMaxOccupancy(roomID), newMaxOccupancy)

    """
    Reads manager details from database and compares against test
    """
    def test_get_managerDetails(self):
        managerID = 1
        test_details = {'firstName': 'Tarun', 'lastName': 'Rodrigo', 'email': 'hari@carling.ca', 'phoneNumber': 1234567890}
        self.assertEqual(getManagerDetails(managerID), test_details)
    
    """
    Reads all fields for an entry and compares against test
    """
    def test_data_addition(self):
        json_entry = '{"Field 1": "enter", "Field 2": 1000, "Field 3": 5}'
        data = getThingSpeak(json_entry)
        
        self.assertTrue(data["Field 1"] == "enter" or data["Field 1"] == "exit" or data["Field 1"] == "max capcity increased" or data["Field 1"] == "max capacity decreased")
        self.assertTrue(isinstance(data["Field 2"], int)) # Room ID
        self.assertTrue(isinstance(data["Field 3"], int)) # Current number of people in room

if __name__ == '__main__':
    main() # Invoking all test functions in DatabaseTests class
