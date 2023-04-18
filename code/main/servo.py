#!/usr/bin/env python
import PCA9685 as servo
import time                  # Import necessary modules

MinPulse = 50
MaxPulse = 450

def setup():
    global pwm
    pwm = servo.PWM()
    pwm.frequency = 50

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

if __name__ == '__main__':
    setup()
    servo_test()
