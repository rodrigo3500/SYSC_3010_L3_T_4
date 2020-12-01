# Author: Hari
# Controls the flow of the endnodes 
import buttonControl as buttonControl
import ledControl as ledControl
import LCDControl as LCDControl
import RPi.GPIO as GPIO

# Number of persons currently in the room 
currentOccupants = 0

# Max number of persons allowed in the room, default is 5
maxCapacity = 5

limitReached = False

# update the roop capacity based on user Input
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

# Decrease the room capacity by 1
def decreaseCapacity():
    global maxCapacity
    maxCapacity = maxCapacity - 1
    updateState()

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

def updateState():
    checkOccupants()
    updateLCD()
    updateLed()

# increase the number of persons in the room by 1
def increaseOccupants():
    global currentOccupants
    currentOccupants = currentOccupants + 1
    updateState()

# decrease the number of persons in the room by 1
def decreaseOccupants():
    global currentOccupants
    currentOccupants = currentOccupants - 1
    updateState()

# check to see if the room capacity has been reached
def checkOccupants():
    global limitReached
    if(currentOccupants >= maxCapacity):
        limitReached = True
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

if __name__=="__main__":
    buttonControl.setupButtons()
    LCDControl.setupLCD()
    ledControl.setUpLeds()
    updateState()
    try:
        while(True):
            x=1
    except KeyboardInterrupt:
        GPIO.cleanup()
