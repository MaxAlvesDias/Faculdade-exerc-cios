def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print("Mova disco 1 de", origem, "para", destino) # usando
        return 1
    hanoi(n - 1, origem, auxiliar, destino)
    print("Mova disco", n, "de", origem, "para", destino)
    hanoi(n - 1, auxiliar, destino, origem)


n = 3
hanoi(n, 'A', 'C', 'B')
