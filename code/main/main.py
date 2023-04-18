from capteurs import *
from Thread import *
import threading

#capt1 = CapteurInfrarouge(20)
#capt1.detect()

ultrasonGauche = CapteurUltrason(11,9)
ultrasonDroite = CapteurUltrason(26,19)
ultrasonAvant = CapteurUltrason(6,5)

th1 = CapteurUltrasonThread(ultrasonGauche)
th2 = CapteurUltrasonThread(ultrasonDroite)
th3 = CapteurUltrasonThread(ultrasonAvant)

th1.start()
th2.start()
th3.start()

time.sleep(2)

for i in range(10):
    time.sleep(2)
    print(f"Essaie {i}:")
    print(f"Le capteur Avant: {th3.get_distance()}")
    print(f"Le capteur Droit: {th2.get_distance()}")
    print(f"Le capteur Gauche: {th1.get_distance()}")
    print("----------------------")

th1.stop()
th2.stop()
th3.stop()