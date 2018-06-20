import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
red = 11
GPIO.setup(red, GPIO.OUT)
my_pwm = GPIO.PWM(red, 100)
my_pwm.start(0)
while (1):
    bright = input("How Bright do you want the LED? (0-7) ")
    if (bright != 7 and bright != 0):
        my_pwm.ChangeDutyCycle(2**bright)
    elif (bright == 0):
        my_pwm.ChangeDutyCycle(0)
    else:
        my_pwm.ChangeDutyCycle(100)
my_pwm.stop()
GPIO.cleanup()
