import unittest
from modules import Primes

class PrimesTest(unittest.TestCase):
    def test_isPrimeShouldReturnTrue(self):
        self.assertEqual(Primes.isPrime(23), True)

    def test_isPrimeShouldReturnFalse(self):
        self.assertEqual(Primes.isPrime(9), False)

    def test_nth_prime_number_6th(self):
        self.assertEqual(Primes.nth_prime_number(6), 13)

    def test_nth_prime_number_2nd(self):
        self.assertEqual(Primes.nth_prime_number(2), 3)




if __name__ == '__main__':
    unittest.main()
