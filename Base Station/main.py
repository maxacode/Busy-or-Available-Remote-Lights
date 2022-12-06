#Capastive touch test


import utime
import rp2
from rp2 import PIO, asm_pio
from machine import Pin, mem32
pinIn1 = 16
pinIn2 = 17
    
@asm_pio(set_init=rp2.PIO.OUT_HIGH)
def GetTouchPulse():
    set(pindirs,0)
    set(x,0)
    label('loopH1')
    jmp(x_dec,'loopH2')
    label('loopH2')
    nop()
    jmp( pin, 'loopH1')
    mov(isr,x)
    push()
    label('done')
    jmp('done')

try:

    while True:

        pinInVar1 = Pin(pinIn1,Pin.OUT,Pin.PULL_DOWN)
        pinInVar1.value(1)
        sm1 = rp2.StateMachine(0,GetTouchPulse,in_base=pinInVar1,jmp_pin=pinInVar1,set_base=pinInVar1,freq=125_000_000)
        sm1.active(1)
        pinInVar1Value = 0xffffffff-sm1.get()
        print(f"Blue: {pinInVar1Value}")
        utime.sleep_ms(500)
        
        pinInVar2 = Pin(pinIn2,Pin.OUT,Pin.PULL_DOWN)
        pinInVar2.value(1)
        sm2 = rp2.StateMachine(0,GetTouchPulse,in_base=pinInVar2,jmp_pin=pinInVar2,set_base=pinInVar2,freq=125_000_000)
        sm2.active(1)
        pinInVar2Value = 0xffffffff-sm2.get()
        print(f"White: {pinInVar2Value}")
        utime.sleep_ms(500)
        
except KeyboardInterrupt:
        pass
    