from modules import Factors


def is_prime(number):
    if number == 2:
        return True

    if number %2 == 0 or number < 2:
        return False

    factor = 3
    while factor*factor <= number:
        if Factors.isFactor(number, factor):
            return False
        factor += 1

    return True


def prime_numbers_below(n):
    primes = []

    if n > 2:
        primes.append(2)

    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)

    return primes


def nth_prime_number(n):
    primes = []

    if n > 0:
        primes.append(2)

    i = 3

    while len(primes) < n:
        if is_prime(i):
            primes.append(i)

        i += 2
    print(primes)
    return primes[n-1]
