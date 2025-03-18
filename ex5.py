from scipy import datasets
import matplotlib.pyplot as plt

face = datasets.face(gray=True) # L'image
plt.imshow(face, cmap=plt.cm.gray) # On convertit l'image en gris par simplicité


zoomed_face = face[100:300, 100:300]
plt.imshow(zoomed_face, cmap=plt.cm.gray)
plt.show() # Afficher l'image (on y reviendra plus tard)

saturated_face = face.copy()
saturated_face[saturated_face < 127] = 0
plt.imshow(saturated_face, cmap=plt.cm.gray)
plt.show() # Afficher l'image (on y reviendra plus tard)
