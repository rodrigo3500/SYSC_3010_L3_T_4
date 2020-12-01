# Author: Hari
# Controls the red and green led indicators
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

# Constants
ON = 1 # GPIO output 1 = on
OFF = 0 # GPIO output 0 = off
red = 22 # GPIO board pin for red LED
green = 24 # GPIO board pin for green LED

# Setting up GPIO output pins
def setUpLeds():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(22, OFF)
    GPIO.output(24, ON)

# Change state of the red led
def redControl(state):
    global red
    GPIO.output(red, state)

# Change state of the green led
def greenControl(state):
    global green
    GPIO.output(green, state)

# Used to change the state of the specified led
# DEPRICATED
def ledControl(state, led):
    if(state==ON):
        led.on()
    elif(state==OFF):
        led.off()

# Turn on the red led and turn off green led. Used when current occupants has exceed the capacity
def aboveLimit():
    redControl(ON)
    greenControl(OFF)

# Turn on the green led and turn off the red led. Used when the current occupants has not yet reached the capacity
def belowLimit():
    redControl(OFF)
    greenControl(ON)
