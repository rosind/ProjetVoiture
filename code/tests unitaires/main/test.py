import unittest
from unittest.mock import patch
from gpiozero import InputDevice
from guiguipastouchecapteurs import CapteurInfrarouge

class TestCapteurInfrarouge(unittest.TestCase):
    def setUp(self): 
        self.capteur = CapteurInfrarouge(20)

    @patch('gpiozero.InputDevice')
    def test_detect_ligne_noir(self, mock_InputDevice):
        mock_input = mock_InputDevice.return_value
        mock_input.is_active.return_value = True
        self.assertTrue(self.capteur.detect())

    @patch('gpiozero.InputDevice')
    def test_detect_pas_ligne_noir(self, mock_InputDevice):
        mock_input = mock_InputDevice.return_value
        mock_input.is_active.return_value = False
        self.assertFalse(self.capteur.detect())

if __name__ == '__main__':
    unittest.main()