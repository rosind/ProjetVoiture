from capteurs import *
from Thread import *
import threading

ultrasonGauche = CapteurUltrason(11,9)
ultrasonDroite = CapteurUltrason(26,19)
ultrasonAvant = CapteurUltrason(6,5)
capt1 = CapteurInfrarouge(20)

th1 = CapteurUltrasonThread(ultrasonGauche)
th2 = CapteurUltrasonThread(ultrasonDroite)
th3 = CapteurUltrasonThread(ultrasonAvant)
th4 = CapteurInfrarougeThread(capt1)

th1.start()
th2.start()
th3.start()
th4.start()

time.sleep(2)

for i in range(10):
    time.sleep(2)
    print(f"Essaie {i}:")
    print(f"Le capteur Avant: {th3.get_distance()}")
    print(f"Le capteur Droit: {th2.get_distance()}")
    print(f"Le capteur Gauche: {th1.get_distance()}")
    if (th4.detect()):
        print("Je détecte la ligne !")
    else:
        print("Je ne détecte pas la ligne !")
    print("----------------------")

th1.stop()
th2.stop()
th3.stop()
th4.stop()