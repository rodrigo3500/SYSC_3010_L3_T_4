from unittest import TestCase, main
from sqlite3 import connect, Error
from random import choice

db_file = "system.db" # path to database
conn = None # to store database connection

def getManagerIDs():
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command = '''SELECT managerID FROM Manager'''
    csr.execute(command) # Executing read here
    data = csr.fetchall() # Storing read data into a list
    conn.close()

    # Cleaning up IDs from database here
    ids = []
    for r in data:
        ids.append(r[0])

    return ids

def generateManagerID():
    ids = getManagerIDs()
    newID = choice([i for i in range(0,1000) if i not in ids]) # Creating a new unique id here

    return newID

def generateRoomID():
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command = '''SELECT roomID FROM Room'''
    csr.execute(command) # Executing read here
    data = csr.fetchall() # Storing read data into a list
    conn.close()

    # Cleaning up IDs from database here
    ids = []
    for r in data:
        ids.append(r[0])

    newID = choice([i for i in range(0,1000) if i not in ids]) # Creating a new unique id here

    return newID

def addManager(firstName, lastName, email, phoneNumber):
    if (len(firstName) < 1 or len(firstName) > 20):
        return False
    if (len(lastName) < 1 or len(lastName) > 20):
        return False
    if (len(email) < 6 or len(email) > 40 or '@' not in email):
        return False

    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    managerID = generateManagerID()

    command = '''INSERT INTO Manager VALUES (?, ?, ?, ?, ?)'''
    csr.execute(command, (str(managerID), firstName, lastName, email, str(phoneNumber))) # Executing write here
    conn.commit()
    conn.close()

    return True

def addRoom(capacity, managerID):
    ids = getManagerIDs()

    if (managerID not in ids):
        return False
    if (capacity < 1):
        return False

    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    roomID = generateRoomID()
    currentSize= 0

    command = '''INSERT INTO Room VALUES (?, ?, ?, ?)'''
    csr.execute(command, (str(roomID), str(currentSize), str(capacity), str(managerID))) # Executing write here
    conn.commit()
    conn.close()

    return True

def removeManager(managerID):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command1 = '''DELETE FROM Manager WHERE managerID = ?'''
    csr.execute(command1, (str(managerID),))
    command2 = '''DELETE FROM Room WHERE managerID = ?'''
    csr.execute(command2, (str(managerID),))
    conn.commit()
    conn.close()

def removeRoom(roomID):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command = '''DELETE FROM Room WHERE roomID = ?'''
    csr.execute(command, (str(roomID),))
    conn.commit()
    conn.close()


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
def sendRecentData():
    #URL = 'https://api.thingspeak.com/channels/1224300/feeds.json?api_key='
    #R_KEY = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key
    #HEADER = '&results=5'
    #recentEntries = requests.get(URL+R_KEY+HEADER).json()["feeds"]
    recentEntries = {
        "Entry_1": {
             "Field 1": "enter",
             "Field 2": 1000,
             "Field 3": 5,
             "Field 4": "time"
        },
        "Entry_2": {
            "Field 1": "exit",
            "Field 2": 1000,
            "Field 3": 3,
            "Field 4": "time"
        },
        "Entry_3": {
            "Field 1": "max capacity increased",
            "Field 2": 1000,
            "Field 3": 6,
            "Field 4": "time"
        },
        "Entry_4": {
            "Field 1": "max capacity decreased",
            "Field 2": 1000,
            "Field 3": 4,
            "Field 4": "time"
        },
        "Entry_5": {
            "Field 1": "max capacity reached",
            "Field 2": 1000,
            "Field 3": "",
            "Field 4": "time"
        }
    }

    for entry in recentEntries.items():
        fields = entry[1]
        if (len(fields) == 4):
            action = fields["Field 1"]
            roomID = fields["Field 2"]
            newValue = fields["Field 3"]

            if (action == "enter" or action == "exit"):
                updateCurrentOccupancy(roomID, newValue)
            elif (action == "max capacity increased" or action == "max capacity decreased"):
                updateMaxOccupancy(roomID, newValue)

# Resetting values before running tests
updateCurrentOccupancy(1000, 0) # Resetting current occupancy to 0
updateMaxOccupancy(1000, 0) # Resetting max occupancy to 0

if __name__ == '__main__':
    #sendRecentData()
    #generateManagerID()
    #print(getManagerIDs())
    #print(addRoom(capacity=0, managerID=2))
