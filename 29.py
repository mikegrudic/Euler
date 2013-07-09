nums = []

for a in xrange(2,101):
    for b in xrange(2,101):
        nums.append(a**b)

print len(set(nums))
