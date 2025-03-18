import numpy as np

def normalisation(mat):
    mean = np.mean(mat, axis=0)
    std_dev = np.std(mat, axis=0)
    
    normalized_mat = (mat - mean) / std_dev
    
    return normalized_mat

matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrice_normalisee = normalisation(matrice)
print(matrice_normalisee)