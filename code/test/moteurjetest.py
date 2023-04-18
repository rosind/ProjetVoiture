#!/usr/bin/env python
import RPi.GPIO as GPIO
import PCA9685 as p
import time    # Import necessary modules

class Car:
    def __init__(self, motor_pins, pwm_pins, forward_configs):
        self.motor_pins = motor_pins
        self.EN_M0, self.EN_M1 = pwm_pins
        self.forward0, self.forward1 = forward_configs
        self.backward0 = not self.forward0
        self.backward1 = not self.forward1
        self.setup()

    def setup(self, busnum=None):
        if busnum == None:
            self.pwm = p.PWM()                  # Initialize the servo controller.
        else:
            self.pwm = p.PWM(bus_number=busnum) # Initialize the servo controller.

        self.pwm.frequency = 60
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)        # Number GPIOs by its physical location
        
        for pin in self.motor_pins:
            GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode as output

    def set_speed(self, speed):
        speed *= 40
        print('Speed is:', speed)
        self.pwm.write(self.EN_M0, 0, speed)
        self.pwm.write(self.EN_M1, 0, speed)

    def move_forward(self):
        self._set_motor_pins(self.forward0, self.forward1)

    def move_backward(self):
        self._set_motor_pins(self.backward0, self.backward1)

    def stop(self):
        for pin in self.motor_pins:
            GPIO.output(pin, GPIO.LOW)

    def _set_motor_pins(self, pin0, pin1):
        GPIO.output(self.motor_pins[0], GPIO.LOW if pin0 else GPIO.HIGH)
        GPIO.output(self.motor_pins[1], GPIO.HIGH if pin0 else GPIO.LOW)
        GPIO.output(self.motor_pins[2], GPIO.LOW if pin1 else GPIO.HIGH)
        GPIO.output(self.motor_pins[3], GPIO.HIGH if pin1 else GPIO.LOW)

if __name__ == '__main__':
    try:
        motor_pins = [11, 12, 13, 15]  # Raspberry Pi pin11, 12, 13, and 15 to realize the clockwise/counterclockwise rotation and forward and backward movements
        pwm_pins = [4, 5]  # Set channel 4 and 5 of the DC motor driver IC to generate PWM, thus controlling the speed of the car
        forward_configs = [True, True]  # Read from config file or set default
        car = Car(motor_pins, pwm_pins, forward_configs)
        
        while True:
            speed = int(input('Enter speed (0-100): '))
            car.set_speed(speed)
            direction = int(input('Enter direction (1 for forward, -1 for backward): '))
            if direction == 1:
                car.move_forward()
            elif direction == -1:
                car.move_backward()
            else:
                car.stop()

    finally:  # This block will run no matter how the try block exits  
        GPIO.cleanup()  # Clean up after yourself
