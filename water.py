import RPi.GPIO as GPIO
from time import sleep

sensor1 = 17
sensor2 = 27
pump1 = 5
pump2 = 6
count1 = 0
count2 = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
GPIO.setup(pump1,GPIO.OUT,initial = 1)
GPIO.setup(pump2,GPIO.OUT,initial = 1)
try:
    while True:
        if GPIO.input(sensor1) == 1:
            print("plant 1 dry")
            GPIO.output(pump1,0)
            sleep(3)
            GPIO.output(pump1,1)
            count1 += 1
            print("plant 1 watered " + str(count1) + " times")
            

        elif GPIO.input(sensor2) == 1:
            print("plant 2 dry")
            GPIO.output(pump2,0)
            sleep(3)
            GPIO.output(pump2,1)
            count2 += 1
            print("plant 1 watered " + str(count2) + " times")
            

        else:
            print("both plants wet")
        sleep(1)

except KeyboardInterrupt:
    GPIO.output(pump1,False)
    GPIO.output(pump2,False)
    GPIO.cleanup()