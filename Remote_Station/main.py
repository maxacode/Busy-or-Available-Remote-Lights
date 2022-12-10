


# Remote Station

#IR Infrared Sensor


from machine import Pin, PWM
import utime
import socket, network
import urequests as requests

import _thread

print("Busy/Availble Remote Station")

busyLedPin = 17
availableLedPin = 18
#Lower LED value
busyLed = Pin(busyLedPin, Pin.OUT)
availableLed = Pin(availableLedPin, Pin.OUT)

busyPWM = PWM(busyLed)
availablePWM = PWM(availableLed)
busyPWM.freq(1000)
availablePWM.freq(1000)

#busyPWM.duty_u16(20000)
availablePWM.duty_u16(40000)

pir = Pin(16, Pin.IN, Pin.PULL_DOWN)

import connectToWlan

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'

ipInfo= connectToWlan.connectWLAN()
print(ipInfo)

 
#ipInfo= connectToWlan.connectWLAN()
#print(ipInfo)


import website

html = website.html

 
# Open socket
#def listener():
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
        utime.sleep(0.2)
        pass

    
def openSocket():

    
    
    print("Open Socket Started")
    while True:
        try:
            cl = ''
            cl, addr = s.accept()
            request = cl.recv(1024)
            print(request)
            requestString = request
            

            if "Busy=Busy" in requestString:
                busyPWM.duty_u16(15000)
                availablePWM.duty_u16(0)
                
                response = "Busy Ok"
                
                
            elif "Available=Available" in requestString:
                busyPWM.duty_u16(0)
                availablePWM.duty_u16(10000)
                response = "Available Ok"
                
            elif "reload=Reload" in requestString:         
                response = "Reload Ok"
                
            else:
                print("not a valid request")
                response = "Invalid Request"
            
        

            #response = html % f""
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
            #print(str(requestString).split("duration="))
            #utime.sleep(int(requestString.split("=")))
            #request = requests.get("192.168.88.147/?Available=Available&duration=")
            #print(request.url)
        except Exception as error:
            print(f"Error on 101: {error}")
            pass
        
def pirDetected():
    while True:
        try:
            while True:
                print(pir.value())
                if pir.value():
                    #Send request to enable LED on Base Syste
                    print("Sending PIR Alert to Base")
                    #busyPWM.duty_u16(15000)
                    #availablePWM.duty_u16(0)
                    #print(requests.get(url = "http://192.168.88.115/PIR-Detected"))

                    response = requests.get(url = "http://192.168.88.115/PIR-Detected").text
                   # response.close()
                    
                    #print(response)
                    #utime.sleep(3)
                    #print(response.url)
                   # print(response.text)          
                utime.sleep(.5)
        except Exception as error:
            print(error)
            pass

#openSocketThread = _thread.start_new_thread(openSocket, ())

#utime.sleep(5)
#pirDetected()
pirThread = _thread.start_new_thread(pirDetected, ())
#listener()
#openSocket()

 

