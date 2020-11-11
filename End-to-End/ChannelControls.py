import requests
import json
import urllib.parse as urlencode

w_key = "NHGIKFM0VW4TGHDA" # L3_T_4a2 write key

def clearChannel():
    try:
        channel_id =1216791
        mydata = {}
        mydata['api_key'] = '4X1V8UAUXRKAOI9F'
        url = "http://api.thingspeak.com:80/channels/" + str(channel_id) + "/feeds.json"
        jsondata = json.dumps(mydata)
        r = requests.delete(url,params=mydata)
        print(r.status_code)
    except Exception as e:
        print (e)

def uploadPersonEnterExitRoomData(action, roomId, occupants, time):
    return uploadData(action, roomId, occupants, time)

def uploadMaxCapChangeData(action, roomId, newMax, time):
    return uploadData(action, roomId, newMax, time)

def uploadMaxCapReachedData(action, roomId, time):
    return uploadData(action, roomId, "", time)


def uploadData(field1, field2, field3, field4):
    try:
        params = {'field1': field1, 'field2':field2, 'field3':field3, 'field4':field3, 'key':w_key}
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        url = "http://api.thingspeak.com:80/update"
        r = requests.post(url, params=params, headers=headers)
        return r.status_code
    except Exception as e:
        print(e)
