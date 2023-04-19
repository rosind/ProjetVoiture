import unittest
import sys
sys.path.append('../main')
from capteurs import CapteurUltrason

class TestCapteurClasse:
    def test_distanceMax40(self):
        capt1 = CapteurUltrason(6,5) #6,5 --> Capteur avant
        self.assertEqual()