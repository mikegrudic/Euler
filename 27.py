from sympy import sieve

sieve.extend(2000000)

maxcount = 0
amax = 0
bmax = 0

for b in sieve.primerange(0,1000):
    for a in xrange(-2*(b/2)-1, 1000, 2):
        term = lambda n: n**2 + a*n + b
        i = 0
        count = 0
        while sieve.__contains__(term(i)):
            i += 1
            count += 1

        if count > maxcount: 
            maxcount = count
            amax = a
            bmax = b

print maxcount
print amax, bmax
