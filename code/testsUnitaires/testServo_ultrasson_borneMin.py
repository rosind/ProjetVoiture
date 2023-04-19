import unittest
import sys
sys.path.append('../main')
from capteurs import CapteurUltrason

class TestCapteurClasse(unittest.TestCase):
    def test_distanceMin5(self):
        capt1 = CapteurUltrason(6,5) #6,5 --> Capteur avant
        self.assertEqual(capt1.distance(),5)

if __name__ == '__main__':
    unittest.main()