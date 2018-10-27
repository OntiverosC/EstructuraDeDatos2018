#! /usr/bin/env python
def Factorial(n):
	if n == 0: 
		r = 1			
	else:
		r = n*Factorial(n-1)	
	return r
n = int(input('Factorial con recursividad\nIngrese numero: '))
Factorial = Factorial(n)
print(Factorial)	

n = int(input('\nFactorial con iteracion\nIngrese numero: '))
for x in range(1, n):
	n *= x
print(n)