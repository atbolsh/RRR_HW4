import math
from copy import deepcopy

import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv

import matplotlib.pyplot as plt



def linProject(A, H, val):
    """Project onto surface A*H = val"""
    #Product is element-wise
    d = np.sum(A*H)
    n = np.sum(H*H)
    return A + ((val - d)/n)*H

def lowerBoundProject(A, H, val):
    d = np.sum(A*H)
    if d <= val:
        return A
    else:
        n = np.sum(H*H)
        return A + ((val - d)/n)*H


