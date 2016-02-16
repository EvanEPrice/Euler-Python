def isFactor(number, factor):
    return number % factor == 0

def smallestFactorOf(number):
    for i in range(2,number):
        if(isFactor(number, i)):
            return i