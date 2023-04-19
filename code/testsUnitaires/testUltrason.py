import unittest
from main.capteurs import CapteurUltrason

class TestCapUltrason(unittest.TestCase):
        
    def testInstanceUltrason(self):
        self.assertIsInstance(ultrasoundFront, CapteurUltrason)
        self.assertIsInstance(ultrasoundRight, CapteurUltrason)
        self.assertIsInstance(ultrasoundLeft, CapteurUltrason)
    
    def detection(self):
        self.assertGreater(ultrasoundFront.distance(),10)
        self.assertGreater(ultrasoundRight.distance(),10)
        self.assertGreater(ultrasoundLeft.distance(),10)        



if __name__ == '__main__':
    ultrasoundRight = CapteurUltrason(19,26) #capteur droit
    ultrasoundLeft = CapteurUltrason(11,9) #capteur gauche
    ultrasoundFront =  CapteurUltrason(6,5) #avant
    unittest.main()