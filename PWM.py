-----------------------------------------BLOG POST #3----------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#PWM, LED fade

from machine import Pin, PWM
from time import sleep
frequency = 5000
led = PWM(Pin(2), frequency)
while True:
  for duty_cycle in range(0, 1024):
    led.duty(duty_cycle)
    sleep(0.005)
