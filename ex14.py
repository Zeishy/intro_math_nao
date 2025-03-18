import numpy as np
import matplotlib.pyplot as plt

def nuage():
    x = np.random.randn(100)
    y = np.random.randn(100)

    plt.scatter(x, y, s=50)
    plt.title('Nuage de points aléatoires')
    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')
    plt.show()

nuage()