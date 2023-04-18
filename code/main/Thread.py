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