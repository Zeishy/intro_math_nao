import matplotlib.pyplot as plt

def basic_graph():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]

    plt.plot(x, y, color='red')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('2.1 gvng')
    plt.grid(True)
    plt.show()

basic_graph()