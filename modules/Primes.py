from modules import Factors

def isPrime(number):
    if(number == 2):
        return True

    if(number %2 == 0):
        return False

    factor = 3
    while factor*factor <= number:
        if Factors.isFactor(number, factor):
            return False
        factor += 1

    return True

def nth_prime_number(n):
    primes = []
    i = 2

    while(len(primes) < n):
        if(isPrime(i)):
            primes.append(i)

        i += 1

    return primes[n-1]
