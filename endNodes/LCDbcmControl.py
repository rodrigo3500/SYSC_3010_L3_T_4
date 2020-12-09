# install: sudo pip3 install adafruit-circuitpython-charlcd
# Tutorial on lcd/library basics can be found at: https://learn.adafruit.com/character-lcds/python-circuitpython
# Author: Hari

import board
import digitalio
import adafruit_character_lcd.character_lcd as charLcd

# Columns in the LCD
lcdColumns = 16

# Rows in the LCD
lcdRows = 2

'''
LCD display message format:
    Max Capacity: x
    Current: y
'''
messageFormat = "Max Capacity: {capacity}\nCurrent: {current}"

# lcd object used to modify LCD screen
lcd = None

# Setting up the LCD GPIO pins and display default message at start
def setupLCD(cap, curr):
    lcd_rs = digitalio.DigitalInOut(board.D15)
    lcd_en = digitalio.DigitalInOut(board.D14)
    lcd_d7 = digitalio.DigitalInOut(board.D21)
    lcd_d6 = digitalio.DigitalInOut(board.D20)
    lcd_d5 = digitalio.DigitalInOut(board.D16)
    lcd_d4 = digitalio.DigitalInOut(board.D18)
    global lcd
    lcd = charLcd.Character_LCD_Mono(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcdColumns, lcdRows)
    lcd.clear()
    writeToLcd(cap, curr)

# Update the LCD to display updated room metrics
def writeToLCD(cap, curr):
    global lcd
    lcd.message=messageFormat.format(capacity=cap,current=curr)
