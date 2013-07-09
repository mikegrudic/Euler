import numpy as np
from scipy import misc

upper_bound = 1000000

num_sum = 0

for i in xrange(upper_bound):
    if np.sum(misc.factorial(np.array(list(str(i)), dtype=np.int16))) == i:
        num_sum += i

print num_sum
