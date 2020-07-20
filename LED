------------------------------------------BLOG POST #1------------------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Turn LED on

# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Turn LED ON

import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.on()

------------------------------------------BLOG POST #1------------------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Blink with Delay

import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
while True:
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.5)
    
-----------------------------------------BLOG POST #2------------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Blink custom number of times

import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
n=int(input("Enter the number of Blinks you need : "))
for i in range(n):
    pin.off()
    time.sleep(0.5)
    pin.on()
    time.sleep(0.5)
    
