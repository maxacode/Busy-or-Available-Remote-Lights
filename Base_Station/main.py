#Capastive touch test

#base station

import utime
import rp2
from rp2 import PIO, asm_pio
from machine import Pin, mem32
import connectToWlan

import urequests as requests
 
ipInfo= connectToWlan.connectWLAN()
print(ipInfo)

pinIn1 = 16
pinIn2 = 17
redPin = 10
greenPin = 9
bluePin = 8

redLed = Pin(redPin, Pin.OUT)
blueLed = Pin(bluePin, Pin.OUT)
greenLed = Pin(greenPin, Pin.OUT)

redLed.value(1)
blueLed.value(1)
greenLed.value(1)
utime.sleep(1)
redLed.value(0)
blueLed.value(0)
greenLed.value(0)

 

# @asm_pio(set_init=rp2.PIO.OUT_HIGH)
# def GetTouchPulse():
#     set(pindirs,0)
#     set(x,0)
#     label('loopH1')
#     jmp(x_dec,'loopH2')
#     label('loopH2')
#     nop()
#     jmp( pin, 'loopH1')
#     mov(isr,x)
#     push()
#     label('done')
#     jmp('done')

#     while True:

#         pinInVar1 = Pin(pinIn1,Pin.OUT,Pin.PULL_DOWN)
#         pinInVar1.value(1)
#         sm1 = rp2.StateMachine(0,GetTouchPulse,in_base=pinInVar1,jmp_pin=pinInVar1,set_base=pinInVar1,freq=125_000_000)
#         sm1.active(1)
#         pinInVar1Value = 0xffffffff-sm1.get()
#         print(f"Blue: {pinInVar1Value}")
#         utime.sleep_ms(500)
        
#         pinInVar2 = Pin(pinIn2,Pin.OUT,Pin.PULL_DOWN)
#         pinInVar2.value(1)
#         sm2 = rp2.StateMachine(0,GetTouchPulse,in_base=pinInVar2,jmp_pin=pinInVar2,set_base=pinInVar2,freq=125_000_000)
#         sm2.active(1)
#         pinInVar2Value = 0xffffffff-sm2.get()
#         print(f"White: {pinInVar2Value}")
#         utime.sleep_ms(500)
        

    
    
def openSocketStart():
    print("Open Socket Started")
    try:
        while True:
            cl = ''
            cl, addr = s.accept()
            request = cl.recv(1024)
            print(request)
            requestString = request
            import json
            

            if "PIR-Detected" in requestString:           
                #response = html % f"PIR Ok"
                print("flashing blue light")
                response =  '{"Alerted":"True"}'
               # y = json.loads(responseText)
                #print(y)
                           
                #response = y

                for x in range(0,3):
                    blueLed.value(1)
                    utime.sleep(.5)
                    blueLed.value(0)
                    utime.sleep(.3)
      

            elif "Available=Available" in requestString:
                response = html % "Available Ok"
                print("Sending Available Request")
                responseReq = requests.get(url = 'http://192.168.88.147/?Available=Available&duration=')
                print(responeReq)
                            
            

            elif "Busy=Busy" in requestString:
                response = html % "Busy Ok"
                print("Sending Busy Request")
                responseReq = requests.get(url = 'http://192.168.88.147/?Busy=Busy&duration=')
                print(responeReq)
                
            else:
                print("not a valid request")
                response = html % f"Invalid Request"
            
        

            #response = html % f""
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
           # print(str(requestString).split("duration="))
            #utime.sleep(int(requestString.split("=")))
            #request = requests.get("192.168.88.147/?Available=Available&duration=")
            #print(request.url)
    except Exception as error:
            response = "Not Ok - error: " + str(error)
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
import socket, network
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

        
        
#request = requests.get(url = "192.168.88.147/?Available=Available&duration=")
#http://192.168.88.147/?Busy=Busy&duration=
#request = requests.get(url = "http://192.168.88.147/?Busy=Busy&duration=")
#utime.sleep(2)
#request = requests.get(url = "http://192.168.88.147/?Available=Available&duration=")

while True:
    openSocketStart()
    

