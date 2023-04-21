import time

from Thread import *
from servo import *
capt1 = CapteurInfrarouge(20)
th4 = CapteurInfrarougeThread(capt1.pin)
th4.start()

for i in range(10):
    print(th4.etat)
    time.sleep(1)

th4.stop()