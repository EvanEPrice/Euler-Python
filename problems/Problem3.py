#What is the largest prime factor of the number 600851475143 ?
from modules import Primes
from modules import Factors

problemNumber = 600851475143


def solve():
    smallest_factor = Factors.smallestFactorOf(problemNumber)
    largest_factor = int(problemNumber/smallest_factor)

    for i in range(smallest_factor, largest_factor):
    
        if Factors.isFactor(problemNumber, i):
            counterpart = int(problemNumber/i)
    
            if Primes.is_prime(counterpart):
                return counterpart

largest_prime_factor = solve()

print(largest_prime_factor)
