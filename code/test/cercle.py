import PCA9685 as servo
import time
from moteurjetest import *

class cercle:
    def __init__(self,minimum,maximum):
        self.min = minimum
        self.max = maximum
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

                pwm.write(0, 0, 350)
        except KeyboardInterrupt:
            GPIO.cleanup()

sens = cercle(100,400)
motor_pins = [11, 12, 13, 15] 
pwm_pins = [4, 5] 
forward_configs = [True, True] 
voiture = Car(motor_pins, pwm_pins, forward_configs)

if __name__ == '__main__':
    voiture.move_forward()
    sens.setup()
    sens.turn()