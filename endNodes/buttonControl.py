import RPi.GPIO as GPIO

increaseCapacity = 1
decreaseCapacity = 2
noChange = 0

# setting up button GPIO button inputs
def setupButtons():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.IN)
    GPIO.setup(18,GPIO.IN)

# Read if the up button is pressed or not
def readUpButton():
    if(GPIO.input(16)==GPIO.HIGH):
        return True
    else:
        return False

# Read if the down button is pressed or not
def readDownButton():
    if(GPIO.input(18)==GPIO.HIGH):
        return True
    else:
        return False

# Determine if the user wants to increase of decrement the capacity
def readButtonInputs():
    upPressed = readUpButton()
    downPressed = readDownButton()
    if(upPressed and (not downPressed)):
        return increaseCapacity
    elif(downPressed and (not upPressed)):
        return decreaseCapacity
    return noChange
