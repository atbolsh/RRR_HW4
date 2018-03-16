import math
from copy import deepcopy

import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv

import matplotlib.pyplot as plt

def semiDefProject(X):
   return np.real((X + X.transpose())*0.5)

def rankProject(X, rank=1, unitary=True):
   l = np.shape(X)[0]
   M = semiDefProject(X)
   vals, x = eig(M)
   #Indeces for sorting
   ind = np.argsort(vals)
   #Indeces for reverse sorting
   rev_ind = np.argsort(ind)
   s = vals[ind]
   s[:-rank] = 0
   if unitary:
      s[-rank:] = 1
   else:
      s = np.maximum(s, 0) #Positive semi-definite   
   vals = s[rev_ind]
   return np.matmul(x, np.matmul(np.identity(l)*vals, inv(x)))


   
   





