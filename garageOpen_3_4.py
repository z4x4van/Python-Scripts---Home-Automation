import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)
if GPIO.input(4):
        print("Already Open")
        GPIO.output(3,GPIO.HIGH)
        GPIO.cleanup()
else:
        print("Closing Garage Door")
        GPIO.output(3,GPIO.LOW)
        time.sleep(1)
        GPIO.output(3,GPIO.HIGH)
        GPIO.cleanup()
