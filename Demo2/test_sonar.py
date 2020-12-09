#Author: Carling Clough
from gpiozero import DistanceSensor
import time
from time import sleep

#test_sonar1() tests if sensors one and two are stable and able to read its enviroment correctly. 
#10 distance measurments will be taken over a period of 10 seconds for each sensor. 
#If all measurments recorded are within the ultrasonic sensors margin of error (0.3cm), all test
#successfully pass.
def test_sonar1():
        
    
    success1 = False #True if sensor 1 passes test
    success2 = False #True if sensor 2 passes test
    success = False #True if sensor 1 and sensor 2 pass all tests
    sensor1 = DistanceSensor(echo=4, trigger=17) #set up sensor 1
    sensor2 = DistanceSensor(echo=27, trigger=22) #set up sensor 2
        
    #test first ultrasonic sensor 

    end_time = time.time()+10
    t_sec = time.time() + 1
    

    #collect 10 different measurments for sensor 1 over a 10 second period
    while time.time() < end_time: 
        
        #get first distance measurment from sensor 1
        while time.time() < t_sec:
                
            distance1 = sensor1.distance*100
            print('Measured distance value - sensor 1: {:.2f}'.format(distance1))
            sleep(1)
        
        #get next distance measurment from sensor 1
        distance2 = sensor1.distance*100
        
        
        #if next recorded distance measurment passes
        if(distance1 - 0.3 <= distance2 <= distance1 + 0.3): #distance2 is within distance1's margin of error
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
        
        #get first distance measurment from sensor 2
        while time.time() < t_sec1: 
                
            distance1 = sensor2.distance*100
            print('Measured distance value - sensor 2: {:.2f}'.format(distance1))
            sleep(1)
        
        #get next distance measurment from sensor 2
        distance2 = sensor2.distance*100
        
        #if next recorded distance measurment passes
        if(distance1 - 0.3 <= distance2 <= distance1 + 0.3): #distance2 is within distance1's margin of error
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

    #if all tests are positive
    if(test):
        print('All sensors successfully passed!')
        success = True
    
    return success
        

if __name__=='__main__':
    test_sonar()
