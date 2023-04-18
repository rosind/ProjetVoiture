#!/usr/bin/env python
import PCA9685 as servo
import time                  # Import necessary modules

MinPulse = 150
MaxPulse = 450

def setup():
    global pwm
    pwm = servo.PWM()
    pwm.frequency = 50

def rightServo():
    for value in range(MinPulse, MaxPulse, 25):
        print ('PWM value: %d' % value)
        pwm.write(0, 0, value)
        time.sleep(0.1)    

def leftServo():
    for value in range(MaxPulse, MinPulse, -25):
        print ('PWM value: %d' % value)
        pwm.write(0, 0, value)
        time.sleep(0.1)

def position_init():
    pwm.write(0, 0, 250)    


        

if __name__ == '__main__':
    setup()
    rightServo()
    leftServo()
    position_init()
