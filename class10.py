# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 18:39:13 2022

@author: Danny Ortega
"""
"""
#Repaso funciones Lambda
lista_numerica=[2,3,4,6,78,10,7]
funcionL=lambda *args:sum(args)
print(funcionL(*lista_numerica))

dicc={"A":1,"B":2,"C":3}
#Sorted para organizar
print(sorted(dicc, key =lambda x:dicc[x]%3))
"""
from functools import reduce
"""
#funcion reduce (Python no la trae por defecto) esta funcion coge un iterable (vector, lista, tupla, etc) y conseguir un solo valor con esto
lista=list(range(5,100,10))
print(lista)

funcion=reduce(lambda x,y:x+y,lista)/len(lista)
print(funcion)
"""
"""
#funcion filtrar
    
lista=list(range(5,100,10))
print(lista)


A=list(filter(lambda x:x%3==0,lista))
B=list(filter(lambda x:x>=50 and x<80,lista))
print(A)
print(B)
"""

"""
def numeroCinco(num1):
    if num1%5==0:
        return True
    
numero1=list(range(100))
print(numero1)
print("La lista filtrada es: ",list(filter(numeroCinco,numero1)))
"""

"""
lista=list(range(5,100,10))
print(lista)

multi=list(map(lambda x:x**2,lista))
print(multi)

f=lambda x,y=2:x+y
print(list(map(f,lista)))
"""
import time
#Funcion ZIP INVESTIGAR

#Recursividad
#Se usa menos codigo y hace que sea mas facil de leer y de mantener
#No es tan eficiente porque la maquina usa mas recursos para ejecutarlo
"""
def imprimir(x):
    while x>=1:
        print(x)
        x-=1

imprimir(10)
"""
#No recursiva
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input("Ingresa un numero: "))
fact=factorial(n)
print(fact)


#Recuersivo

def factorialRecursiva(n):
    
    if n ==1:
        return 1
    else:
        
        return(n*factorial(n-1))

startr=time.time()
fact1=factorialRecursiva(n)
endr=time.time()
tiempor=endr-startr
print(fact1)
print(tiempor)






