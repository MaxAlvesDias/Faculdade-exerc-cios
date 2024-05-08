import random

def troca(v):
    n = len(v)
    trocou = True
    while trocou:
        trocou = False
        for i in range(n - 1):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                trocou = True

vetor = list(range(0,20))
random.shuffle(vetor)
ordenar = [3, 2, 6, 5, 4, 1, 0, 7, 9, 8]
troca(ordenar)
troca(vetor)
print("ordem crescente:", ordenar)
print(vetor)
