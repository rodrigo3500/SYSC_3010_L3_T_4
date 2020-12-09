#author: Carling Clough


from gpiozero import DistanceSensor
import datetime
from datetime import datetime
import time
from time import sleep
import capacityControl as capacityControl

#Sonar() detects if a person is entering or exiting a closed space. In the first two seconds of 
#run time, sensor 1 and sensor 2 will record the distance of the doorway. After the first two 
#seconds sonar continously reads the distance. If the distance read is less than the first 
#doorway measurment, a person has been detected. 
def sonar():
    
    global TimeDetected1 #time stamp sensor 1 detected a person
    global TimeDetected2 #time stamp sensor 2 dectected a person

   

    global MotionDetected1
    global MotionDetected2
    MotionDetected1 = False #Check if sensor 1 detected movement
    MotionDetected2 = False #Check if sensor 2 detected Movement



    t_sec = time.time() + 2 #First two seconds of Sonar() running

    

    ON = True
    
    #First two seconds.
    while time.time() < t_sec:
                
        FirstMeasurement1 = sensor1.distance*100 #distance between sensor 1 and doorway
        sleep(1)
        FirstMeasurement2 = sensor2.distance*100 #distance between sensor 2 and doorway
        #print('Measured distance to wall - sensor 1: {:.2f}'.format(FirstMeasurement1))
        #print('Measured distance to wall - sensor 2: {:.2f}'.format(FirstMeasurement2))
        sleep(1)
        
    #Continously read distance measurments after first two seconds.
    while ON:            
        distance1 = sensor1.distance*100 #get sensor 1 measured distance value
        distance2 = sensor2.distance*100 #get sensor 2 measured distance value
        
        sleep(0.2)
        
        #sensor 1 detects person
        if(distance1 < (FirstMeasurement1 -2)): #2cm margin of error
            TimeDetected1 = datetime.now() #time person was detected by sensor 2
            MotionDetected1 = True
            #print('Measured distance value - sensor 1: {:.2f}, time:{:.2f}, object sensed: '.format(distance1,TimeDetected1.microsecond),MotionDetected1)
            
        #sensor 2 detects person
        if(distance2 < (FirstMeasurement2 -2)): #2cm margin of error
            TimeDetected2 = datetime.now() #time person was detected by sensor 2
            MotionDetected2 = True
            #print('Measured distance value - sensor 2: {:.2f}, time: {:.2f}, object sensed: '.format(distance2,TimeDetected2.microsecond),MotionDetected2)
            
        #if both sensor 1 and sensor 2 have detected a person, compare time stamps to determine direction    
        if (MotionDetected1 and MotionDetected2):
            
            #sensor 1 detected a person first
            if(TimeDetected1<TimeDetected2): 
            
                PersonEnteredRoom()
                
            #sensor 2 detected a person first
            else: 
                PersonExitedRoom()
                
#Updates capacity if person has entered the closed space.            
def PersonEnteredRoom():

    print('Person has entered the room')
    capacityControl.increaseOccupants()
    time = TimeDetected2
    #uploadPersonEntering(roomId, occupants, time)
    sleep(2)
    clear()

    #write to thingspeak
    
    return

#Updates capacity if person has exited the closed space.
def PersonExitedRoom():

    print('Person has exited the room')
    capacityControl.decreaseOccupants() 
    time = TimeDetected1

    #uploadPersonExiting(roomId, occupants, time):
    sleep(2)
    clear()

    #write to thingspeak
    
    return
#resets Sonar() if the occupancy changed.
def clear():
    MotionDetected1 = False
    MotionDetected2 = False
    sonar()

#set up Ultrasonic sensors
def setupSonar():
    global sensor1
    sensor1 = DistanceSensor(echo=4, trigger=17)#outside the room
    global sensor2
    sensor2 = DistanceSensor(echo=27, trigger=22)#inside the room
    
if __name__=="__main__":
    setupSonar()
    sonar()
