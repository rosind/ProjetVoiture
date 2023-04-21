from Thread import *
from servo import *

voit1 = Voiture(60)
try:
    tour = int(input("Entre le nombre de tours:"))
    while (tour > 0):
        voit1.autonome()
        print(voit1.detect_Line())
        if voit1.detect_Line():
            tour-=1
            time.sleep(1)

    print("Fin de course !")
    voit1.stopThread()
    voit1.stop_voiture()
except(KeyboardInterrupt):
    voit1.stopThread()
    voit1.stop_voiture()