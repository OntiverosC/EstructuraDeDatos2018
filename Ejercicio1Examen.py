#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
# 1.- Fibonacci 1-9

def Sumatoria(n): # Se le manda el parametro n al metodo que realizara la sumatoria                  
  if n==1:   # Si n fuese igual a 1 entonces...                                  
    return 1  # el resultado seria 1.       
  else:
      return Sumatoria(n-1)+n # Realiza la sumatoria por el metodo fibonacci
print("\nResultado:") # Imprime el resultado.
print(Sumatoria(9)) # No se pide ingresar el numero al usuario, sino que esta definido desde el inicio el valor del parametro.
