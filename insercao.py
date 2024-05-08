def insercao(v):
    n = len(v)

    for i in range(1, n):
        x= v[i]
        j = i-1

        while j >= 0 and v[j]> x:
            v[j], v[j+1] = v[j + 1], v[j]
            j -= 1
    return v
    

ordenar = [3,2,6,5,4,1,0,7,9,8]
insercao(ordenar)
print("ordem crescente", ordenar)
