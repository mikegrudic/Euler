#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy
from optparse import OptionParser
from subprocess import call

numList=numpy.ones(1000000,dtype=numpy.bool)
maxLength=0
maxIndex=0

values=numpy.where(numList==True)[0]
print values


for i in xrange(1000000):
    n=i+1
    if (not numList[n-1]): 
        continue
    print n
    length=0
    while (n!=1):
        if (n%2==0): n=n/2
        else: n=3*n+1
        if(n<1000001): numList[n-1]=False
        length+=1
    if (length>maxLength):
        maxIndex=i+1
        maxLength=length
    
print maxIndex, maxLength
