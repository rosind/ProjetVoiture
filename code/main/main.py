from capteurs import *

#capt1 = CapteurInfrarouge(20)
#capt1.detect()

ultrason = CapteurUltrason(37,35)
print("Attente du capteur...")
time.sleep(2)
print("Distance ", ultrason.distance(), " cm" )
ultrason.cleanup()