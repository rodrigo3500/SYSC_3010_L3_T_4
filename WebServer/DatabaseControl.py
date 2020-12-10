from unittest import TestCase, main
from sqlite3 import connect, Error
from random import choice
from requests import get
from time import sleep
import smtplib


"""
Setup for the email functionality 
A gmail account is required
You also have to turn on "App Access' in your Gmail security settings
Otherwise, it'll fail authentication. (SMTPAuthenticationError)
Sends the email with the contents of the parameter as the content
"""


def send_email(roomID):

    mail = smtplib.SMTP('smpt.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    # Sender email and password
    mail.login('email', 'password')

    # Parameters:  sender , recipient, content
    mail.sendmail('sender', 'recipient', 'Max Capacity Reached for node: ' +  roomID )

    mail.close()


db_file = "system.db" # path to database
conn = None # to store database connection

"""
Returns a list of all Manager IDs from database
"""
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

"""
Generates a unique random ID for every new Manager
"""
def generateManagerID():
    ids = getManagerIDs()
    newID = choice([i for i in range(0,1000) if i not in ids]) # Creating a new unique id here

    return newID

"""
Generates a unique random ID for every new Room
"""
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

"""
Adds a new Manager to database
"""
def addManager(firstName, lastName, email, phoneNumber):
    if (len(firstName) < 1 or len(firstName) > 20): # First name must be between 1 and 20 characters long (inclusive)
        print("first")
        return False
    if (len(lastName) < 1 or len(lastName) > 20): # Last name must be between 1 and 20 characters long (inclusive)
        print("last")
        return False
    if (len(email) < 6 or len(email) > 40 or '@' not in email): # Email must be between 6 and 40 characters long (inclusive)
        print("email")
        return False
    if (not (len(str(phoneNumber)) == 10)): # Phone number must be 10 digits long
        print(len(str(phoneNumber)))
        print("phone")
        return False

    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    managerID = generateManagerID() # Creating new unique Manager ID for new Manager

    command = '''INSERT INTO Manager VALUES (?, ?, ?, ?, ?)'''
    csr.execute(command, (str(managerID), firstName, lastName, email, str(phoneNumber))) # Executing write here
    conn.commit()
    conn.close()

    return True

"""
Adds a new Room to database
"""
def addRoom(capacity, managerID):
    ids = getManagerIDs()

    if (managerID not in ids): # Room must always be associated with a Manager
        return False
    if (capacity < 1): # Capacity of room must always be at least 1 to create a new room
        return False

    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    roomID = generateRoomID() # Creating new unique Room ID for new Room
    currentSize = 0 # 0 people in a Room when first created

    command = '''INSERT INTO Room VALUES (?, ?, ?, ?)'''
    csr.execute(command, (str(roomID), str(currentSize), str(capacity), str(managerID))) # Executing write here
    conn.commit()
    conn.close()

    return True

"""
Removes Manager and all associated Rooms from database
"""
def removeManager(managerID):
    # Creating connection to database
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    csr = conn.cursor() # Creating cursor to access database

    command1 = '''DELETE FROM Manager WHERE managerID = ?''' # To remove Manager
    csr.execute(command1, (str(managerID),))
    command2 = '''DELETE FROM Room WHERE managerID = ?''' # To remove Rooms associated with Manager
    csr.execute(command2, (str(managerID),))
    conn.commit()
    conn.close()

"""
Removes Room from database
"""
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
Checks if any emails need to be sent
"""
def checkForEmail():




"""
Puts JSON entry from ThingSpeak into a dictionary
"""
def sendRecentData():
    URL = 'https://api.thingspeak.com/channels/1224300/feeds.json?api_key='
    R_KEY = "1IF97D5OLYHPX0ER"  # L3_T_4a2 read key
    HEADER = '&results=30' # Getting last 30 entries from ThingSpeak
    recentEntries = get(URL+R_KEY+HEADER).json()["feeds"] # All 30 entries stored in one list

    # Iterates over every entry from list
    for entry in recentEntries:
        print(entry)
        #print("==========================================================================")

        if len(entry) == 6:
            action = entry["field1"]
            roomID = entry["field2"]
            newValue = entry["field3"]

            if action == "max capacity reached ":#if the max capacity of a room is reached, send email notification
                send_email(roomID)
            if action == "enter" or action == "exit": # If a person enters or exits Room, currentOccupancy in databse is updated
                updateCurrentOccupancy(roomID, newValue)
            elif action == "max capacity increased" or action == "max capacity decreased": # If the capacity of a Room increases or decreases, capacity in database updated
                updateMaxOccupancy(roomID, newValue)

if __name__ == '__main__':
    while (True): # Periodic timing loop
        sendRecentData()
        print("====================================================================================================================================================================================")
        sleep(10) # Request last 30 entries every 10 seconds
