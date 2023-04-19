import time
from capteurs import *
from Thread import *


class Race:
    def __init__(self):
        capteurAvant = CapteurUltrason(trig=6,echo=5)
        capteurDroite = CapteurUltrason(26, 19)
        capteurGauche = CapteurUltrason(11, 9)
        CapteurInfra = CapteurInfrarouge(20)

        threadCaptAvant = CapteurUltrasonThread(capteurAvant)
        threadCaptDroite = CapteurUltrasonThread(capteurDroite)
        threadCaptGauche = CapteurUltrasonThread(capteurGauche)
        threadInfra = CapteurInfrarougeThread(CapteurInfra.pin)

        threadCaptAvant.start()
        threadCaptDroite.start()
        threadCaptGauche.start()
        threadInfra.start()
        
    def race(self):
        self.threadInfra = InfraredSensor(laps)
        self.motor.moveForward(50)
        while self.infraredSensor.getLaps() > 0:
            self.infraredSensor.isOn()
            position_to_wall = self.sensorR.getDistance()
            self.servo.setAngleByDist(position_to_wall)
        self.motor.stopMove()
        
