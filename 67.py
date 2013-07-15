#import numpy as np
import math
import time

t = time.time()
class Node:
    def __init__(self,value):
        self.l1 = None
        self.l2 = None
        self.value = value
    def MaxSum(self):
        if self.l1 == None:
            self.maxsum = self.value
        else:
            self.maxsum =  max(self.l1.maxsum,self.l2.maxsum) + self.value

f=open('triangle.txt', 'r')
nums = f.read().split()
nums = [int(num) for num in nums]

nodes = [Node(num) for num in nums]

nmax = int(-0.5 + math.sqrt(0.25 + 4*0.5*len(nums)) + 0.5)
for i, node in enumerate(nodes):
    n = int(math.ceil(-0.5 + math.sqrt(0.25 + 4*0.5*(i+1)))+0.5)
    if n < nmax:
        node.l1, node.l2 = nodes[i+n], nodes[i+n+1]

for i in xrange(len(nodes)-1,-1,-1):
    nodes[i].MaxSum()
    
print nodes[0].maxsum
print time.time()-t
