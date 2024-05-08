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



nomes = ["Max","Ana","Henrique","Emanuel" ]
troca(nomes)

n = len(nomes)
entrada_usuario = input("Digite o nome de um usuario: ")
local = -1
for i in range(n):
    if nomes[i] == entrada_usuario:
        local = i
if local > -1:
    print("O nome ",entrada_usuario, " esta posição:", local)
else:
    print("Esse nome não existe na lista")

print("ordem crescente:", nomes)
