# Busy-or-Available-Remote-Lights
Signal if busy or available to speak to a light outside the door from 2 buttons inside the office

Research:
- Wireless Antenna/radio frequency transciever that i have


2 Components

1st - Local Controller:
- Pico W
- Red Button - Busy
- Green Button - Available
- RGB-LED - Connected to Remote Station Status
- - Red - Busy Signal
- - Green - Available (If Battery powered then no lights/deep sleep mode to conserve power)
- - Blue - Motion Detected



2nd - Remote Station 
- Pico W
- RGB-LED 
- - Red - Busy Signal
- - Green - Available (If Battery powered then no lights/deep sleep mode to conserve power)
- - Blue - Motion Detected
- Proximity Sensor
- - IR PIR
- - Passive Infared (PIR) https://www.sparkfun.com/products/13285
- - Lidar 
- - W Wave? Youtube video about motion detection from it





Links:
https://electronics.stackexchange.com/questions/513096/reducing-ir-proximity-sensor-module-power-consumption
https://www.seeedstudio.com/blog/2019/12/19/all-about-proximity-sensors-which-type-to-use/
