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
    """Capteur HC-SR04 --> trig=26 echo=19 """
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setmode = (GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    def distance(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        pulseStart = time.time()
        while GPIO.input(self.echo)==0:
            pulse_start = time.time()

        pulseEnd = time.time()
        while GPIO.input(self.echo)==1:
            pulse_end = time.time()

        pulseTotal= pulseEnd-pulseStart
        distance = pulseTotal*17150 #vitesse du son/2
        distance = round(distance,2)

        return distance

    def clean(self):
        GPIO.cleanup()

class CapteurRGBDetector:
    """Capteur TCS3472"""
    pass