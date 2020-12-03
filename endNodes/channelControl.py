# Author: Hari
# Contains all methods required to upload messages to thingspeak
import requests
import json
import urllib.parse as urlencode

w_key = "NHGIKFM0VW4TGHDA" # L3_T_4a2 write key
user_key = "VF11C85OPY3Q5UR6"
channel_id = 1224300

# Clearing all the data in the channel. Good for testing to ensure that the environment is in a known state
def clearChannel():
    try:
        mydata = {}
        mydata['api_key'] = user_key
        url = "http://api.thingspeak.com:80/channels/" + str(channel_id) + "/feeds.json"
        jsondata = json.dumps(mydata)
        r = requests.delete(url,params=mydata)
        return r.status_code
    except Exception as e:
        print (e)

# uploading datapoint of a person entering a room
def uploadPersonEntering(roomId, occupants, time):
    return uploadPersonEnterExitRoomData("enter",roomId,occupants,time)

# uploading datapoint of a person exiting a room
def uploadPersonExiting(roomId, occupants, time):
    return uploadPersonEnterExitRoomData("exit",roomId,occupants,time)

# uploading datapoint when increasing room capacity
def uploadIncreasedCapacity(roomId, newLimit, time):
    return uploadMaxCapChangeData("max capacity increased", roomId, newLimit, time)

# uploading datapoint with decreasing room capacity
def uploadDecreasedCapacity(roomId, newLimit, time):
    return uploadMaxCapChangeData("max capacity decreased", roomId, newLimit, time)

def uploadPersonEnterExitRoomData(action, roomId, occupants, time):
    return writeData(action, roomId, occupants, time.__str__())

def uploadMaxCapChangeData(action, roomId, newLimit, time):
    return writeData(action, roomId, newLimit, time.__str__())

def uploadMaxCapReachedData(roomId, time):
    return writeData("max capacity reached", roomId, "", time.__str__())

# Writing data to thingspeak
def writeData(field1, field2, field3, field4):
    try:
        params = {'field1': field1, 'field2':field2, 'field3':field3, 'field4':field4, 'key':w_key}
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        url = "http://api.thingspeak.com:80/update"
        r = requests.post(url, params=params, headers=headers)
        return r.status_code
    except Exception as e:
        print(e)
