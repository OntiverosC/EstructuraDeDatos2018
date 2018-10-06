#! /usr/bin/env python
#Ontiveros Lara Claudia Sarahi.
index = 0
class Stack:
    def __init__(self):
        self.pila = []
    
    def push(self, item, maxIndex):                                         
         global index
         if index < maxIndex:             
             self.pila.append(item)
             index += 1
         else:
             print("Error")
         
    def peek(self, maxIndex):                                                  
        for x in range(maxIndex - 1, -1, -1):
                        print ("Version"+ str(x+1) + ": "+ str(self.pila[x]))
                    
Versiones = Stack()
Numerov = int(input("Numero de versiones: "))
for x in range(0, Numerov):
    Versiones.push(input("Version " + str(x+1) + ": "),Numerov)
print("\nListado de versiones (actual-antiguo): ")
Versiones.peek(Numerov)
