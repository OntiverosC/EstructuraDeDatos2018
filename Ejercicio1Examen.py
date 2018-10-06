#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
def Sumatoria(n):                  
  if n==1:                                     
    return 1         
  else:
      return Sumatoria(n-1)+n 
print(Sumatoria(9)) 
