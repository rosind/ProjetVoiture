import time

import RPi.GPIO as GPIO
class CapteurInfrarouge:
    """Capteur TCRT5000"""
    def __init__(self,pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.IN)
        self.pin = pin
    def detect(self):
        while True:
            if GPIO.input(self.pin):
                print("Je détecte !")
                time.sleep(1)
            else:
                print("Je ne détecte pas !")
                time.sleep(1)