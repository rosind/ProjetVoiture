from Thread import *
from servo import *

voit1 = Voiture(40)

tour = int(input("Entre le nombre de tours:"))
while (tour > 0):
    voit1.suivreMur()
    if voit1.detect_Line():
        tour-=1

print("Fin de course !")
voit1.stopThread()
voit1.stop_voiture()