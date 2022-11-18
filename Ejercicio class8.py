# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:28:03 2022

@author: Danny Ortega
"""

"""7 filas tipo de asistencia (Armamento, asesoria militar, alimentos, personal medico, entrenamiento, diplomatica, migracion)
7 columnas pais
"""

import random
asistencia = []

def matrizAleatoria():
    for i in range(0,3):
        asistencia.append([0]*3)
    #print(asistencia)
    
    for i in range(0,3):
        for j in range(0,3):
            asistencia[i][j]=(random.randint(0, 50000))
    print("La matriz creada fue: ")
    for i in asistencia:
       print(i)
    return asistencia

def totalFilas():
    vectorFila = []
    for i in range(3):
        suma = 0
        for j in range(3):
            suma = suma + matriz[i][j]
        vectorFila.append(suma)
    print(f"La suma de cada fila es: {vectorFila}")
    return vectorFila


def totalColumnas():
    vectorColumna=[]
    for j in range(3):
        suma = 0
        for i in range(3):
            suma = suma + matriz[i][j]
        vectorColumna.append(suma)
    print(f"La suma de las columnas es: {vectorColumna}")
    return vectorColumna
       
def mayorAsistencia():
    mayor = max(vectorColumna)
    print(f"La mayor asistencia es: {mayor}")
    
def menosAsistenciaBrindada():
    menor = min(vectorFila)
    print(f"La menor asistencia es: {menor}")
    
def menor():
    minimo = matriz[1][1]
    for i in range(3):
        for j in range (3):
            if matriz[i][j]<minimo:
                minimo=matriz[i][j]
    print(f"La minima asistencia de todo es: {minimo}")
    
def mayor():
    mayor = matriz[1][1]
    for i in range(3):
        for j in range (3):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
    print(f"La mayor asistencia de todo es: {mayor}")
    
matriz = matrizAleatoria()    
vectorFila = totalFilas()
vectorColumna = totalColumnas()
mayorAsistencia()
menosAsistenciaBrindada()
menor()
mayor()