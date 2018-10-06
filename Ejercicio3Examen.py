#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
# 3.- Hacer una pila y regresar los valores invertidos (mas actual a antiguo)

index = 0
class Stack:
    def __init__(self):
        self.pila = [] # Se crea la pila
    
    def push(self, item, maxIndex):                                         
         global index # Se declara index como un parametro global
         if index < maxIndex:              
             self.pila.append(item) # Al metodo append recibe el parametro item
             index += 1
         else:
             print("Error")
         
    def peek(self, maxIndex):                                                  
        for x in range(maxIndex - 1, -1, -1): # Mostrara los datos invertidos
                        print ("Version" + str(x+1) + ": "+ str(self.pila[x])) # Muestra "Version" + "ultimo numero de version" + "valor de x"
                    
Versiones = Stack()
Numerov = int(input("Numero de versiones: ")) # El usuario ingresa el numero de versiones de los proyectos.
for x in range(0, Numerov): # Se define el valor que el usuario ingreso como limite.
    Versiones.push(input("Version " + str(x+1) + ": "),Numerov) # Se añaden las versiones...
print("\nListado de versiones (actual-antiguo): ")
Versiones.peek(Numerov) # Consulta de los datos agregados llamando al metodo peek().
