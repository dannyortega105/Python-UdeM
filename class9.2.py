# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 20:53:09 2022

@author: Danny Ortega
"""

#Funciones Especiales o funaciones de orden superior
#Es una funcion como parametro de otra funcion

def funcionSuperior(funcion, x, y):
    return(funcion(x, y))

def multiplicar(x,y):
    return(x*y)

def dividir(x,y):
    return(x/y)
    
resultado1=funcionSuperior(multiplicar,6,2)
print(f'La multiplicacion da como resultado: {resultado1}')
resultado1=funcionSuperior(dividir,6,2)
print(f'La division da como resultado: {resultado1}')

#Funciones anonimas
#Funciones lambda

import math as m

r=lambda a:m.sqrt(a)
print('la raiz del numero es:',r(16))

f=lambda x,y:x+y
print(f(3,5))

#Calcular las raices de la ecuacion cuadratica
discriminante=lambda a,b,c:m.pow(b,2)-4*a*c
D=discriminante(-1,3,5)
#print(D)

x1=lambda a,b,c:(-b+m.sqrt(D))/(2*a)
x2=lambda a,b,c:(-b-m.sqrt(D))/(2*a)

print('x1',x1(-1,3,5))
print('x1',x2(-1,3,5)s)