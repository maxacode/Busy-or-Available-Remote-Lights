# Remote Station

#IR Infrared Sensor
from machine import Pin, PWM
import utime

print("Starting IRIS")

led = Pin(17, Pin.OUT)
pwm = PWM(led)
pwm.freq(1000)
pwm.duty_u16(1000)

iris = Pin(16, Pin.IN)

while True:
    print(" ")
    print(iris.value())
    if iris.value() == 1:
        led.value(0)
        pwm.duty_u16(1000)

    else:
        led.value(1)
        pwm.duty_u16(20000)

    utime.sleep(.5)
        