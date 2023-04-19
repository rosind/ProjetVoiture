#!/usr/bin/env python
import PCA9685 as servo
import time                  # Import necessary modules

class Servo:
    def setup(self):
        global pwm
        self.pwm = servo.PWM()
        self.pwm.frequency = 50
        self.value=350

    def rigth(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            print("Valeur comprise entre 250 et 450")
        else:
            self.pwm.write(1,0,self.value + a)
            print("Tourne à droite", a, ' (', self.value + a, ')')

    def left(self, a=60):
        if self.value - a < self.value-75 or self.value + a > self.value+75:
            print("Valeur comprise entre 250 et 450")
        else: 
            self.pwm.write(1,0,self.value - a)
            print("Tourne à gauche", a, ' (', self.value + a, ')')

    def servo_test(self):
        if self.value < 300 or self.value > 420:
            print("Valeur comprise entre 250 et 450")
        else:
            self.pwm.write(1,0,225)
            time.sleep(1)
            self.pwm.write(1,0,300)
            time.sleep(1)
            self.pwm.write(1,0,375)
            time.sleep(1)
            self.pwm.write(1,0,299)
            

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


if __name__ == '__main__':
    MyServo=Servo()
    MyServo.setup()
    MyServo.servo_test()
    #setup()
    #Servo_test()

