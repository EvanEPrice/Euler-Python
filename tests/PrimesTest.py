import unittest
from modules import Primes

class PrimesTest(unittest.TestCase):
    def test_isPrimeShouldReturnTrue(self):
        self.assertEqual(Primes.isPrime(23), True)

    def test_isPrimeShouldReturnFalse(self):
        self.assertEqual(Primes.isPrime(12), False)

    def test(self):
        self.assertEqual(Primes.isPrime(600851475143), False)


if __name__ == '__main__':
    unittest.main()
