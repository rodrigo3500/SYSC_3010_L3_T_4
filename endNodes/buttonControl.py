# Author: Hari
# Setup input buttons and uses interrupts to trigger actions inside program
import RPi.GPIO as GPIO
import capacityControl as capacityControl

# DEPRICATED
increaseCapacity = 1
decreaseCapacity = 2
noChange = 0

# GPIO ports used for button input
increaseButtonPin = 23
decreaseButtonPin = 24

# setting up button GPIO button inputs
def setupButtons():
    GPIO.setmode(GPIO.BCM) # restricted to BCM because of chosen Sonar Sensor library
    # Defining button GPIO ports and inputs
    GPIO.setup(increaseButtonPin,GPIO.IN)
    GPIO.setup(decreaseButtonPin,GPIO.IN)
    # Setting up event listeners. Since a pull down resistor is used in the design, a rising edge dictates a button press
    GPIO.add_event_detect(increaseButtonPin, GPIO.RISING)
    # Interrupt based programming
    GPIO.add_event_callback(increaseButtonPin, callIncreaseCap)
    GPIO.add_event_detect(decreaseButtonPin, GPIO.RISING)
    GPIO.add_event_callback(decreaseButtonPin, callDecreaseCap)

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

# callback function to update values when up button pressed
def callIncreaseCap(callBack):
    capacityControl.increaseCapacity()

# callback function to update values when down button pressed
def callDecreaseCap(callBack):
    capacityControl.decreaseCapacity()

