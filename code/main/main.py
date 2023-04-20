from Thread import *

ultrasonGauche = CapteurUltrason(11,9)
ultrasonDroite = CapteurUltrason(26,19)
ultrasonAvant = CapteurUltrason(6,5)
capt1 = CapteurInfrarouge(20)
th1 = CapteurUltrasonThread(ultrasonGauche)
th2 = CapteurUltrasonThread(ultrasonDroite)
th3 = CapteurUltrasonThread(ultrasonAvant)
th4 = CapteurInfrarougeThread(capt1.pin)
th1.start()
th2.start()
th3.start()
th4.start()
time.sleep(1)

tour = int(input("Entre le nombre de tours:"))
while (tour > 0):
    i=1
    time.sleep(1)
    print(f"Essaie {i}:")
    print(f"Le capteur Avant: {th3.distance} cm")
    print(f"Le capteur Droit: {th2.distance} cm")
    print(f"Le capteur Gauche: {th1.distance} cm")
    print(f"Le capteur infrarouge est {th4.etat}")
    print(tour)
    if (th4.etat==True):
        tour-=1
        i+=1


th1.stop()
th2.stop()
th3.stop()
th4.stop()