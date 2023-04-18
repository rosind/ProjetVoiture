from motorcc import *
import board
import busio
import Adafruit_PCA9685 as adafruit_pca9685

i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 50
pca1 = pca.channels[5]
#pca2 = adafruit_pca9685.channels[4]
motor1 = motorcc(pca1,17,18)
#motor2 = motorcc(pca2,27,22)
try:
    while True:
        motor2.advance
        #motor1.advance
except keyboardInterrupt:
    motor1.clean()
    #motor2.clean()