from sympy.ntheory import divisors
import numpy as np


sum = 0

for i in xrange(1,10000):
    divSum = np.sum(divisors(i)[:-1])
    if i == np.sum(divisors(divSum)[:-1]) and i !=divSum:
        sum += i

print sum
