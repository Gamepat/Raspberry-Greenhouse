#!/usr/bin/python
from picamera import PiCamera
import thingspeak
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setwarnings(False)

channel_id = 694063
write_key  = 'QNIM0VZ4VDTZKAW7'
read_key   = 'XEMY9SF60QSDKH0R'
pin = 4
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

camera = PiCamera()

def measure(channel):
	try:
        	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	        # write
	        response = channel.update({'field1': temperature, 'field2': humidity})
		print("Measured")
    	except:
        	print("connection failed")
 
 
if __name__ == "__main__":
    	channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
   	while True:
		dt = list(time.localtime())
		hr = dt[3]
		min = dt[4]
		sec = dt[5]

		if hr == 9 and min == 0:
			GPIO.output(27, GPIO.LOW)
		elif hr == 21 and min == 0:
			GPIO.output(27, GPIO.HIGH)

		measure(channel)
		camera.start_preview()
        	time.sleep(15)
		camera.capture('/home/pi/Desktop/img.jpg')
		camera.stop_preview()
	GPIO.cleanup()
