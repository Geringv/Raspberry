#import dependencies
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

#variables
sensoren = [17,27]
pumpen = [5,6]
count1 = 0
count2 = 0
now = datetime.now() #current date and time
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #formatting


#numbering
GPIO.setmode(GPIO.BCM)
#pin setup
GPIO.setup(sensoren,GPIO.IN)
GPIO.setup(pumpen,GPIO.OUT,initial = 1)

#variable function for watering
def watering(sensorID,pumpeID,pflanzeID,gießzeit):
    if GPIO.input(sensoren[sensorID]) == 1: #check moisture sensor for dryness
        print(f"plant {pflanzeID} dry")
        GPIO.output(pumpen[pumpeID],0) #turn pump on
        sleep(gießzeit) #water plant for x seconds
        GPIO.output(pumpen[pumpeID],1) #turn pump off
        count1 += 1
        
        with open('log.txt', 'a') as f: #open txt file
            f.write('\n'.join(f"{dt_string} : plant {pflanzeID} watered")) #write content to txt file
        
        print(f"plant {pflanzeID} watered " + str(count1) + " times")
    else:
        print(f"plant {pflanzeID} wet")

#executing
try:
    while True:
        watering(0,0,1,3) #plant 1 checked / watered
        watering(1,1,2,3) #plant 2 checked / watered
        sleep(1) #sleep for 1 second to save cpu

except KeyboardInterrupt: #quit if strg + c is pressed
    GPIO.output(pumpen,False) # set pumps to off
    GPIO.cleanup() #free cpu
