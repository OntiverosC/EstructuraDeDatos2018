#! /usr/bin/env python
index = 0
class Queue():       

    def __init__(self):                  
        self.cola = [0,0,0,0,0]          
    
    def push(self,dato):                 
        global index
        self.cola[index] = dato
        index += 1

def Opcion():
    col = Queue()
    while True:
        print("\n1.- Insertar un numero\n2.- Salir\n")
        dato = int(input("Opcion:  "))
        if dato == 1:
            if index <= 4:
                num = int(input("\n\tNumero a insertar: "))  
                col.push(num)
            else:
                print("\n\tNo hay lugar disponible en la cola\n\n")

        elif dato == 2:
            exit()

        else:
            print("\n\tOpcion invalida")

Opcion()
