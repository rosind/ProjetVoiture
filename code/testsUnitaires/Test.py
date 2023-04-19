import unittest
import sys
sys.path.append('..')
from main.capteurs import CapteurInfrarouge

class TestCapteur(unittest.TestCase):
    def capteurInfraIsInstanceOfCapteurInfra(self):
        cap1 = CapteurInfrarouge(20)
        self.assertIsInstance(cap1, CapteurInfrarouge)

if __name__ == '__main__':
    unittest.main()