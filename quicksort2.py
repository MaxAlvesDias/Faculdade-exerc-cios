import matplotlib.pyplot as plt
import numpy as np

# Função para plotar o gráfico
def plot_graph(data, colors, title):
    plt.clf()
    plt.bar(range(len(data)), data, color=colors)
    plt.title(title)
    plt.pause(0.5)  # Ajuste o tempo de pausa aqui (em segundos)

# Algoritmo Quicksort
def quicksort(data, low, high, step=1):
    if low < high:
        pivot_index = partition(data, low, high)
        title = f'Step {step}: Subarray from index {low} to {pivot_index} and from index {pivot_index+1} to {high}'
        quicksort(data, low, pivot_index, step + 1)
        quicksort(data, pivot_index + 1, high, step + 1)
        plot_graph(data, ['blue' if x == pivot_index else 'green' if low <= x <= high else 'white' for x in range(len(data))], title)

# Função para particionar a lista
def partition(data, low, high):
    pivot = data[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while data[i] < pivot:
            i += 1

        j -= 1
        while data[j] > pivot:
            j -= 1

        if i >= j:
            return j

        data[i], data[j] = data[j], data[i]

# Lista de números a serem ordenados
data = np.random.randint(1, 100, 20)

# Plot inicial
plt.bar(range(len(data)), data, color='green')
plt.title('Original Array')
plt.show()

# Chamada para Quicksort
quicksort(data, 0, len(data) - 1)

# Plot final
plt.bar(range(len(data)), data, color='green')
plt.title('Sorted Array')
plt.show()
