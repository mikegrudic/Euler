#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy,random
from optparse import OptionParser
from subprocess import call

def pathsum(path,numbers):
    Sum=numbers[0][0]
    j=0
    for i in xrange(1,len(numbers)):
        j+=path[i]
        Sum+=numbers[i][j]
    
    return Sum

f=open("18.dat","r")

text=f.readlines()

f.close()

numbers=numpy.zeros((len(text),len(text)),dtype=int)


for i in xrange(len(text)):
    for j in xrange(i+1):
        numbers[i][j]=numpy.fromstring(text[i],dtype=int,sep=' ')[j]


path=numpy.zeros(len(numbers),dtype=int)

l=len(path)

max_sum=0

for i in xrange(100000):
    rindex=int(l*random.random())
    r2=random.random()

    path[rindex]=1-path[rindex]
    
    newsum=pathsum(path,numbers)

    if (newsum>max_sum):
        max_sum=newsum
    elif(r2>0.2):
        path[rindex]=1-path[rindex]

print max_sum

