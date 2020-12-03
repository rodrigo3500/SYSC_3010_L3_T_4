from gpiozero import DistanceSensor
import time
from time import sleep

def test_sonar1():
        #test first ultrasonic sensor
    success1 = False
    success2 = False
    success = False
    end_time = time.time()+10
    t_sec = time.time() + 1
    sensor1 = DistanceSensor(echo=4, trigger=17)
    sensor2 = DistanceSensor(echo=27, trigger=22)

    #collect 10 different measurments for sensor 1 over a 10 second period
    while time.time() < end_time: 
            
        while time.time() < t_sec:
                
            distance1 = sensor1.distance*100
            print('Measured distance value - sensor 1: {:.2f}'.format(distance1))
            sleep(1)
        distance2 = sensor1.distance*100
        #test if next recorded measurement is within margin of error
        if(distance1 - 0.3 <= distance2 <= distance1 + 0.3): 
            success1 = True
            print('Measured distance value - sensor 1: {:.2f}, passed: {}'.format(distance2,success1))
            distance1 = distance2
            sleep(1)
        #break if test failed
        else: 
            success1 = False;
            break
    #test second ultrasonic sensor
    end_time2 = time.time() + 10
    t_sec1 = time.time() + 1
    #collect 10 different measurments for sensor 2 over a 10 second period
    while end_time <time.time() < end_time2: 
        while time.time() < t_sec1:
                
            distance1 = sensor2.distance*100
            print('Measured distance value - sensor 2: {:.2f}'.format(distance1))
            sleep(1)
        distance2 = sensor2.distance*100
        #test if next recorded measurement is within margin of error
        if(distance1 - 0.3 <= distance2 <= distance1 + 0.3): 
            success2 = True
            print('Measured distance value - sensor 2: {:.2f}, passed: {}'.format(distance2,success2))
            distance1 = distance2
            sleep(1)
        #break if test failed
        else: 
            success2 = False;
            print (distance2,success2)
            break
    #Check that both sensors passed
    if(success1 & success2): 
        success = True
    return success



def test_sonar():
    #returns true if all tests have passed
    success = False
    test = test_sonar1()

    if(test):
        print('All sensors successfully passed!')
        success = True
    
    return success
        

if __name__=='__main__':
    test_sonar()
