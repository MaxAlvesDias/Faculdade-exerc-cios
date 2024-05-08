import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Maxsuenaldy Alves Dias Engenharia de software 5ºperiodo

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort(esquerda) + meio + quicksort(direita)

def atualizar(frame):
    global rects, data
    ax.clear()
    sorted_data = quicksort(data[:frame + 1]) + data[frame + 1:]
    rects = ax.bar(range(len(sorted_data)), sorted_data, color='lightblue')
    ax.set_ylim(0, 20)
data = [9,5,7,2,1,6,3,10]

fig, ax = plt.subplots()
ax.set_xlim(0, len(data))
ax.set_ylim(0, 20)

rects = ax.bar(range(len(data)), data, color='lightblue')
ani = animation.FuncAnimation(fig, atualizar, frames=20, interval=1000, repeat=False)
plt.show()
