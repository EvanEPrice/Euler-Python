#Find the sum of all the primes below two million.

from modules import Primes

problem_number = 2000000
primes = Primes.prime_numbers_below(problem_number)

prime_sum = sum(primes)

print(primes)
print(prime_sum)
