import unittest
from modules import Factors


class FactorsTest(unittest.TestCase):
    def test_isFactorShouldReturnTrue(self):
        self.assertEqual(Factors.isFactor(12,3), True)


    def test_isFactorShouldReturnFalse(self):
        self.assertEqual(Factors.isFactor(14,3), False)

    def test_SmallestFactorOfShouldReturn2(self):
        self.assertEqual(Factors.smallestFactorOf(24), 2)

    def test_SmallestFactorOfShouldReturn3(self):
        self.assertEqual(Factors.smallestFactorOf(21), 3)


if __name__ == '__main__':
    unittest.main()
