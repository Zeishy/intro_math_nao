import numpy as np

def super_square(lines, cols):
    A = np.zeros((lines, cols))
    
    A[0, :] = 1
    A[-1, :] = 1
    A[:, 0] = 1
    A[:, -1] = 1
    
    return A

resultat = super_square(5, 5)
print(resultat)