import math
from copy import deepcopy

import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv
from numpy.linalg import svd

import matplotlib.pyplot as plt

def spinGlassProject(A, sG = True):
   spins = extractSpins(A)
   return np.outer(spins, spins)

def extractSpins(A):
   u, s, vh = svd(A)
   vh = np.sign(vh)
   return vh[0]


