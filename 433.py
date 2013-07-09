# can do the sum over relatively prime pairs - multiply by the number of multiples of the pair below N
# do the same for (n,m) as for (m,n), using recurrence relation

def E(x,y):
    count = 0
    while (y!=0):
        x, y = y, x%y
        count += 1

    return count

print E(13,17), E(17,13)

#def S(N):
#    s = 0
#    for x in xrange(1,N+1):
        
#    return s
#e = []



#for i in xrange(1000):
#    for j in xrange(1000):
#        e.append(E(i,j))

#print e

