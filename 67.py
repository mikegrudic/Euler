#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy,random
from optparse import OptionParser
from subprocess import call

usage="""                                                                                                                                           """

def error(msg):
    os.sys.stderr.write("############# ERROR n#############\n");
    os.sys.stderr.write(msg+"\n")
    os.sys.exit(-1)

# Display a verbose error message & backtrace                                                                                                        
def croak(msg):
    os.sys.stderr.write("############# CROAK #############\n");
    os.sys.stderr.write(msg+"\n")
    traceback.print_stack()
    os.sys.exit(-1)

# Subroutine to safely run a system bash command                                                                                                     
def System(cmd):
    status = call(cmd, shell=True, executable='/bin/bash')
    if status != 0:
      croak("This command failed with return status "+str(status)+": "+cmd)

########################################################################################

def pathsum(path,numbers):
    Sum=numbers[0][0]
    j=0
    for i in xrange(1,len(numbers)):
        j+=path[i]
        Sum+=numbers[i][j]
    
    return Sum

f=open("triangle.txt","r")

text=f.readlines()

f.close()

numbers=numpy.zeros((len(text),len(text)),dtype=int)

for i in xrange(len(text)):
    for j in xrange(i+1):
        numbers[i][j]=numpy.fromstring(text[i],dtype=int,sep=' ')[j]

path=numpy.zeros(len(numbers),dtype=int)

triSum=numbers[
