# Workshop - Les librairies mathématique, statistique et graphique en Python

Bienvenue dans cet atelier concernant les librairies mathématiques Python.
En vérité il s'agit d'un atelier principalement axé sur `numpy` et `matplotlib`.
Les exercices que nous allons faire vont probablement vous servir dans le contexte de Deep Learning,
mais également dans le contexte de la Data Science en général. Sans plus tarder, commençons.


## 0.1 Environnement Python
Flemme de casser votre système d'exploitation et votre python ? Je vous comprends. Mon Arch Linux a hurlé, sachez-le.
Apprenez dans un premier temps à **créer un environnement python**. Appellez-moi avant de passer à l'étape suivante pour la vérification.

## 0.2 Installation
Créez un fichier `requirements.txt`. Le but de ce fichier est de faire en sorte que chaque installation de projet soit simple.
Cela semble rien du tout comme ça, mais je vous assure que ça fait gagner un temps astronomique.

# 1.0 Numpy

NumPy, c'est LA bibliothèque fondamentale en Python utilisée pour le calcul scientifique et l'analyse de données.
Sa principale force, c'est les tableaux multidimensionnels (les matrices) et sa grande collection de fonctions mathématiques pour manipuler ces tableaux. 
NumPy est largement utilisé pour ses performances élevées et sa capacité à effectuer des opérations sur de grands ensembles de données de manière efficace.
Nous allons étudier quelques fonctions qui vous seront utile.

## 1.1 Créer un tableau et une matrice
Utilisez Numpy afin de créer un tableau. A première vue, cela n'est pas différent d'un tableau classique,
mais je vous assure que ce tableau est bien plus performant et efficace que ces derniers.
Voici un lien qui pourrait vous permettre de tester un peu, et ainsi [de faire un tableau](https:/e/numpy.org/doc/2.2/user/absolute_beginners.html).

## 1.2 Random 2-dimension array
Créez un tableau en 2 dimensions avec des valeurs complètements aléatoires. Pour cela,
n'hésitez pas à consulter `numpy.random.randn()`
et les autres fonctions aléatoires.
Vous espérez un lien ? Bah débrouillez-vous. Il faut chercher un peu bande d'enfants.
- Je veux un tableau de 3 lignes et 4 colonnes avec des valeurs comprises entre 1 et 100.
- Cherchez la fonction vous permettant d'atteindre cet objectif.

## 1.3 2-dimension full of 0 and 1 array (a lot of numbers)
- Utilisez une fonction vous permettant de faire une matrice rempli de 1.
- Ecrivez une fonction `my_full_of_1_arr(lines, columns)`qui AFFICHE un array, 
ainsi que son nombre de lignes et de colonnes. **Vous n'afficherez pas explicitement
`lines` et `columns` (c'est à dire pas de `print(lines)` ou `print(columns)`).

## 1.4 Slicing in numpy arrays
Prenez le code suivant:
```python
import numpy as np

A = np.ones(5,5)
...
print(A)
## Expected

# [[1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 1.]
# [1. 0. 0. 0. 1.]
# [1. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1.]]
```
- Faites en sorte de disposer d'une matrice qui a toujours les côtés remplis de 1.
C'est à dire que les premières et dernières lignes et colonnes doivent être des 1.
- Faites en une fonction `super_square(lines, cols)`.

## 1.5 Zoomer une image avec des maths ?
Allez on va voir si vous avez compris le slicing.
Prenez le code suivant
```python
from scipy import datasets
import matplotlib.pyplot as plt

face = datasets.face(gray=True) # L'image
plt.imshow(face, cmap=plt.cm.gray) # On convertit l'image en gris par simplicité
plt.show() # Afficher l'image (on y reviendra plus tard)
```
Ce code devrait vous afficher un râton laveur. Cool ! Mais j'aimerai zoomer sur son gros crâne.
Vous remarquerez que `face` n'est en vérité qu'une matrice représentant chaque pixels de 
0 à 255 (noir à blanc).
- Zoomez vers le milieu de l'image. Pour cela, utilisez le slicing.
- On va désormais saturer cette même image. Pour cela, c'est simple : disons que
chaque pixels inférieur à 127 doit être égale à 0 (ou une valeur de votre choix).
Vous pouvez faire ça très simplement avec le [boolean indexing](https://numpy.org/doc/2.2/user/basics.indexing.html#boolean-array-indexing).
Soyez vraiment simple en utilisant cette feature. Vous serez surpris du résultat !

## 1.6 Une matrice vraiment utile !
- Faites une matrice de nombres aléatoires avec `randn().
- Une fois cette matrice générée, ajoutez une colonne de 1 comme cela:
```
[X X X X 1]
[X X X X 1]
[X X X X 1]
[X X X X 1]
[X X X X 1]

Où X est un nombre aléatoire.
```
- Pour cela, utilisez la fonction `concatenate()`. N'hésitez pas à vous renseigner sur
cette fonction et sur l'option `axis`. Cela pourrait s'avérer utile !
- Faites en une fonction `initialisation(lines, cols)`.

## 1.7 Standardisation par la normalisation
Ok, on a vu des choses qui sont utilisés avec numpy, mais la vérité,
c'est que plusieurs de ces fonctionnalités ne sont pas utiles seuls.
La matrice que l'on a créé précédemment est une matrice avec un biais de 1.
C'est une notion vraiment utilisé dans le monde de la data science. Cela
démontre alors pourquoi la manipulation de tableaux est utile. Mais ce n'est pas la 
seule chose que l'on peut faire en data science. Des fois, il faut manipuler les données
 et en faire des statistiques. Des fois, les données ne sont pas à l'échelle, et c'est
relou si vous faites du deep learning par exemple... au hasard...
Il est donc important de faire de la statistique et de normaliser nos données !
Je vous donne les méthodes suivantes : `std()`, `mean()`. N'hésitez pas à les utiliser
afin de comprendre comment ça fonctionne !
- Utilisez les fonctions données pour faire une [normalisation z-score](https://www.statology.org/z-score-normalization/).
- N'utilisez pas cette notion sur la matrice directement ! Faites-le
sur chaque colonne de cette matrice.
- Faites une fonction `normalisation(mat)` qui prend une matrice et qui renvoie une matrice
avec les colonnes normalisées. PAS LES LIGNES, LES COLONNES.

Bon, on a fait des choses avec numpy, et normalement vous savez manipuler des données.
On va pas faire le tour de toutes les fonctions mathématiques et statistiques (parce qu'il y en a trop), mais vous savez
faire les tours de passe-passe basique désormais. Pour utiliser le reste, il faudra juste lire la doc, utiliser les
notions associés, faire en sorte de traduire sous forme de code, et voilà. Vous savez utiliser numpy.

# 2.0 Matplotlib

Pouvoir faire des tableaux et matrices c'est cool, mais visualiser les données et savoir ce que représente ces dernières,
c'est pratique aussi. Avec matplotlib, vous pouvez devenir le vendeur de tapis que vous pensez être.
Bon : commençons ?

## 2.1 Un graphique basique
Créez un graphique linéaire simple en utilisant `matplotlib`. Utilisez les données suivantes :
  ```python
  x = [1, 2, 3, 4, 5]
  y = [10, 20, 25, 30, 40]
```
- Ajoutez des labels aux axes (xlabel, ylabel).
- Ajoutez un titre au graphique.
- Changez la couleur de la ligne en rouge.
- Affichez une grille en arrière-plan.

## 2.2 Plusieurs courbes
```python
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [5, 15, 20, 25, 35]
```
Tracez deux courbes sur le même graphique. Avec cela :
- Utilisez des styles de ligne différents pour chaque courbe (par exemple, une ligne continue et une ligne pointillée).
- Ajoutez une légende pour distinguer les deux courbes.

## 2.3 Dictionnaire : rassemblez les données
- Générez 400 données de manière complètement aléatoires.
- Ces données (ou valeurs selon vos préférences d'épelation) devront former 4 listes.
Chacune de ces listes ont une clé représentée par un string. On peut par exemple
nommer la première liste "Expérience 1", et ainsi de suite.
- Au mieux, faites une fonction `random_dataset()` qui prends un nombre entier `n` et qui retourne un dictionnaire.
Ce dictionnaire contient donc un `n` listes de nombres aléatoires avec `n` strings comme clé.
Si vous avez fait 

## 2.4 Fonction graphique
- Faites une fonction `graphique()` qui génère un graphique à partir d'un dictionnaire.
- Chaque listes du dictionnaire doit pouvoir générer un [subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html).
- Les clés composant le dictionnaire devient donc le titre du graphique.
- Soyez le plus générique possible.

## 2.5 Histogramme
-  Créez un histogramme à partir de données aléatoires. 
Pour cela, utilisez `numpy.random.normal()` pour générer 1000 points de données suivant une distribution normale.
- Petite précision, `bins=30`.
- Amusez-vous à changer la couleur et les labels. Pour cela, renseignez vous sur la distribution normale.

## 2.6 Scatter plot
- Créez un nuage de points à partir de données aléatoires.
Générez via `randn()` 100 points x et y.
- Les points doivent être de taille 50.
