from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

button1 = 16
button2 = 12
LED1 = 22
LED2 = 18

GPIO.setup(button1, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
pwm1 = GPIO.PWM(LED1, 1000)
pwm2 = GPIO.PWM(LED2, 1000)
pwm1.start(0)
pwm2.start(0)
bright = 1
while(1):
    if GPIO.input(button1) == 0:
        print "Button 1 was pressed"
        bright = bright / 1.25
        pwm1.ChangeDutyCycle(bright)
        pwm2.ChangeDutyCycle(bright)
        sleep(.25)
        print "Your brightness is: " , bright
    if GPIO.input(button2) == 0:
        print "Button 2 was pressed"
        bright = bright * 1.25
        if bright > 100:
            bright = 100
            print "You are at full brightness"
        pwm1.ChangeDutyCycle(bright)
        pwm2.ChangeDutyCycle(bright)
        sleep(.25)
        print "Your brightness is: ", bright
