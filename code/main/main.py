from Thread import *
from servo import *
from captCourant import *

voit1 = Voiture(40)
voit1.startThread()
courant = CaptCourant()

try:
    tour = int(input("Entre le nombre de tours:"))
    while (tour > 0):
        voit1.autonome()
        print(voit1.detect_Line())
        if voit1.detect_Line():
            tour-=1
            time.sleep(1.5)

    print("Fin de course !")
    voit1.stopThread()
    voit1.stop_voiture()
#if(courant.ina.voltage() >= 4.5 or courant.ina.current() >=330 or courant.ina.power() >= 28):
#voit1.stopThread()
#voit1.stop_voiture()
except(KeyboardInterrupt):
    voit1.stopThread()
    voit1.stop_voiture()