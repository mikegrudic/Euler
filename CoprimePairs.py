def CoprimePairs(N):
    pairs = [(2,1),(3,1)]
    i = 2
    
    while i > 0:
        newpairs = []
        for pair in pairs[-i:]:
            m = pair[0]
            n = pair[1]
            a1 = 2*m - n
            a2 = 2*m + n
            a3 = m + 2*n
            if 2*m-n < N:
                newpairs.append((a1, m))
            if 2*m+n < N:
                newpairs.append((a2, m))
            if m + 2*n < N:
                newpairs.append((a3, n))
        
        pairs.extend(newpairs)
        i = len(newpairs)
        
    return pairs

for i in xrange(100,1000,100):
    print i, 2.0*len(CoprimePairs(i))/i**2
