#What is the largest prime factor of the number 600851475143 ?
from modules import Primes
from modules import Factors

problemNumber = 600851475143
largestPrimeFactor = 0

smallestFactor = Factors.smallestFactorOf(problemNumber)
largestFactor = int(problemNumber/smallestFactor)

for i in range(smallestFactor, largestFactor):

    if Factors.isFactor(problemNumber,i):
        counterpart = int(problemNumber/i)

        if(Primes.is_prime(counterpart)):
            largestPrimeFactor = counterpart
            print(largestPrimeFactor)
            break

print("done")