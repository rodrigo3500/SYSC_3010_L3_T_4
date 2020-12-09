# Author: Hari
import RPi.GPIO as GPIO
import unittest
import time

# Setup button as GPIO inputs. Ports are predesignated in the design doc.
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.IN)
    GPIO.setup(18,GPIO.IN)

class TestPushButtons(unittest.TestCase):
    
    # Setting a 5 second delay between prompt and start of test to give user adequate time to press or unpress the correct button
    def printDelay():
        print("Test starting in 5...")
        x = 4
        while (x > 0):
            time.sleep(1)
            print("{}...".format(x))
            x = x -1
        print("starting...")
    
    # Test for up button unpressed, required to test pull down resistor
    def test_upButtonUnpressed(self):
        print("Please do not touch any of the buttons")
        printDelay()
        secondsPassed = 0
        buttonNotPressed = 0
        while(secondsPassed <5):
            time.sleep(1)
            if(GPIO.input(16)==GPIO.LOW):
                buttonNotPressed = buttonNotPressed + 1
            secondsPassed = secondsPassed + 1
        self.assertEqual(5,buttonNotPressed)
        print()
    # Test for up button pressed
    def test_upButtonPressed(self):
        print("Please press the up button (RED cap), and hold until prompted to let go of the button")
        printDelay()
        secondsPassed = 0
        buttonPressed = 0
        while(secondsPassed < 5):
            time.sleep(1)
            if(GPIO.input(16)==GPIO.HIGH):
                buttonPressed = buttonPressed + 1
            secondsPassed = secondsPassed + 1
        print("Please let go of the button.")
        self.assertEqual(5,buttonPressed)
        print()
    
    # Test for down button unpressed, required to test pull down resistor
    def test_downButtonUnpressed(self):
        print("Please do not touch any of the buttons")
        printDelay()
        secondsPassed = 0
        buttonNotPressed = 0
        while(secondsPassed <5):
            time.sleep(1)
            if(GPIO.input(18)==GPIO.LOW):
                buttonNotPressed = buttonNotPressed + 1
            secondsPassed = secondsPassed + 1
        self.assertEqual(5,buttonNotPressed)
        print()

    # Test for down button pressed
    def test_downButtonPressed(self):
        print("Please press the down button (YELLOW cap), and hold until prompted to let go of the button")
        printDelay()
        secondsPassed = 0
        buttonPressed = 0
        while(secondsPassed < 5):
            time.sleep(1)
            if(GPIO.input(18)==GPIO.HIGH):
                buttonPressed = buttonPressed + 1
            secondsPassed = secondsPassed + 1
        print("Please let go of the button.")
        self.assertEqual(5,buttonPressed)
        print()

if __name__=="__main__":
    setup()
    unittest.main()
