import RPi.GPIO as GPIO          
import time
#import threading a implementer peut etre plus tard
class motorDC:
    def __init__(self,en,input1,input2): #definition des pins pour activer le moteur, le pin input pour le controller
        self.en=en
        self.in1=13
        self.in2=15
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        p=GPIO.PWM(self.en,1000)     
        p.start(50)     #valeur du DutyCylce au demarrage

    def forward(self):
        while True:
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            print("forward")
            time.sleep(10)
            motorDC.stop()  #retirer 2 lignes ci apres le tests
            time.sleep(5)

    def backward(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        print("backward")
        time.sleep(10)
        motorDC.stop()  #retirer 2 lignes ci apres le tests
        time.sleep(5)
    
    def stop(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        print("stop")

        


    if __name__ == "__main__":
        try:         
            pass #wip
        except:
            print("modifier pins de connections")