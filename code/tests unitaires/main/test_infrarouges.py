import unittest
from unittest.mock import patch
from guiguipastouchecapteurs import CapteurInfrarouge

class TestCapteurInfrarouge(unittest.TestCase): #permet de tester des cas
    def setUp(self): 
        self.capteur = CapteurInfrarouge(20)

    @patch('capteur_infrarouge.GPIO')
    def test_detect_ligne_noir(self, mock_GPIO):
        mock_GPIO.input.return_value = True
        self.assertTrue(self.capteur.detect())

    @patch('capteur_infrarouge.GPIO')
    def test_detect_pas_ligne_noir(self, mock_GPIO):
        mock_GPIO.input.return_value = False
        self.assertFalse(self.capteur.detect())

if __name__ == '__main__':
    unittest.main()