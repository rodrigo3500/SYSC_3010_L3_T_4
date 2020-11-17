from gpiozero import LED
from time import sleep

def test_LEDs():
    red = LED(25)
    green = LED(8)
    
    for i in range(3):
        red.on()
        green.on()
        sleep(0.5)
        red.off()
        green.off()
        
if __name__ == "__main__":
    test_LEDs()