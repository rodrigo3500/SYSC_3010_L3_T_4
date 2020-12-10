# SYSC_3010_L3_T_4
Room Capacity Limiter Ultra

## Summary
Room Capacity Limiter Ultra was developed to encourage social distancing during the COVID-19 pandemic of 2020.

## Features
* Detects individuals entering and leaving a room (one at a time)
* Logically prevents more individuals from entering a room once capacity is reached
* Displays room metrics on website
* Email notifications when capacity is reached

## Prerequisites
Data Collection Node
* Python 3.5
* GPIO Zero library; comes preinstalled with RPi os
* CharLCD library; ```sudo pip3 install adafruit-circuitpython-charlcd```

Central Data Node
* Install Apache 2, PHP 7.3, and SQLite 3 on Pi
* Obtain RPi’s IP address by running ```$hostname -I``` 
* Ensure Apache 2 Web Server is running on the Pi by visiting IPaddress/index.html in any browser connected to the same network, where IPaddress is the one assigned to the Rpi

## Usage
Data Collection Node
1. Run ```python3 /endNodes/capacityControl.py``` on all secondary nodes
2. Ensure Apache 2 is running on central node

Central Data Node
1. Download the contents of /Webserver folder to /var/www/html folder on Rpi
2. Run python3 /WebServer/database/DatabaseControls.py folder on central node
3. Open any browser on the same network as the Pi, and navigate to the following site, where the url is the local IP address of the RPi
```Http://{rpi ip address}:80```

## Troubleshooting
### Hardware Tests
* LEDs Test: ```python3 /Demo2/test_hw.py```
* LCD Test: ```python3 /Demo2/lcdTest.py```
* Buttons Test: ```python3 /Demo2/pushButtonTest.py```
* Sensors Test: ```python3 /Demo2/test_sonar.py```

### End-to-End Tests
* Test LEDs: ```python3 /Demo2/test_1-5.py```
* Test LEDs: ```python3 /Demo2/test_6-8.py```

### Database Test
* Run ```python3 /Demo2/test_db.py```

## License
[MIT](https://choosealicense.com/licenses/mit/)
