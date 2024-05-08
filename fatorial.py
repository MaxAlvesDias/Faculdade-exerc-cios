def fatorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * fatorial(n-1)

numero = int(input("Digite um numero para calcular seu fatorial: "))
resultado = fatorial(numero)
print("O fatorial de", numero,"é", resultado)