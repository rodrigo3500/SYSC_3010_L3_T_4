import requests
import json


def clearChannel():
    print("test")
    try:
        channel_id = 1224300
        mydata = {}
        mydata['api_key'] = 'VF11C85OPY3Q5UR6'
        url = "http://api.thingspeak.com:80/channels/" + str(channel_id) + "/feeds.json"
        jsondata = json.dumps(mydata)
        r = requests.delete(url, params=mydata)
        print(r.status_code)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    clearChannel()
