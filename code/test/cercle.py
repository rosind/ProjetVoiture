import PCA9685 as servo
import time
from moteurjetest import *

class cercle:
    def __init__(self,minimum,maximum):
        self.minimum = minimum
        self.maximum = maximum
        GPIO.setmode(GPIO.BOARD)

    def setup(self):
        global pwm
        pwm = servo.PWM()
        pwm.frequency = 50

    def turn(self):
        try:
            while True:
                for value in range(self.minimum, self.maximum):
                    print ('PWM value: %d' % value)
                    pwm.write(0, 0, value)
                    time.sleep(0.05)

                pwm.write(0, 0, 700)
        except KeyboardInterrupt:
            GPIO.cleanup()

sens = cercle(100,700)
motor_pins = [11, 12, 13, 15] 
pwm_pins = [4, 5] 
forward_configs = [True, True] 
voiture = Car(motor_pins, pwm_pins, forward_configs)
voiture.set_speed(60)

if True:
    voiture.move_forward()
    sens.setup()
    sens.turn()
