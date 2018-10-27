#! /usr/bin/env python
def fibonacci(n):
	if n==0 or n==1:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)
n = int(input('Fibonacci con recursividad\nIngrese un numero: '))
print fibonacci(n)

def Fibonacci(n):
    p = 1
    u = 0
    for x in range(n+1):
    	p, u = u, p + u
    return u
def Imprimir():
	n = int(input('\nFibonacci con iteracion\nIngrese un numero: '))
	for x in range(n+1):
		print(Fibonacci(x))
Imprimir()