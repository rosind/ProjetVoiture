from Thread import *
from servo import *

ultrasonGauche = CapteurUltrason(11,9)
ultrasonDroite = CapteurUltrason(26,19)
ultrasonAvant = CapteurUltrason(6,5)
capt1 = CapteurInfrarouge(20)

voit1 = Voiture(40)

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
i=1
while (tour > 0):
    voit1.suivreMur()
    if (th4.etat==True):
        tour-=1
        i+=1

print("Fin de course !")
th1.stop()
th2.stop()
th3.stop()
th4.stop()