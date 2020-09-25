## NOTE: cleanexit does not work yet!!!

#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import signal

ledPin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

while True:
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(1)

def cleanexit():
    GPIO.cleanup()

# By using signal, I can gracefully exit the GPIO application.
# Thanks, StackOverflow!!!
# https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python

signal.signal(signal.SIGINT, cleanexit)