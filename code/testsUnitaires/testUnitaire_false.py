import unittest
import sys
sys.path.append('../main')
from capteurs import CapteurInfrarouge

class TestCapteurTrue(unittest.TestCase):
    def test_capteurInfraIsTrue(self):
        cap1 = CapteurInfrarouge(20)
        self.assertTrue(cap1.detect())

if __name__ == '__main__':
    unittest.main()