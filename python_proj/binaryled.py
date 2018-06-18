import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
red = 17
red1 = 18
red2 = 27
red3 = 22
GPIO.setup(red, GPIO.OUT)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(red3, GPIO.OUT)
deci_num=input("Enter a number 0 through 15: ")
if deci_num == 0:
    GPIO.output(red, 0)
elif deci_num == 1:
    GPIO.output(red, True)
elif deci_num == 2:
    GPIO.output(red1, True)
elif deci_num == 3:
    GPIO.output(red, True)
    GPIO.output(red1, True)
elif deci_num == 4:
    GPIO.output(red2, True)
elif deci_num == 5:
    GPIO.output(red, True)
    GPIO.output(red2, True)
elif deci_num == 6:
    GPIO.output(red1, True)
    GPIO.output(red2, True)
elif deci_num == 7:
    GPIO.output(red, True)
    GPIO.output(red1, True)
    GPIO.output(red2, True)
elif deci_num == 8:
    GPIO.output(red3, True)
elif deci_num == 9:
    GPIO.output(red, True)
    GPIO.output(red3, True)
elif deci_num == 10:
    GPIO.output(red1, True)
    GPIO.output(red3, True)
elif deci_num == 11:
    GPIO.output(red, True)
    GPIO.output(red1, True)
    GPIO.output(red3, True)
elif deci_num == 12:
    GPIO.output(red2, True)
    GPIO.output(red3, True)
elif deci_num == 13:
    GPIO.output(red, True)
    GPIO.output(red2,True)
    GPIO.output(red3,True)
elif deci_num == 14:
    GPIO.output(red1, True)
    GPIO.output(red2, True)
    GPIO.output(red3, True)
elif deci_num == 15:
    GPIO.output(red, True)
    GPIO.output(red1, True)
    GPIO.output(red2, True)
    GPIO.output(red3, True)
else:
    print ("Enter a number between 0 and 15 next time...")
time.sleep(3)
GPIO.output(red, False)
GPIO.output(red1, False)
GPIO.output(red2, False)
GPIO.output(red3, False)
time.sleep(1)
GPIO.cleanup()
