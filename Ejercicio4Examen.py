#! /usr/bin/env python
# Ontiveros Lara Claudia Sarahi.
# 4.- Hacer una cola con un maximo de 5 elementos

index = 0
class Queue():       

    def __init__(self):                  
        self.cola = [0,0,0,0,0]          
    
    def push(self,dato):                 
        global index
        self.cola[index] = dato
        index += 1
    
    def peek(self):                     
        global index
        if index!=0:
            print(str("\n\tCliente numero: [" + str(self.cola[0])) + "] abandono la cola")
            for x in range(0,4):
                self.cola[x] = self.cola[x+1]     
            self.cola[4] = 0
            index -= 1
        else:   
            print("\nLugar disponible en la cola")

def Menu():              
    cola = Queue()
    while True:                  
        print("\nMENU\n1.-Cliente nuevo\n2.-Cliente atendido\n3.-Cerrado\n")     
        dato = int(input("Opcion:  "))
        if dato == 1:                                              
            if index <= 4:
                num = int(input("\n\tNumero de cliente: "))  
                cola.push(num)
            else:
                print("\n\tNo hay lugar disponible en la cola")
        elif dato == 2:                               
            cola.peek()                             
            
        elif dato == 3:                              
            exit()                                 
        else:
            print("\n\tOpcion invalida")
    
Menu() 