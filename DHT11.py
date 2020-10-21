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
