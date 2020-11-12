import requests
import json
import urllib.parse as urlencode

w_key = "NHGIKFM0VW4TGHDA" # L3_T_4a2 write key
#w_key = "R2E49ELP96PB9RCX" 


def clearChannel():
    try:
        channel_id =1224300
        mydata = {}
        mydata['api_key'] = 'VF11C85OPY3Q5UR6'
        url = "http://api.thingspeak.com:80/channels/" + str(channel_id) + "/feeds.json"
        jsondata = json.dumps(mydata)
        r = requests.delete(url,params=mydata)
        return r.status_code
    except Exception as e:
        print (e)

def uploadPersonEnterExitRoomData(action, roomId, occupants, time):
    return uploadData(action, roomId, occupants, time.__str__())

def uploadMaxCapChangeData(action, roomId, newMax, time):
    return uploadData(action, roomId, newMax, time.__str__())

def uploadMaxCapReachedData(action, roomId, time):
    return uploadData(action, roomId, "", time.__str__())


def uploadData(field1, field2, field3, field4):
    try:
        params = {'field1': field1, 'field2':field2, 'field3':field3, 'field4':field4, 'key':w_key}
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        url = "http://api.thingspeak.com:80/update"
        r = requests.post(url, params=params, headers=headers)
        return r.status_code
    except Exception as e:
        print(e)
