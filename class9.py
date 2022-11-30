# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:53:40 2022

@author: Danny Ortega
"""
#Aprendiendo de NUMPY
import numpy as np
import pandas as p
#Nucleo principal de numpy son los arrays
D=np.array([(1,2,3), (4,5,6),(7,8,9)])
print('D=', D)

D1=np.matrix([[1,2,3], [4,5,6],(7,8,9)])
print('D=', D1)

U=np.ones((4,5))
print(U)

Z=np.zeros((4,3))
print(Z)

V=np.empty((3,3))
print(V)

A=np.random.random((3,3))*10
print(A)

A1=np.random.randint(10,20,(3,3))
print(A1)

C=np.full((4,5),4)
print(C)

ME=np.arange(10,90,20)
print(ME)

MA=np.linspace(0,2,60)
print(MA)

#Matriz de identidad
I=np.eye(5,5)
print(I)

I1=np.identity(10)
print(I1)

#Matrices tridimencionales (En este caso se pone primero las columnas luego filas por eso hay 5 columnas y 3 filas)
M3D=[[[0]*5]*3]
print(M3D)
for i in M3D:
    print(M3D)
    
M2=[['*']*3]
print(M2)

print(D.dtype)
print(D.size)
print(C.shape)
c1=C.reshape(1,20)
print(c1)
print(D[0,0])

#Obtener todos los elementos de una columna 2
print(D[:,2])
#Obtener todos los elementos de la fila
print(D[2,:])
#Como sacar el maximo usando numpy
print(D.max())
print(D.sum())
print(np.sqrt(D))
print(np.std(D))

#multiplicacion matricial
E=np.random.random((3,3))
print('E',E)
F=np.random.random((3,3))
print('F',F)
multiplicar=E.dot(F)
print('M',multiplicar)
#Transponer
print(E.transpose())