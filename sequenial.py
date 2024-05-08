import random
lista = list(range(1,1000))
random.shuffle(lista)
n = len(lista)
entrada_usuario = int(input("Digite um numero: "))
local = -1
for i in range(n):
    if lista[i] == entrada_usuario:
        local = i
if local > -1:
    print("O numero",entrada_usuario, " esta posição:", local)
else:
    print("Esse numero não existe na lista")