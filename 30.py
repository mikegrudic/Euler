import numpy as np

sum = 0
powers = np.arange(10)**5

#powers = dict(powerlist)

for i in xrange(2,1000000):
    digits = list(str(i))
#    a = sum(powers[digits])
    a = np.sum(np.array(digits, dtype=np.int32)**5)
    if a == i:
        sum += i
        print i

print sum

