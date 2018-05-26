import sys
import pandas as pds
import os


def countdist(dframe, tprob, maxprob=1000000.0):
    skdjfhskdjfh
    kjsdhfkhsdkfj
    kshdkfhsdkjfh
    bottom = len(dframe[dframe[tprob]==maxprob])
    uncertain = dframe[dframe[tprob] < maxprob]

def countrange(dframe, tprob, maxprob=1000000.0):

    maxcount = len(dframe)
    mincount = len(dframe[dframe[tprop] == maxprob])
    return mincount, maxcount
def countexp(dframe, tprob, maxprob=1000000.0):

    margcounts = dframe[tprob]

    return margcounts.sum()/maxprob
def sumdist(dframe, tprob, tval, maxprob=1000000.0):
    pass
def sumrange(dframe, tprob, tval, maxprob=1000000.0):

    maxsum = dframe[tval].sum()
    minsum = dframe[dframe[tval] == maxprob][tval].sum()

    return minsum, maxsum
def sumexp(dframe, tprob, tval, maxprob=1000000.0):

    margsums = dframe[tprob]*dframe[tval]

    return margsums.sum()/maxprob
def maxdist(dframe, tprob, tval, maxprob=1000000.0):

    pass
def maxrange(dframe, tprob, tval, maxprob=1000000.0):

    maxmax = dframe[tval].max()
    minmax = dframe[dframe[tprop] == maxprob][tval].max()

    return minmax, maxmax
def maxexp(dframe, tprob, tval, maxprob=1000000.0):

    pass
def mindist(dframe, tprob, tval, maxprob=1000000.0):

    pass
def minrange(dframe, tprob, tval, maxprob=1000000.0):

    minmin = dframe[tval].min()
    maxmin = dframe[dframe[tprop] == maxprob][tval].min()

    return minmin, maxmin
def minexp(dframe, tprob, tval, maxprob=1000000.0):

    pass
if __name__ == '__main__':
    #unittest.main()
    print(os.getcwd())
    test()
