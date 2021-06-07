# 라즈베리파이에 연결된 온열매트를 작동시키는 코드

import os
import glob
import time
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

w = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(w, GPIO.OUT)
GPIO.output(w, 0)

w1_device_file = '/sys/devices/w1_bus_master1/28-00000c981cd6/temperature'
 
def read_temp_raw():
   f = open(w1_device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines[0] 

while True:
    value = float(read_temp_raw()) / 1000.0
    
    print("CEL temperature = %.1f" %value)
   
    
    if value <= 20 :
        GPIO.output(w, 1)
   
    elif value >= 25:
        GPIO.output(w, 0)
    
    time.sleep(1)
