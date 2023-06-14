# In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that m^k = n.

from math import log, sqrt

def isPP(n):
    n = int(n)
    if n < 4: return None
    sr = round(sqrt(n),6)
    if sr == round(sr): return [sr, 2]
    for m in range(2,int(n/2)):
        k = round(log(n, m),6)
        if k == round(k): return [m, k]
    return None

n = input('Enter an integer number: ')
m = isPP(int(n))
print(f'The powers of {n} are {m}')
