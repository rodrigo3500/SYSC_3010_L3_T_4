from gpiozero import LED
from time import sleep

"""
Blinks red and green LEDs simultaneously 3 times
"""
def test_LEDs():
    red = LED(25) # red LED connected to GPIO pin 25
    green = LED(8) # green LED connected to GPIO pin 8
    
    # Red and green LEDs blink simultaneously 3 times with a 500ms delay between each blink
    for i in range(3):
        red.on()
        green.on()
        sleep(0.5)
        red.off()
        green.off()
        sleep(0.5)

if __name__ == "__main__":
    test_LEDs()
