import unittest
import sys
sys.path.append('../main')
from capteurs import CapteurInfrarouge

class TestCapteurClasse(unittest.TestCase):
    def test_capteurInfraIsInstanceOfCapteurInfra(self):
        cap1 = CapteurInfrarouge(20)
        self.assertIsInstance(cap1, CapteurInfrarouge)

if __name__ == '__main__':
    unittest.main()