import RPi.GPIO as GPIO
import time as sleep

class motorcc : 
    def __init__(self,EN,A,B):
        GPIO.setmode(GPIO.BCM)
        self.EN = EN
        self.A = A
        self.B = B

    def advance(self) : 
        # On configure toutes les pins
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(A, GPIO.OUT)
        GPIO.setup(B, GPIO.OUT)

        while True : 
            GPIO.output(EN, GPIO.HIGH)
            GPIO.output(A, GPIO.HIGH)
            GPIO.output(B, GPIO.LOW)

    
    def backward(self):
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(A, GPIO.OUT)
        GPIO.setup(B, GPIO.OUT)

        while True : 
            GPIO.output(EN, GPIO.HIGH)
            GPIO.output(A, GPIO.LOW)
            GPIO.output(B, GPIO.HIGH)

    def speed(self,percent):
        self.percent=percent #percent représente le pourcentage de vitesse
        freq = GPIO.PWM(EN, 100)

        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(A, GPIO.OUT)
        GPIO.setup(B, GPIO.OUT)

        while True : 
            freq.start(percent)
            GPIO.output(A, GPIO.HIGH)
            GPIO.output(B, GPIO.LOW)

    def cleanup(self): 
        GPIO.cleanup()
