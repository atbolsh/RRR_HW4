import math
from copy import deepcopy

import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv

import matplotlib.pyplot as plt

def kissProject(M):
    N = deepcopy(M)
    signs = np.sign(N)
    #Go to absolute values
    N = N*signs
    N = np.minimum(N, 0.5)
    #Go back
    N = N*signs
    #Must have only 1s, no -1s, on the diagonal
    np.fill_diagonal(N, 1.)
    return N           
    

   
