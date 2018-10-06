#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
# 2.- Potencia n del numero 2.

def Numero(n):   # El parametro n se guarda en el metodo Numero.
  if n==0:       # Si n = 0, entonces... 
    return 1     # regresa 1 porque cualquier numero elevado a 0 es 1.                               
  else:
      return 2*Numero(n -1) # Se realiza la operacion en donde 2 es el numero base y n el valor agregado por el usuario.
r = int(input("Grado de potencia: ")) # Pide un valor n al usuario, donde n es la potencia.
print("\nResultado: ")
print(Numero(r))
