import requests
import json

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


if __name__=="__main__":
    clearChannel()
