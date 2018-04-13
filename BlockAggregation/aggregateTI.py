#!/usr/bin/env python
# -*- coding: utf-8 -*-


def countdist(data):
    
    result= [0] * len(data)+1
    result[0]=1000000

    i = 0
    while i < len(data):

        ex = data[i]
        nex = 1000000-ex
        result = (result[0]*nex)/1000000

        j = 1
        while j < i+1:
            result[j] = ((result[j]*nex) + (result[j-1]*ex))
        
        result[i+1] = result[i]*ex

    return result

def countrange(data):

    pass


def countexpected(data):

    pass

def sumdist(data):

    pass

def sumrange(data):

    pass


def sumexpected(data):

    pass

def minvalue(minval, a):

    if a < minval:
        return a
    else:
        return minval

def maxvalue(maxval, a):

    if a > maxval:
        return a
    else:
        return maxval

def sumvalue(sumvalue, a):

    sumvalue = sumvalue + a
    return sumvalue

def distagg(atype, data):

    pass

def rangeagg(atype, data):

    pass



