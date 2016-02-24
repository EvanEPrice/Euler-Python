import unittest

from problems import Problem1
from problems import Problem2
from problems import Problem3


class ProblemTest(unittest.TestCase):
    def test_problem1(self):
        self.assertEqual(Problem1.solve(), 233168)

    def test_problem2(self):
        self.assertEquals(Problem2.solve(), 4613732)

    def test_problem3(self):
        self.assertEquals(Problem3.solve(), 6857)


if __name__ == '__main__':
    unittest.main()
