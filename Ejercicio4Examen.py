#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
# 4.- Hacer una cola con un maximo de 5 elementos

index = 0
class Queue():       

    def __init__(self):                  
        self.cola = [0,0,0,0,0] # Se indica el numero de elemntos que tendra la cola
    
    def push(self,dato): # Metodo para añadir elementos
        global index # se declara index como global
        self.cola[index] = dato
        index+=1
    
    def peek(self): # Metodo para eliminar elementos 
        global index
        if index!=0:
            print(str("\n\tCliente numero: " + str(self.cola[0])) + " abandono la cola") # Muestra: "Cliente numero:" + "valor en x" + "abandono la cola"
            for x in range(0,4): # Se define el rango de los valores que se guardaran en x
                self.cola[x] = self.cola[x+1]     
            self.cola[4]=0 # Cola con capacidad del 0-4
            index -=1
        else:   
            print("\nLugar libre en la cola")

def Menu(): # Menu ciclico 
    cola = Queue()
    while True:  
        print("\nMENU:\n1.-Cliente nuevo\n2.-Cliente atendido\n3.-Cerrado\n") 
        dato = int(input("Ingrese opcion:  ")) # El usuario puede ingresar un numero equivalente a cada opcion a elegir
        if dato==1:  # Compara el numero que ingreso el usuario para realizar una accion.
            if index <= 4:
                num = int(input("\n\tNumero de cliente: ")) # Se contabiliza a los clientes 
                cola.push(num) # Se añade al metodo push()
            else:
                print("\n\tNo hay lugar disponible en la cola") # Imprime en caso de que la cola este llena
        elif dato==2: # Compara el numero que ingreso el usuario para realizar una accion.
            cola.peek() # En este metodo se realizan consultas, lo que hara es eliminar uno de los elementos guardados
            
        elif dato==3: # Compara el numero que ingreso el usuario para realizar una accion.
            exit() # Se termina el ciclo
        else:
            print("\n\tOpcion invalida") # En caso de que se ingrese un numero erroneo
    
Menu() # Llama al menu