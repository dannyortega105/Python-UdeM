# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:47:29 2022

@author: Danny Ortega
"""

def conteoPalabra():
    palabra = input("Escribe una palabra o frase: ")
    letra = input("Escribe la letra que quieres buscar: ")
    conteo = palabra.count(letra)
    print(f"La cantidad de letra O que hay en esa palabra son: {conteo}")
    
def conteoPalabra2():
    conteo = 0
    palabra = input("Escribe una palabra o frase: ")
    letra = input("Escribe la letra que quieres buscar: ")
    for i in palabra:
        if i== letra.upper() or i== letra.lower():
            conteo +=1
    print(f"la cantidad de letra {letra} que hay en esa palabra son: {conteo}")
#conteoPalabra()
#conteoPalabra2()

"""lista = [23,False,True,'python',78.3]
sublista=lista[:0]
print(sublista)"""
import random
"""def crearVector(rango):
    
    A=[0]*rango
    for i in range(rango):
        A[i]=random.random()*100
    return A


def promedio(B):
    suma = 0
    for i in range(n):
        suma=suma+B[i]
    prom=suma/len(B)
    return(prom)
n=int(input("Digite el rango para el vector: "))
B = crearVector(n)
p = promedio(B)
print(f"El vector creado es: {B} y su promedio es: {p:.2f}")"""


##metodo que permita organizar un vector de forma decendente METODO BURBUJa o intercambio directo

def crearVectorDecendente():
    rango=int(input("Digite el rango para el vector: "))    
    A=[0]*rango
    for i in range(rango):
        A[i]=random.random()*100
    x= A.reverse()
    print(x)

#crearVectorDecendente()

f = int(input("digite filas: "))
c = int(input("digite columnas: "))
m=[]
for i in range(f):
    m.append([0]*c)

for i in m:
    print(i)
#Generacion de array por indexación
for i in range (f):
    for j in range(c):
        #dato=int(input("Digite dato: "))
        m[i][j]=random.randint(0,100)

print("La matriz creada fue: ")
for i in m:
    print(i)

#Otra forma de generar la matriz es
print('generación de array por comprensión')
A=[[random.randint(0, 100)for i in range (f)]for j in range(c)]
for i in A:
    print(i)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    