from Thread import *
from servo import *

voit1 = Voiture(60)
#Ajouter un try except avec un raise except conditionné 
# par les valeurs du capteur de courant
tour = int(input("Entre le nombre de tours:"))
while (tour > 0):
    voit1.startThread()
    voit1.autonome()
    print(voit1.detect_Line())
    if voit1.detect_Line():
        tour-=1

print("Fin de course !")
voit1.stopThread()
voit1.stop_voiture()