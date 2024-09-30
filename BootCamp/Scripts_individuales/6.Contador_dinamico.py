print(' ')
print('#6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.')
print(' ')
numInicial=1
numFinal=50
multiplo=5
for res in range(numInicial, numFinal + 1):
    if res % multiplo == 0:
        print(res)