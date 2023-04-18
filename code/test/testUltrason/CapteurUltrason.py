#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class CapteurUltrason():
    def __init__(self, trig, echo):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig,GPIO.IN)
        GPIO.setup(echo, GPIO.OUT)

        self.trig = trig
        self.echo = echo

        

    def setup(self):
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

    def distance(self):

        pulse_start = 0
        pulse_end = 0
        pulse_duree = 0

        self.setup()
        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(0.0001)
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)

        while GPIO.input(self.echo)==0:
            pulse_start = time.time()
        
        while GPIO.input(self.echo_pin)==1:
            pulse_end = time.time()

        self.pulse_duree = self.pulse_end - self.pulse_start

        distance = self.pulse_duree


        distance = self.pulse_duree * 17150
        distance = round(distance, 2)

        if distance > 2:
            return distance - 0.5
        else :
            return 0
    
    def cleanup(self):
        GPIO.cleanup()

    


