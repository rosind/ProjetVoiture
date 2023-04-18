#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

#configurer le min et le max du servo
servo_min = 150
servo_max = 600 

class Servo:
    def set_servo_pulse(channel, pulse):
        pulse_length = 1000000
        pulse_length //=60
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(channel, 0, pulse)
        
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)


        
