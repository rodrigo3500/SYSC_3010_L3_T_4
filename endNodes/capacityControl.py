# Author: Hari
# Controls the flow of the endnodes 
import buttonControl as buttonControl
import ledControl as ledControl
import LCDbcmControl as LCDControl
import RPi.GPIO as GPIO
import channelControl as channelControl
import sonars as sonar
import datetime

# Number of persons currently in the room, system assumes room is empty as the start
currentOccupants = 0

# Max number of persons allowed in the room, default is 5
maxCapacity = 5

# Unique room id, different for each end node
roomId = 1

limitReached = False

# update the room capacity based on user Input
# DEPRICATED
def updateCapacity():
    global maxCapacity
    userInput = buttonControl.readButtonInputs()
    if(userIput is buttonControl.increaseCapacity):
        maxCapacity = maxCapacity + 1
    elif(userInput is buttonControl.decreaseCapacity):
        maxCapacity = maxCapacity - 1

# Increase the room capacity by 1
def increaseCapacity():
    global maxCapacity
    maxCapacity = maxCapacity + 1
    updateState()
    channelControl.uploadIncreasedCapacity(roomId, maxCapacity, datetime.datetime.now())


# Decrease the room capacity by 1. Cannot decrease the room capcaity if the room has reached its limit.
def decreaseCapacity():
    if(not limitReached):
        global maxCapacity
        maxCapacity = maxCapacity - 1
        updateState()
        channelControl.uploadDecreasedCapacity(roomId, maxCapacity, datetime.datetime.now())

# update the LCD screen
def updateLCD():
    global maxCapacity
    global currentOccupants
    LCDControl.writeToLCD(maxCapacity, currentOccupants)

# update the indicator led's 
def updateLed():
    if (not limitReached):
        ledControl.belowLimit()
    elif(limitReached):
        ledControl.aboveLimit()

# Update the state of limit reached and update LCD and led components
def updateState():
    checkOccupants()
    updateLCD()
    updateLed()

# increase the number of persons in the room by 1
def increaseOccupants():
    if(not limitReached):
        global currentOccupants
        currentOccupants = currentOccupants + 1
        updateState()
        channelControl.uploadPersonEntering(roomId, currentOccupants, datetime.datetime.now())

# decrease the number of persons in the room by 1
def decreaseOccupants():
    global currentOccupants
    currentOccupants = currentOccupants - 1
    updateState()
    channelControl.uploadPersonExiting(roomId, currentOccupants, datetime.datetime.now())

# check to see if the room capacity has been reached. IF reached, send message to thingspeak
def checkOccupants():
    global limitReached
    if(currentOccupants >= maxCapacity):
        limitReached = True
        channelControl.uploadMaxCapReachedData(roomId, datetime.datetime.now())
    elif(currentOccupants < maxCapacity):
        limitReached = False
    return limitReached

# turn on green and turn off red led if capacity hasnt been reached
# turn on red and turn off green led if capacity has been reached
# DEPRICATED
def updateLeds():
    global limitReached
    if(not limitReached):
        ledControl.belowLimit()
    elif(limitReached):
        ledControl.aboveLimit()

# Set up all harware compoonents and start sonar sensing loop
if __name__=="__main__":
    global maxCapacity
    global currentOccupants
    buttonControl.setupButtons()
    LCDControl.setupLCD(maxCapacity, currentOccupants)
    ledControl.setUpLeds()
    updateState()
    sonar.setupSonar()
    try:
        sonar.sonar()
    except KeyboardInterrupt:
        GPIO.cleanup()
