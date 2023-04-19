import unittest
import sys
sys.path.append('../main')
from capteurs import CapteurUltrason

class TestCapUltrason(unittest.TestCase):
    def testInstanceUltrason(self):
        ultrasoundRight = CapteurUltrason(19,26) #capteur droit
        ultrasoundLeft = CapteurUltrason(11,9) #capteur gauche
        ultrasoundFront =  CapteurUltrason(6,5) #avant
        self.assertIsInstance(ultrasoundFront, CapteurUltrason)
        self.assertIsInstance(ultrasoundRight, CapteurUltrason)
        self.assertIsInstance(ultrasoundLeft, CapteurUltrason)
    
    def detection(self):
        ultrasoundRight = CapteurUltrason(19,26) #capteur droit
        ultrasoundLeft = CapteurUltrason(11,9) #capteur gauche
        ultrasoundFront =  CapteurUltrason(6,5) #avant
        self.assertGreater(ultrasoundFront.distance(),10)
        self.assertGreater(ultrasoundRight.distance(),10)
        self.assertGreater(ultrasoundLeft.distance(),10)        



if __name__ == '__main__':
    unittest.main()