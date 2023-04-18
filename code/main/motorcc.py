import RPi.GPIO as GPIO
import time as sleep
import PCA9685 as p

class motorcc : 
    pwm = p.PWM()
    pwm.frequency = 60
    def __init__(self,A,B):
        GPIO.setmode(GPIO.BOARD)
        self.A = A
        self.B = B

    def advance(self) : 
        # On configure toutes les pins
        GPIO.setup(A, GPIO.OUT)
        GPIO.setup(B, GPIO.OUT)

        while True : 
            GPIO.output(A, GPIO.HIGH)
            GPIO.output(B, GPIO.LOW)

    
    def backward(self):
        GPIO.setup(A, GPIO.OUT)
        GPIO.setup(B, GPIO.OUT)

        while True : 
            GPIO.output(A, GPIO.LOW)
            GPIO.output(B, GPIO.HIGH)

    def setSpeed(self,speed):

        self.speed = speed #percent représente le pourcentage de vitesse
        EN_M0 = 4  
        EN_M1 = 5 
        print ('speed is: ', speed)
        pwm.write(EN_M0, 0, speed)
        pwm.write(EN_M1, 0, speed)

    def cleanup(self): 
        GPIO.cleanup()
