import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('Histogramme de données aléatoires suivant une distribution normale')

plt.show()