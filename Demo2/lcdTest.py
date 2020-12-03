# install: sudo pip3 install adafruit-circuitpython-charlcd
# https://learn.adafruit.com/character-lcds/python-circuitpython
import board
import unittest
import digitalio
import adafruit_character_lcd.character_lcd as charLcd
lcd_rs = digitalio.DigitalInOut(board.D15)
lcd_en = digitalio.DigitalInOut(board.D14)
lcd_d7 = digitalio.DigitalInOut(board.D21)
lcd_d6 = digitalio.DigitalInOut(board.D20)
lcd_d5 = digitalio.DigitalInOut(board.D16)
lcd_d4 = digitalio.DigitalInOut(board.D18)
lcd_columns=16
lcd_rows=2

lcd = charLcd.Character_LCD_Mono(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns, lcd_rows)


def setup():
    lcd_rs = digitalio.DigitalInOut(board.D15)
    lcd_en = digitalio.DigitalInOut(board.D14)
    lcd_d7 = digitalio.DigitalInOut(board.D21)
    lcd_d6 = digitalio.DigitalInOut(board.D20)
    lcd_d5 = digitalio.DigitalInOut(board.D16)
    lcd_d4 = digitalio.DigitalInOut(board.D18)
    lcd_columns=16
    lcd_rows=2
    lcd = charLcd.Character_LCD_Mono(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns, lcd_rows)
    lcd.clear()

class TestLCD(unittest.TestCase):
    def test_LCD_Write(self):
        lcd.message="Hello\nJoseph!"
        didDisplayCorrectly = input("If the test displayed in the LCD is \"Hello Joseph\" enter (y) else enter (n)")
        self.assertEqual("y",didDisplayCorrectly)
        lcd.clear()

if __name__=="__main__":
    setup()
    unittest.main()
