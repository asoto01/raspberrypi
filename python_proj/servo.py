import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin = 11
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(0)
for i in range (0, 20):
    desiredPosition = input("Where do you want the servo? (0,180) ")
    DC = (1/20.0) * (desiredPosition) + 2.8
    pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()
