# install: sudo pip3 install RPLCD
# tutorial on: https://www.digikey.com/en/maker/blogs/2018/how-to-connect-a-raspberry-pi-to-a-16-x-2-lcd-display
# Author: Hari
# controls the 2x16 LCD for information display
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time

# Columns in the lcd 
column = 16

# Rows in the lcd
row = 2

# lcd object used to modify the LCD screen
lcd = None

# GPIO pins used to connect to LCD, can be found in the design docs
rs = 10
e = 8
db4 = 12
db5 = 36
db6 = 38
db7 = 40

# Setting up the LCD GPIO pins and display default message at the start
def setupLCD():
    global lcd
    lcd = CharLCD(pin_rs=rs, pin_e=e, pin_rw=None, pins_data=[db4,db5,db6,db7], numbering_mode = GPIO.BOARD,cols=column,rows=row,dotsize=8)
    writeToLCD(5,0)

'''
LCD display message format:
    Max Capacity: x
    Current: y
'''
def writeToLCD(capacity, current):
    global lcd
    lcd.clear()
    lcd.cursor_pos=(0,0)
    lcd.write_string("Max Capacity: {cap}".format(cap=capacity))
    lcd.cursor_pos=(1,0)
    lcd.write_string("Current Occ: {curr}".format(curr=current))

