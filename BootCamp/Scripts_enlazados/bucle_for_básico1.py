print('')
print('#1. Básico: imprime todos los números enteros del 0 al 100.')
print('')
for i in range(101):
	print(i)


print(' ')
print(' ')
print('#2.Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500')
print('')
for m2 in range(2,501):
	if m2 % 2 ==0:
		print(m2)
  

print(' ')  
print(' ')
print('#3.Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”')
print('')
for nmultiplos in range(1,101):
	if nmultiplos % 10 ==0:
		print('baby')
	elif nmultiplos % 5 ==0:
		print('ice ice')
	else:
		print (nmultiplos)

print(' ')
print(' ')
print('#4.Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).')
print('')
sm=0
for npar in range(0, 500001):
    if npar % 2 == 0:
        sm += npar
print('la suma es',sm)

print(' ')
print(' ')
print('#5.Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.')
print(' ')
print('los numeros son:')
for npar in range(2024, 0, -3):
    if npar % 2 == 0:
        print(npar)
        
        
print(' ')
print(' ')
print('#6.Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo')
print(' ')
numInicial=1
numFinal=50
multiplo=5
for res in range(numInicial, numFinal + 1):
    if res % multiplo == 0:
        print(res)