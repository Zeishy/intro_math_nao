import numpy as np

def initialisation(lines, cols):
    matrice2d = np.random.randint(1, 101, size=(lines, cols))
    matrice2d[:, -1] = 1
    print(matrice2d)

initialisation(4, 3)