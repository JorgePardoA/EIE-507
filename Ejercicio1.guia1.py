import serial
from serial import Serial
Arduino = serial.Serial('/dev/ttyACM0',9600)

while True:
	read_serial = Arduino.readline()
	print (read_serial)		
