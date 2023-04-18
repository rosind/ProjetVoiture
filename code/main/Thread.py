from capteurs import *
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
    def get_distance(self):
        return self.distance

class CapteurInfrarougeThread(threading.Thread):
    """Capteur TCRT5000 --> Pin 20"""
    def __init__(self, pin):
        threading.Thread.__init__(self)
        self.pin = pin
        self.detectLigne = False
        self.running = True
    def run(self):
        while self.running:
            if GPIO.input(self.pin):
                self.detectLigne = True
                time.sleep(0.2)
            else:
                self.detectLigne = False
                time.sleep(0.2)

    def stop(self):
        self.running = False

    def detect(self):
        return self.detectLigne