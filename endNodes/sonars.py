#author: Carling Clough


from gpiozero import DistanceSensor
import datetime
from datetime import datetime
import time
from time import sleep
import capacityControl as capacityControl

def sonar():

    global TimeDetected1
    global TimeDetected2

   

    global MotionDetected1
    global MotionDetected2
    MotionDetected1 = False #Check if sensor 1 detected movement
    MotionDetected2 = False #Check if sensor 2 detected Movement



    t_sec = time.time() + 2

    

    ON = True
    
    while time.time() < t_sec:
                
        FirstMeasurement1 = sensor1.distance*100
        sleep(1)
        FirstMeasurement2 = sensor2.distance*100
        #print('Measured distance to wall - sensor 1: {:.2f}'.format(FirstMeasurement1))
        #print('Measured distance to wall - sensor 2: {:.2f}'.format(FirstMeasurement2))
        sleep(1)
    while ON:            
        distance1 = sensor1.distance*100 #get sensor 1 measured distance value
        distance2 = sensor2.distance*100 #get sensor 2 measured distance value
        
        sleep(0.2)
        
        #sensor 1 detects person
        if(distance1 < (FirstMeasurement1 -2)): 
            TimeDetected1 = datetime.now() #get time person was detected by sensor 2
            MotionDetected1 = True
            #print('Measured distance value - sensor 1: {:.2f}, time:{:.2f}, object sensed: '.format(distance1,TimeDetected1.microsecond),MotionDetected1)
            
        #sensor 2 detects person        
        if(distance2 < (FirstMeasurement2 -2)):
            TimeDetected2 = datetime.now()#get time person was detected by sensor 2
            MotionDetected2 = True
            #print('Measured distance value - sensor 2: {:.2f}, time: {:.2f}, object sensed: '.format(distance2,TimeDetected2.microsecond),MotionDetected2)
            
            
        if (MotionDetected1 and MotionDetected2):
            
            #getDirection
            if(TimeDetected1<TimeDetected2):
            
                PersonEnteredRoom()
    
            else: #if sensor 2 detected a person first
                PersonExitedRoom()
                
             
def PersonEnteredRoom():

    print('Person has entered the room')
    capacityControl.increaseOccupants()
    time = TimeDetected2
    #uploadPersonEntering(roomId, occupants, time)
    sleep(2)
    clear()

    #write to thingspeak
    
    return
def PersonExitedRoom():

    print('Person has exited the room')
    capacityControl.decreaseOccupants() 
    time = TimeDetected1

    #uploadPersonExiting(roomId, occupants, time):
    sleep(2)
    clear()

    #write to thingspeak
    
    return

def clear():
    MotionDetected1 = False
    MotionDetected2 = False
    sonar()

def setupSonar():
    global sensor1
    sensor1 = DistanceSensor(echo=4, trigger=17)#outside the room
    global sensor2
    sensor2 = DistanceSensor(echo=27, trigger=22)#inside the room
    
if __name__=="__main__":
    setupSonar()
    sonar()
