from capteurs import *

#capt1 = CapteurInfrarouge(20)
#capt1.detect()

ultrason = CapteurUltrason(26,19)
try:
    while True:
        print(f"La distance est de {ultrason.distance()} cm.")
        time.sleep(0.5)
except KeyboardInterrupt:
    ultrason.clean()
