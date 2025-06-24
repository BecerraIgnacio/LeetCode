word = "ahahnhahhah"
k = 1

def ejercicio(word, k):
    letras = []
    cantidad = []
    for letter in word:
        if letter not in letras:
            letras.append(letter)
            cantidad.append(1)
        else:
            i = letras.index(letter)
            cantidad[i] += 1
    print(letras)
    print(cantidad)
    suma = [0] * len(cantidad)
    for i in range(len(cantidad)):
        for j in range(len(cantidad)):
            if cantidad[i] != cantidad[j] and not abs(cantidad[i] - cantidad[j]) <= k:
                if cantidad[i] > cantidad[j]:
                    suma[i] += cantidad[j]
                else:
                    suma[i] += cantidad[j]-(cantidad[i]+k)
    print(suma)
    if all(v == 0 for v in suma): return 0
    indice = suma.index(min(suma))
    print(cantidad[indice])
    minimo = 0
    for i in range(len(cantidad)):
        if cantidad[i] > cantidad[indice]+k//2:
            minimo += cantidad[i]-(cantidad[indice]+k)
        if cantidad[i] < cantidad[indice]-k//2:
            minimo += cantidad[i]
    return minimo


print(ejercicio(word, k))