import time
import RPi.GPIO as GPIO
class CapteurInfrarouge:
    """Capteur TCRT5000 --> Pin 20"""
    def __init__(self,pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.IN)
        self.pin = pin
    def detect(self):
        while True:
            if GPIO.input(self.pin):
                print("Je détecte la ligne noir!")
                time.sleep(0.2)
            else:
                print("Je ne détecte pas la ligne noir !")
                time.sleep(0.2)
class CapteurUltrason():
    def __init__(self, trig, echo):
        GPIO.setmode(GPIO.BCM) #mode de numérotation des pins
        GPIO.setup(trig, GPIO.OUT) #sortie Trig branchée au GPIO 37
        GPIO.setup(echo, GPIO.IN) #entrée Echo branchée au GPIO 35

        GPIO.output(trig, False)
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo)==0: ## Emission de l'ultrason
            debutImpulsion = time.time()
        
        while GPIO.input(echo)==1: ## Retour de l'Echo
            finImpulsion = time.time()

        distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1) ## Vitesse du son = 340 m/s

        print ("La distance est de : ",distance," cm")

        #GPIO.cleanup()

class CapteurRGBDetector:
    """Capteur TCS3472"""
    pass