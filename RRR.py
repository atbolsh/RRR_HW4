import numpy as np
from numpy.linalg import norm
import random as r

def RRR_error(v, proj1, proj2):
    b = proj2(v)
    a = proj1(2*b - v)
    return a - b

def RRR(v, proj1, proj2, beta=0.5, cutoff = 0.0001, maxIter=10000, errors=True):
    error = 1000*np.ones(np.shape(v)) #Nonzero initial error
    i = 0
    trace = []
    while norm(error) > cutoff and i < maxIter:
        i += 1
        error = RRR_error(v, proj1, proj2)
        v = v + beta*error
        if errors:
            trace.append(norm(error))
    if norm(error) > cutoff:
        print "Warning: maximum iterations exceeded, no convergence"
    if errors:
        return v, trace, proj1(v)
    else:
        return v, proj1(v)




