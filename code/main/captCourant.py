import time
from ina219 import INA219
from ina219 import DeviceRangeError

class CaptCourant():
    def __init__(self):
            pass
    
    def testcourant(self):
        
        ina = INA219(0.1)
        ina.configure()
        try:
            print("Bus Voltage: %.3f V" % ina.voltage())
            print("Bus Current: %.3f mA" % ina.current())
            print("Power: %.3f mW" % ina.power())
            print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
        except DeviceRangeError as e:
            # Current out of device range with specified shunt resistor
            print(e)
            
if __name__ == '__main__':
    mytestcourant = CaptCourant()
    while True:
        mytestcourant.testcourant()
        