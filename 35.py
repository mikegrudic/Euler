from PermuteString import PermuteString
from sympy import sieve
import itertools

sieve.extend(1000000)

primes = sieve._list
stringprimes=[]
for prime in primes:
    stringprimes.append(str(prime))

count = 0

primeset = set(stringprimes)

excluded_digits = set(['0','2','4','5','6','8'])

for p in stringprimes:
    if not excluded_digits.isdisjoint(set(p)):
        continue

    perm = PermuteString(p)

    if set(perm) <= primeset:
        count += 1
        print p

count += 2

print count
