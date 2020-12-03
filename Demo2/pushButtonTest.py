import RPi.GPIO as GPIO
import unittest
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.IN)
    GPIO.setup(18,GPIO.IN)

class TestPushButtons(unittest.TestCase):
    def test_upButtonUnpressed(self):
        print("Please do not touch any of the buttons")
        print("Test starting in 5...")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("starting...")
        secondsPassed = 0
        buttonNotPressed = 0
        while(secondsPassed <5):
            time.sleep(1)
            if(GPIO.input(16)==GPIO.LOW):
                buttonNotPressed = buttonNotPressed + 1
            secondsPassed = secondsPassed + 1
        self.assertEqual(5,buttonNotPressed)
        print()

    def test_upButtonPressed(self):
        print("Please press the up button (RED cap), and hold until prompted to let go of the button")
        print("Test starting in 5...")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Starting...")
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

    def test_downButtonUnpressed(self):
        print("Please do not touch any of the buttons")
        print("Test starting in 5...")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("starting...")
        secondsPassed = 0
        buttonNotPressed = 0
        while(secondsPassed <5):
            time.sleep(1)
            if(GPIO.input(18)==GPIO.LOW):
                buttonNotPressed = buttonNotPressed + 1
            secondsPassed = secondsPassed + 1
        self.assertEqual(5,buttonNotPressed)
        print()

    def test_downButtonPressed(self):
        print("Please press the down button (YELLOW cap), and hold until prompted to let go of the button")
        print("Test starting in 5...")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Starting...")
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
