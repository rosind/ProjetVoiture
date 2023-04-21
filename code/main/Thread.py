from capteurs import *
from servo import *
import threading
class CapteurUltrasonThread(threading.Thread):
    def __init__(self, capteur):
        threading.Thread.__init__(self)
        self.capteur = capteur
        self.distance = None
        self.running = False
    def run(self):
        self.running = True
        while self.running:
            self.distance = self.capteur.distance()
            time.sleep(0.1)
    def stop(self):
        self.running = False
        #self.capteur.clean()

class CapteurInfrarougeThread(threading.Thread):
    def __init__(self, pin):
        threading.Thread.__init__(self)
        self.capteur = CapteurInfrarouge(pin)
        self.running = True
        self.etat = False
        self.passeligne = self.capteur.detect()

    def run(self):
        while (self.running):
            self.passeligne = self.capteur.detect()
            if self.capteur.detect():
                #print("detect ok")
                self.etat = True
            else:
                #print("detect ko")
                self.etat = False


            time.sleep(0.1)

    def stop(self):
        self.running = False

class VoitureThread(threading.Thread):
    def __init__(self,voiture,speed):
        threading.Thread.__init__(self)
        self.voiture=voiture
        self.voiture = Voiture(speed)
        self.running = True
    def run(self):
        while (self.running):
            pass
    def stop(self):
        self.running=False

