import matplotlib.pyplot as plt

def graphique(data_dict):
    num_plots = len(data_dict)
    fig, axs = plt.subplots(num_plots, 1, figsize=(10, 5 * num_plots))

    for i, (key, values) in enumerate(data_dict.items()):
        axs[i].plot(values)
        axs[i].set_title(key)
        axs[i].grid(True)

    plt.tight_layout()
    plt.show()

data = {
    "Expérience 1": [1, 2, 3, 4, 5],
    "Expérience 2": [5, 4, 3, 2, 1],
    "Expérience 3": [2, 3, 5, 7, 11]
}

graphique(data)