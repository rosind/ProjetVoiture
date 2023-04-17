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
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig,GPIO.IN)
        GPIO.setup(echo, GPIO.OUT)

        self.trig = trig
        self.echo = echo
    def distance(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(self.echo)==0:
            pulse_start = time.time()

        while GPIO.input(self.echo)==1:
            pulse_end = time.time()

        pulse_duree = pulse_end - pulse_start

        distance = pulse_duree * 17150
        distance = round(distance, 2)
        return distance
    def cleanup(self):
        GPIO.cleanup()

class CapteurRGBDetector:
    """Capteur TCS3472"""
    pass