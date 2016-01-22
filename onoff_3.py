import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.HIGH)

SleepTimeL = 1

GPIO.output(3,GPIO.LOW)
time.sleep(SleepTimeL)
GPIO.cleanup()
