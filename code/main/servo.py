#!/usr/bin/env python
import PCA9685 as servo
import time
from motorcc import *

class Voiture() :
    def __init__(self,speed):
        self.speed = speed
        self.setup()
        self.voiture = drive(self.speed)
        
    def setup(self):
        global pwm
        self.pwm = servo.PWM()
        self.pwm.frequency = 50
        self.value=350

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
        # self.voiture.set_speed()
        # self.right()
        # self.voiture.move_forward()
        # time.sleep(5)
        # self.start
        # time.sleep(1)
        # self.left()
        # self.voiture.move_forward()
        # time.sleep(5)
        # self.stop_servo()
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
        self.stop_servo()

    
            

"""
MinPulse = 150
MaxPulse = 450



def servo_test():
    
    while True:

        for value in range(MinPulse, MaxPulse, 25):
            print ('PWM value: %d' % value)
            pwm.write(0, 0, value)
            #pwm.write(14, 0, value)
            #pwm.write(15, 0, value)
            time.sleep(0.1)

        for value in range(MaxPulse, MinPulse, -25):
            print ('PWM value: %d' % value)
            pwm.write(0, 0, value)
            #pwm.write(14, 0, value)
            #pwm.write(15, 0, value)
            time.sleep(0.1)


        pwm.write(0, 0, 350)
"""


""" if __name__ == '__main__':
    MyServo=Servo()
    MyServo.setup()
    MyServo.servo_test()
    #setup()
    #Servo_test()
 """