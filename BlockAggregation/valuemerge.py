#!/usr/bin/env python
# -*- coding: utf-8 -*-

def minmerge(minval, a):

    if a < minval:
        return a
    else:
        return minval

def maxmerge(maxval, a):

    if a > maxval:
        return a
    else:
        return maxval

def summerge(sumvalue, a):

    sumvalue = sumvalue + a
    return sumvalue


