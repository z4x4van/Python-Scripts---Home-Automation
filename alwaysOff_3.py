import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)
try:
        while 1:
                if GPIO.input(4):
                        GPIO.output(3,GPIO.HIGH)
                else:
                        print("Pin 4 is LOW")
                        GPIO.output(3,GPIO.LOW)
except KeyboardInterrupt:
        GPIO.cleanup()
