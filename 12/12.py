import numpy as np
import sympy
from sympy import sieve

max_num = 100000000

tri = np.zeros(max_num, dtype=np.int64)
trisum = 0
for i in xrange(1,int(-0.5+0.5*np.sqrt(8*max_num+1))):
    trisum = trisum+i
    divisors = sympy.factor_.divisor_count(trisum)
    if divisors>500:
        print divisors, trisum
        exit()
