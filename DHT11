--------------------------------------BLOG POST #4--------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Read Temperature Sensor

from machine import Pin
from time import sleep
import dht
sensor = dht.DHT11(Pin(14))
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = print('Temperature:',sensor.temperature(),'*C','\n')
    hum = print('Humidity:',sensor.humidity(),'%','\n','-----------')
  except OSError as e:
    print('Failed to read sensor.')

-------------------------------------BLOG POST #4-----------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#DHT-11 based simple Alert System.

import machine
pin1 = machine.Pin(5, machine.Pin.OUT)
pin2 = machine.Pin(14, machine.Pin.OUT)
from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(4))

while True:
  try:
    sleep(2)
    sensor.measure()
    print('Temperature:',sensor.temperature(),'*C','\n')
    print('Humidity:',sensor.humidity(),'%','\n','-------------------')
  except OSError as e:
    print('Failed to read sensor.')

  if sensor.temperature() >33:
      pin1.on()
      print('Temperature:',sensor.temperature(),'*C',"Temperature is High(>33*C)",'\n')
  else:
      pin1.off()
        
  if sensor.humidity() > 90:
      pin2.on()
      print('Humidity:',sensor.humidity(),'%',"Humidity is High(>90%)",'\n','-------------------')
  else:
      pin2.off()
