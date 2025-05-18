import unittest
from pi_calculation import calculate_pi

class TestPiCalculation(unittest.TestCase):
    def test_calculate_pi(self):
        self.assertAlmostEqual(calculate_pi(1), 4.0)
        self.assertAlmostEqual(calculate_pi(100), 3.1315929035585537)
        self.assertAlmostEqual(calculate_pi(1000), 3.140592653839794)

if __name__ == '__main__':
    unittest.main()