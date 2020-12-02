# Author: Hari
# Setup input buttons and uses interrupts to trigger actions inside program
import RPi.GPIO as GPIO
import capacityControl as capacityControl

increaseCapacity = 1
decreaseCapacity = 2
noChange = 0

# setting up button GPIO button inputs
def setupButtons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.IN)
    GPIO.add_event_detect(23, GPIO.RISING)
    GPIO.add_event_callback(23, callIncreaseCap)
    GPIO.add_event_detect(24, GPIO.RISING)
    GPIO.add_event_callback(24, callDecreaseCap)

# Read if the up button is pressed or not
# DEPRICATED
def readUpButton():
    if(GPIO.input(16)==GPIO.HIGH):
        return True
    else:
        return False

# Read if the down button is pressed or not
# DEPRICATED 
def readDownButton():
    if(GPIO.input(18)==GPIO.HIGH):
        return True
    else:
        return False

# Determine if the user wants to increase of decrement the capacity
# DEPRICATED
def readButtonInputs():
    upPressed = readUpButton()
    downPressed = readDownButton()
    if(upPressed and (not downPressed)):
        return increaseCapacity
    elif(downPressed and (not upPressed)):
        return decreaseCapacity
    return noChange

# callback function to update values when incremented
def callIncreaseCap(callBack):
    capacityControl.increaseCapacity()

# callback function to update values when decremented
def callDecreaseCap(callBack):
    capacityControl.decreaseCapacity()

