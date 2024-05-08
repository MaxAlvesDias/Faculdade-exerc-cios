def busca_binaria(lista, valor):

    primeiro = 0
    ultimo = len(lista) -1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            primeiro = meio + 1
        else:
            ultimo = meio - 1
    return -1

lista = [1,3,5,7,9]
valor = 5
indice = busca_binaria(lista, valor)

if indice != -1:
    print("O valor", valor ,"esta no indice", indice)
else:
    print("O valor", valor, "não foi encontrado na lista:")
        