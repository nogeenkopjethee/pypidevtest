#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

BuzzerPin = 37    # pin37

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BuzzerPin, GPIO.OUT)
	GPIO.output(BuzzerPin, GPIO.LOW)

def loop():
	loopTime = 0.5

	while True:
		GPIO.output(BuzzerPin, GPIO.HIGH)
		time.sleep(loopTime)
		GPIO.output(BuzzerPin, GPIO.LOW)
		time.sleep(loopTime)
		loopTime = loopTime / 1.1
		print(loopTime)
		
		if loopTime < 0.001:
			loopTime = 0.5

def destroy():
	GPIO.output(BuzzerPin, GPIO.LOW)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

