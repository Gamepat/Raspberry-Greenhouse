#!/usr/bin/python
import thingspeak
import time
import Adafruit_DHT
 
channel_id = 694063
write_key  = 'QNIM0VZ4VDTZKAW7'
read_key   = 'XEMY9SF60QSDKH0R'
pin = 4
sensor = Adafruit_DHT.DHT11
 
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
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)
