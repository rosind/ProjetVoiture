#!/usr/bin/env python
import PCA9685 as servo
import time
from motorcc import *
import Thread
from capteurs import *

class Voiture:
    def __init__(self,speed):
        self.speed = speed
        self.voiture = drive(self.speed*40)
        self.pwm = servo.PWM()
        self.pwm.frequency = 50
        self.value=350

        self.ultrasonGauche = CapteurUltrason(11,9)
        self.ultrasonDroite = CapteurUltrason(26,19)
        self.ultrasonAvant = CapteurUltrason(6,5)
        self.capt1 = CapteurInfrarouge(20)

        self.th1=Thread.CapteurUltrasonThread(self.ultrasonGauche)
        self.th2=Thread.CapteurUltrasonThread(self.ultrasonDroite)
        self.th3=Thread.CapteurUltrasonThread(self.ultrasonAvant)
        self.th4=Thread.CapteurInfrarougeThread(self.capt1.pin)


    def startThread(self):
        self.th1.start()
        self.th2.start()
        self.th3.start()
        self.th4.start()

    def stopThread(self):
        self.th1.stop()
        self.th2.stop()
        self.th3.stop()
        self.th4.stop()

    def detect_Line(self):
        return self.th4.passeligne

    def changeSpeed(self,speed):
        self.speed = speed

    def right(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            pass
        else:
            self.pwm.write(0,0,self.value + a)
        
    def left(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            pass
           
        else:
            self.pwm.write(0,0,150)
           
    def start(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            pass
           
        else:
            self.pwm.write(0,0,260)
           
    def turn(self,angle):
        self.pwm.write(0,0,angle)
        

    def servo_test(self):
        if self.value < 300 or self.value > 420:
            pass
            
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
       
        self.start()
        time.sleep(0.5)
        self.right()
        time.sleep(0.5)
        self.avance()
        time.sleep(6)
        self.stop_voiture()
        time.sleep(0.5)
        self.left()
        time.sleep(0.5)
        self.avance()
        time.sleep(6)
        self.voiture.stop()
        time.sleep(0.5)
        self.start()
        time.sleep(0.5)
        self.stop_servo()

    def avance(self):
        self.voiture.set_speed()
        self.voiture.move_forward()

    def recule(self):
        self.voiture.set_speed()
        self.voiture.move_backward()

    def autonome(self):
        self.start()
        time.sleep(0.3)
        self.avance()
        if (self.th1.distance <= 30):
            self.turn(290) # vitesse de base : 410 --> 310
            time.sleep(1)
            self.avance()
        elif(self.th2.distance <= 30):
            self.turn(225) # vitesse de base : 150 -->210
            time.sleep(1)
            self.avance()
        elif(self.th3.distance <= 15):
            self.stop_voiture()
            self.recule()
            if(self.speed<=40):
                time.sleep(1)
            else :
                time.sleep(1)
            self.stop_voiture()
            if(self.th1.distance < self.th2.distance):
                self.turn(310)
                time.sleep(1)
                self.avance()
                time.sleep(1)
                self.stop_voiture()
            if (self.th2.distance < self.th1.distance):
                self.turn(200)
                time.sleep(1)
                self.avance()
                time.sleep(1)
                self.stop_voiture()
        else :
            self.avance()
    def IA(self):
        self.start()
        self.avance()
        if self.th3.distance <= 30:
            self.avance()
            print("Distance plus petite que 30 cm")
            print("1",self.speed)
            self.voiture.changeSpeed(30)
            print("2",self.speed)
            if self.th1.distance >=100 and self.th2.distance>=100:
                self.turn(140)
        if self.th3.distance <=7:
            print("Distance plus petite que 10 cm")
            self.voiture.changeSpeed(60)
            self.recule()
            time.sleep(0.7)
            if self.th1.distance >=80 and self.th2.distance>=30:
                self.turn(140)
            if self.distancePlusLoin() == False:
                self.turn(140)
            if self.distancePlusLoin() == True:
                self.turn(360)

        else:
            self.voiture.changeSpeed(30)
            print("3",self.speed)
        if self.distancePlusLoin()==False:
            self.turn(190)
        if self.distancePlusLoin() == True:
            self.turn(325)


    def distancePlusLoin(self):
        dist_gauche = self.th1.distance
        dist_droite = self.th2.distance
        dist_plus_loin = None
        if dist_droite < dist_gauche:
            dist_plus_loin = False      #False --> Distance Gauche
        if dist_gauche < dist_droite:
            dist_plus_loin = True       #True --> Distance Droite
        return dist_plus_loin

    def mur_gauche(self):
        self.start()
        time.sleep(0.5)
        self.avance()
        if (self.th1.distance <=18):
            self.turn(283)
            time.sleep(0.4)
            self.start()
            time.sleep(0.5)
            self.avance()
        if (self.th1.distance >= 60):
            self.turn(235)
            time.sleep(1)
            self.start()
            time.sleep(0.5)
            self.avance()

    def mur_droite(self):
        self.start()
        time.sleep(0.5)
        self.avance()
        if (self.th2.distance <=15):
            self.turn(240)
            time.sleep(0.4)
            self.start()
            time.sleep(0.5)
            self.avance()
        if (self.th2.distance >= 60):
            self.turn(283)
            time.sleep(0.3)
            self.start()
            time.sleep(0.3)
            self.avance()


    def evite(self):
        self.start()
        time.sleep(0.3)
        self.avance()
        if(self.th3.distance <= 30):
            self.turn(310)
            time.sleep(0.5)
            self.avance()
            time.sleep(1)
            self.turn(170)
            time.sleep(1)
            self.start()
            time.sleep(0.5)
            self.avance()
        else :
            self.avance()

    def testCapteurs(self):
        print(self.th1.distance)
        print(self.th2.distance)
        print(self.th3.distance)

