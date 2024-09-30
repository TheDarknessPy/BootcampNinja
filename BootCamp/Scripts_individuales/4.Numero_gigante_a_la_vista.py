print('')
print('#4.Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).')
print('')
sm=0
for npar in range(0, 500001):
    if npar % 2 == 0:
        sm += npar
print('la suma es',sm)