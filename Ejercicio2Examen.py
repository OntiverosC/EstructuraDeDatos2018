#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
def Numero(n):   
  if n==0:                                     
    return 1         
  else:
      return 2*Numero(n -1)
r = int(input("Grado de potencia: "))
print("Resultado: ")
print(Numero(r))
