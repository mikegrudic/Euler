#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy
from optparse import OptionParser
from subprocess import call

def nWords(d1,d2,d3,d4):
    words=""

    digits=(["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
    tensDigits=(["twenty", "thirty","forty", "fifty", "sixty", "seventy", "eighty", "ninety"])
    teens=(["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"])

    if (d1!=0): words+=digits[d1]+"thousand"
    if (d2!=0): words+=digits[d2]+"hundred"
    if (d3!=0):
        if (d1!=0 or d2!=0): words+="and"
        if (d3*10+d4>19): 
            words+=tensDigits[d3-2]
            if (d4!=0): words+=digits[d4]
        elif(d3*10+d4>9): words+=teens[d4]
        else: words+="and"+digits[d4]
    elif((d2>0 or d1>0) and d4!=0):
        words+="and"+digits[d4]
    elif(d4!=0): 
        words+=digits[d4]
    
    print len(words), words

    return len(words)

letters=0

for k in xrange(10):
    for j in xrange(10):
        for i in xrange(10):
            letters+=nWords(0,k,j,i)
            
letters=letters+len("onethousand")

print letters
