"""Exemple de code et test pour adafruits_ina219"""
import time
import PCA9685 as servo
#from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

class Ina219():
    def __init__(self):
        self.i2c_bus = servo.I2C()
        self.ina219 = INA219(i2c_bus)
        self.setup()

    def setup(self):
        ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        ina219.bus_voltage_range = BusVoltageRange.RANGE_16V
    def currentmeasure(self):
        for i in range(10):
            current = ina219.current  # current in mA
            print(" Current  : {:7.4f}  A\n".format(current / 1000))
            if ina219.overflow:
                print("Internal Math Overflow Detected!")
                print("")
            time.sleep(0.5)


if __name__=="__main__":
 i2c_bus = servo.I2C()  # uses board.SCL and board.SDA
 # i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

 ina219 = INA219(i2c_bus)

 # optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
 ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
 ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
 # optional : change voltage range to 16V
 ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

 # measure and display loop
 for i in range(20):
    current = ina219.current  # current in mA
    print(" Current  : {:7.4f}  A".format(current / 1000))
    print("")

    if ina219.overflow:
        print("Internal Math Overflow Detected!")
        print("")

    time.sleep(0.5)
