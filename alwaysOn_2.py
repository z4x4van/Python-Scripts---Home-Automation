import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(2, GPIO.OUT)
try:
        while 1:
                if GPIO.input(4):
                        GPIO.output(2,GPIO.LOW)
                else:
                        print("Pin 4 is HIGH")
                        GPIO.output(2,GPIO.HIGH)
except KeyboardInterrupt:
        GPIO.cleanup()
