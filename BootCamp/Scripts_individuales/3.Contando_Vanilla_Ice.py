print('')
print('#3. Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”')
print('')
for nmultiplos in range(1,101):
	if nmultiplos % 10 ==0:
		print('baby')
	elif nmultiplos % 5 ==0:
		print('ice ice')
	else:
		print (nmultiplos)