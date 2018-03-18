import math
from copy import deepcopy

import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv

import matplotlib.pyplot as plt

def flipVars(M, i, j, copy=False):
    if copy:
        N = deepcopy(M)
    else:
        N = M
    N[[i, j]] = N[[j, i]]
    N = N.T
    N[[i, j]] = N[[j, i]]
    N = N.T
    return N

def dagger(A, copy=True):
    return A.conj().T

   
