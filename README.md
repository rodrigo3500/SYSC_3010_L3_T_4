# SYSC_3010_L3_T_4
Room Capacity Limiter Ultra

## Summary
In an effort to encourage social distancing during this COVID-19 pandemic, this system was developed to encourage social distancing.

## Features
* Detects individuals entering and leaving a room (one at a time)
* Logically prevents more individuals from entering a room once capacity is reached
* Displays room metrics on website
* Text and email notifications when capacity is reached

## Prerequisites
* Python 3.5
* GPIO Zero library
* CharLCD library
## Usage
1. Run ```python3 /endNodes/capacityControl.py``` on all secondary nodes
2. Run ```python3 /database/DatabaseControl.py``` on central node
3. <WEBPAGE STEP>

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
