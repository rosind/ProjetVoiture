from motorcc import *

motors = Car(60)
a = 0

while (a<1):
    motors.run()
    time.sleep(5)
    #motors.faireUnCercle()
    a+=1