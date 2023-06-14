# In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that m^k = n.

from math import sqrt

def isPP(n):
    for k in range(1,int(sqrt(n)+3)):
        for i in range(0,k):
            for j in range(0,k):
                if i**j == n:
                    return [i,j]
                    break
    return None

n = input('Enter an integer number: ')
m = isPP(int(n))
print(f'The powers of {n} are {m}')
