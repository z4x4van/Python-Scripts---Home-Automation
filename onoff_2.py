import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

SleepTimeL = 1

GPIO.output(2,GPIO.LOW)
time.sleep(SleepTimeL)
GPIO.cleanup()
