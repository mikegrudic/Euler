#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy
from optparse import OptionParser
from subprocess import call

numList=numpy.ones(1000000,dtype=numpy.bool)
maxLength=0
maxIndex=0

values=numpy.where(numList==True)[0]
print values


for i in values:
    n=i+1
    print n
    length=0
    while (n!=1):
        if (n%2==0): n=n/2
        else: n=3*n+1
        values=numpy.delete(values,n-1)
        length+=1
    if (length>maxLength):
        maxIndex=i+1
        maxLength=length
    
    
print maxIndex, maxLength
