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

class CapteurInfrarougeThread(threading.Thread):
    def __init__(self, pin):
        threading.Thread.__init__(self)
        self.capteur = CapteurInfrarouge(pin)
        self.running = True
        self.etat = False

    def run(self):
        while (self.running):
            if self.capteur.detect():
                #print("detect ok")
                self.etat = True
            else:
                #print("detect ko")
                self.etat = False


            time.sleep(0.1)

    def stop(self):
        self.running = False

class ThreadTriangulation:
    def __init__(self, triangulation):
        self.triangulation = triangulation
        self.thread_droit = threading.Thread(target=self.mesure_capteur, args=(self.triangulation.capteur_droit,))
        self.thread_gauche = threading.Thread(target=self.mesure_capteur, args=(self.triangulation.capteur_gauche,))
        self.thread_avant = threading.Thread(target=self.mesure_capteur, args=(self.triangulation.capteur_avant,))

    def mesure_capteur(self, capteur):
        while True:
            capteur.distance()

    def start(self):
        self.thread_droit.start()
        self.thread_gauche.start()
        self.thread_avant.start()

    def join(self):
        self.thread_droit.join()
        self.thread_gauche.join()
        self.thread_avant.join()
