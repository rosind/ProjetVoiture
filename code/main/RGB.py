#!/usr/bin/env /python3reb
import RPi.GPIO as GPIO
import time
import board
import tcs34725

class Color:
    def __init__(self):
        super().init()
        self.i2c = board.I2C()
        self.sensor = tcs34725.TCS34725(self.i2c)
        self.valColor = 0
        self.valTemp = 0
        self.valLux = 0

    def run(self):
        while not self.isKilled:
            self.setColor(self.sensor.color_rgb_bytes)
            self.setTemp(self.sensor.color_temperature)
            self.setLux(self.sensor.lux)

        print(self, "is killed")

    def setColor(self, _valC):
        self.valColor = _valC

    def getColor(self):
        return self.valColor

    def setTemp(self, _valT):
        self.valTemp = _valT

    def getTemp(self):
        return self.valTemp

    def setLux(self, _valL):
        self.valLux = _valL

    def getLux(self):
        return self.valLux