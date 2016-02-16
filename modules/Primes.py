from modules import Factors

def isPrime(number):
    if(number == 2):
        return True

    if(number %2 == 0):
        return False

    factor = 3
    while factor*factor < number:
        if Factors.isFactor(number, factor):
            return False
        factor += 2

    return True
