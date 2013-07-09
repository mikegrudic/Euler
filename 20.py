#!/usr/bin/env python                                                                                                                                
import numpy as np
from scipy import misc

n = misc.factorial(100,exact=True)
n_str = str(n)

sum = 0
for digit in n_str:
    sum += int(digit)

print sum

