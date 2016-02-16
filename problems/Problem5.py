#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from modules import Factors


def divisbleByAll(number):
    for i in range(1,20):
        if(not Factors.isFactor(number, i)):
            return False

    return True


upper = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20

for r in range(20, upper, 20):
    if(divisbleByAll(r)):
        print (r)
        break

