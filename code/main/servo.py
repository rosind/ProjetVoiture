#!/usr/bin/env python
import PCA9685 as servo
import time
from motorcc import *
from Thread import *
from capteurs import *

class Voiture:
    def __init__(self,speed):
        self.speed = speed
        self.voiture = drive(self.speed)
        self.pwm = servo.PWM()
        self.pwm.frequency = 50
        self.value=350

        self.ultrasonGauche = CapteurUltrason(11,9)
        self.ultrasonDroite = CapteurUltrason(26,19)
        self.ultrasonAvant = CapteurUltrason(6,5)
        self.capt1 = CapteurInfrarouge(20)

        self.th1=CapteurUltrasonThread(self.ultrasonGauche)
        self.th2=CapteurUltrasonThread(self.ultrasonDroite)
        self.th3=CapteurUltrasonThread(self.ultrasonAvant)
        self.th4=CapteurInfrarougeThread(self.capt1.pin)

        self.th1.start()
        self.th2.start()
        self.th3.start()
        self.th4.start()

    def stopThread(self):
        self.th1.stop()
        self.th2.stop()
        self.th3.stop()
        self.th4.stop()
        
    def detectLine(self):
        self.detectLine()
    
    def changeSpeed(self,speed):
        self.speed = speed

    def right(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            print("Valeur comprise entre 250 et 450")
        else:
            self.pwm.write(0,0,self.value + a)
            print("Tourne à droite", a, ' (', self.value + a, ')')

    def left(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            print("Valeur comprise entre 250 et 450")
        else: 
            self.pwm.write(0,0,150)#self.value - a)
            print("Tourne à gauche", a, ' (', self.value + a, ')')
    
    def start(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            print("Valeur comprise entre 250 et 450")
        else: 
            self.pwm.write(0,0,300)
            print("position de départ")

    def turn(self,angle):
        self.pwm.write(0,0,angle)
        print("tourne à un angle de : ",angle,"degrés")

    def servo_test(self):
        if self.value < 300 or self.value > 420:
            print("Valeur comprise entre 250 et 450")
        else:
            self.pwm.write(0,0,225)
            time.sleep(1)
            self.pwm.write(0,0,300)
            time.sleep(1)
            self.pwm.write(0,0,375)
            time.sleep(1)
            self.pwm.write(0,0,299)

    def stop_servo(self):
        self.pwm.write(0,0,0)

    def stop_voiture(self):
        self.stop_servo()
        self.voiture.stop()

    def cercle(self):
        self.voiture.set_speed()
        self.start()
        self.stop_voiture()
        self.right()
        time.sleep(1)
        self.voiture.move_forward()
        time.sleep(5)
        self.stop_voiture()
        time.sleep(0.5)
        # self.start()
        # time.sleep(2)
        self.left()
        time.sleep(1)
        self.voiture.move_forward()
        time.sleep(5)
        self.voiture.stop()
        time.sleep(1)
        self.start()
        time.sleep(1.5)
        self.stop_servo()
        
    def avance(self):
        self.voiture.set_speed()
        self.voiture.move_forward()

    def recule(self):
        self.voiture.set_speed()
        self.voiture.move_backward()
        
    def suivreMur(self):
        self.start()
        time.sleep(0.5)
        self.avance()
        if (self.th1.distance <= 15):
            self.turn(390) # vitesse de base : 410
            time.sleep(0.5) 
            self.avance()
        elif(self.th2.distance <= 15):
            self.turn(200) # vitesse de base : 150
            time.sleep(0.5)
            self.avance()
        elif(self.th3.distance <= 20):
            self.stop_voiture()
            self.recule()
            time.sleep(2)
            self.stop_voiture()
            if(self.th1.distance<self.th2.distance):
                 self.turn(390)
                 time.sleep(0.5)
                 self.avance()
                 time.sleep(1)
                 self.stop_voiture()
            else : 
                 self.turn(200)
                 time.sleep(0.5)
                 self.avance()
                 time.sleep(1)
                 self.stop_voiture()
        else : 
            self.avance()
