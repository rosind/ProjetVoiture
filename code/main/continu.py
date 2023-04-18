from motorcc import *

motor1 = motorcc(11,12)
motor2 = motorcc(13,15)
try:
    while True:
        motor1.setSpeed(100)
        motor2.setSpeed(100)
        motor2.advance()
        motor1.advance()
except KeyboardInterrupt:
    motor1.clean()
    motor2.clean()