import unittest
from unittest.mock import MagicMock
from guiguipastouchecapteurs import CapteurUltrason

class TestCapteurUltrason(unittest.TestCase):
    def setUp(self):
        self.trig = 26
        self.echo = 19
        self.capteur = CapteurUltrason(self.trig, self.echo)

    def test_init(self):
        self.assertEqual(self.capteur.trig, self.trig)
        self.assertEqual(self.capteur.echo, self.echo)

    def test_distance(self):
        # Mock GPIO and set echo to HIGH for 0.01s to simulate pulse
        GPIO = MagicMock()
        GPIO.input.return_value = 0
        GPIO.input.side_effect = [1, 1, 1, 0, 0, 0]
        self.capteur.GPIO = GPIO
        distance = self.capteur.distance()
        self.assertAlmostEqual(distance, 5.85, delta=0.1)

    def test_clean(self):
        # Test that GPIO cleanup function is called
        GPIO = MagicMock()
        self.capteur.GPIO = GPIO
        self.capteur.clean()
        GPIO.cleanup.assert_called_once()

if __name__ == '__main__':
    unittest.main()