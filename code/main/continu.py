from motorcc import *
import adafruit_pca9685

pca1 = adafruit_pca9685.channels[5]
pca2 = adafruit_pca9685.channels[4]
motor1 = motorcc(pca1,17,18)
motor2 = motorcc(pca2,27,22)
try:
    while True:
        motor2.advance
        motor1.advance
except keyboardInterrupt
    motor1.clean()
    motor2.clean()