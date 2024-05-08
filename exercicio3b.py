import random

def selection(v):
    for i in range(len(v) - 1):
        minimo_indice = i
        for j in range(i + 1, len(v)):
            if v[j] < v[minimo_indice]:
                minimo_indice = j
        v[i], v[minimo_indice] = v[minimo_indice], v[i]  # Corrigido aqui

v = [5, 2, 4, 1, 3]
selection(v)
print(v)
