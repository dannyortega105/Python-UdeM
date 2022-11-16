# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:41:03 2022

@author: Danny Ortega
"""

#Sacar la moda(El dato que mas se repite)
import random
def crearMatriz(f,c):
    M=[[random.randint(1,50) for i in range(c)] for j in range (f)]
    return M
        
def moda(M, f,c):
    contm=0
    for i in range(f):
        for j in range(c):
            dato=M[i][j]
            cont=0
            for k in range(f):
                for l in range(c):
                    if M[k][l]==dato:
                        cont+=1
            if cont>contm:
                moda=dato
                contm=cont
            if contm ==1:
                moda=None
                contm=0
    return moda, contm
    
def sumafilas(M,f,c):
    for i in range(f):
        sf=0
        for j in range(c):
            sf=sf+M[i][j]
        print(f"La suma de la fila {i} es: {sf}")
        
def sumaColumnas(M,f,c):
    for j in range(c):
        sc=0
        for i in range(f):
            sc=sc+M[i][j]
        print(f"La suma de la columna {j} es: {sc}")
        
def Buscar(A,f,c,db):
    ie=None
    je=None
    for i in range(f):
        for j in range(c):
            if A[i][j]==db:
                ie=i
                je=j
            
                
    return ie, je
    

#Principal

f=int(input("Digite la cantidad de filas: "))
c=int(input("Digita la cantidad de columnas: "))
A=crearMatriz(f, c)
for i in A:
    print(i)
Moda, Cont=moda(A, f, c)
print(f"La moda es: {Moda} y se repite {Cont} veces")
sumafilas(A, f, c)
sumaColumnas(A, f, c)
db=int(input("Digite dato a buscar: "))
fila, columna=Buscar(A,f,c,db)




    
    
    
    
    