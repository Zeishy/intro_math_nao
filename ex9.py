import matplotlib.pyplot as plt

def double_graphic():
    x = [1, 2, 3, 4, 5]
    y1 = [10, 20, 25, 30, 40]
    y2 = [5, 15, 20, 25, 35]

    plt.plot(x, y1, color='red', linestyle='-', label='Courbe 1')
    plt.plot(x, y2, color='blue', linestyle='--', label='Courbe 2')

    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')

    plt.title('Graphique des courbes double')
    plt.grid(True)
    plt.legend()
    plt.show()

double_graphic()