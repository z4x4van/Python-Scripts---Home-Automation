import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
if GPIO.input(4):
        print("Closing Garage Door (Relay 2)")
        GPIO.output(3,GPIO.LOW)
        time.sleep(1)
        GPIO.output(3,GPIO.HIGH)
        GPIO.cleanup()
else:
        print("Opening Garage Door (Relay 1)")
        GPIO.output(2,GPIO.LOW)
        time.sleep(1)
        GPIO.output(2,GPIO.HIGH)
        GPIO.cleanup()
