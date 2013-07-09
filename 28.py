import numpy as np

diag1 = 0
diag2 = 0

maxterm = 1001**2+1
i = 1
sum1 = sum2 = 0
term = 1

while term < maxterm:
    sum1 += term
    term += 2*i
    i += 1

term = 1
i = 0
while term < maxterm:
    sum2 += term
    term += 4*(i/2+1)
    i += 1
    
print sum1 + sum2 - 1
