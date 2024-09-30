print(' ')
print('#5.Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.')
print(' ')
print('los numeros son:')
for npar in range(2024, 0, -3):
    if npar % 2 == 0:
        print(npar)