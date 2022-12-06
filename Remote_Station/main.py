# Remote Station

#IR Infrared Sensor

from machine import Pin, PWM
import utime
import socket, network

print("Busy/Availble Remote Station")

busyLedPin = 18
availableLedPin = 17
#Lower LED value
busyLed = Pin(busyLedPin, Pin.OUT)
availableLed = Pin(availableLedPin, Pin.OUT)

busyPWM = PWM(busyLed)
availablePWM = PWM(availableLed)
busyPWM.freq(1000)
availablePWM.freq(10000)

busyPWM.duty_u16(15000)
availablePWM.duty_u16(10000)

pir = Pin(16, Pin.IN, Pin.PULL_DOWN)

import connectToWlan

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'

ipInfo= connectToWlan.connectWLAN(ssid, password)
print(ipInfo)


import website

html = website.html

 
# Open socket
while True:
    try:
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(50)
        print('listening on', addr)
        break
    except Exception as e:
        print(f"except 68: {e}")
        utime.sleep(0)
        pass
    
    
    
def openSocket():
    print("Open Socket Started")
    while True:
        cl, addr = s.accept()
        request = cl.recv(1024)
        print(request)
        requestString = request
        

        if "Busy=Busy" in requestString:
            busyPWM.duty_u16(15000)
            availablePWM.duty_u16(0)
            
            response = html % f"Busy Ok"
            
            
        elif "Available=Available" in requestString:
            busyPWM.duty_u16(0)
            availablePWM.duty_u16(10000)
            response = html % f"Available Ok"
            
        elif "reload=Reload" in requestString:         
            response = html % f"Reload Ok"
            
        else:
            print("not a valid request")
            response = html % f"Invalid Request"
        
    

        #response = html % f""
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        print(str(requestString).split("duration="))
        #utime.sleep(int(requestString.split("=")))
        #request = requests.get("192.168.88.147/?Available=Available&duration=")
        #print(request.url)
        
        
def motionDetection():
    print(pir.value())
    utime.sleep(.4)
    if pir.value():
        #Send request to enable LED on Base Syste
        print("test")
        busyPWM.duty_u16(15000)
        availablePWM.duty_u16(0)
    else:
        busyPWM.duty_u16(0)
        availablePWM.duty_u16(10000)
        
while True:
    openSocket()
    

