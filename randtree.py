#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy,random
from optparse import OptionParser
from subprocess import call

f=open("randtree.dat","w")

for i in xrange(10):
        r1=numpy.random.rand(i+1)
        print r1

f.close()
