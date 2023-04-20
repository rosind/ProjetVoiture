import time
import RPi.GPIO as GPIO
class CapteurInfrarouge:
    """Capteur TCRT5000 --> Pin 20"""
    def __init__(self,pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.IN)
        self.pin = pin
    def detect(self):
        detect = False
        if GPIO.input(self.pin):
            #print("Je détecte la ligne noir!")
            detectLigne = True
            time.sleep(0.2)
        else:
            #print("Je ne détecte pas la ligne noir !")
            detectLigne = False
            time.sleep(0.2)

        return detectLigne
class CapteurUltrason:
    """Capteur HC-SR04 --> trig=26 echo=19 (capteur droit) // trig=11 echo=9 (capteur gauche) // trig=6 echo=5 (avant)"""
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    def distance(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        pulseStart = time.time()
        while GPIO.input(self.echo)==0:
            pulseStart = time.time()

        pulseEnd = time.time()
        while GPIO.input(self.echo)==1:
            pulseEnd = time.time()

        pulseTotal= pulseEnd-pulseStart
        distance = pulseTotal*17150 #vitesse du son/2
        distance = round(distance,2)
        if (distance > 120): #Permet de définir les bornes du capteur
            distance=120
        elif (distance < 5):
            distance=5

        return distance

    def clean(self):
        GPIO.cleanup()

class CapteurRGBDetector:
    """Capteur TCS3472"""
    pass

class TriangulationVoiture:
    def __init__(self):
        self.capteur_droit = CapteurUltrason(trig=26, echo=19)
        self.capteur_gauche = CapteurUltrason(trig=11, echo=9)
        self.capteur_avant = CapteurUltrason(trig=6, echo=5)
        self.x = 0
        self.y = 0

    def trianguler_position(self):
        # positions des capteurs
        pos_droit = (0, 0)
        pos_gauche = (0, 10)
        pos_avant = (5, 5)

        # boucle principale pour la triangulation
        while True:
            distance_droit = self.capteur_droit.distance()
            distance_gauche = self.capteur_gauche.distance()
            distance_avant = self.capteur_avant.distance()

            # calcul de la position de la voiture
            trilat = Trilateration(pos_droit, pos_gauche, pos_avant)
            self.x, self.y = trilat.trilaterate(distance_droit, distance_gauche, distance_avant)

    def get_position(self):
        return self.x, self.y
