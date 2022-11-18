# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:45:38 2022

@author: Danny Ortega
"""

#Personalizar el error

def categoriaCiudad():
    poblacion = int(input("Digite la cantidad de habitantes de la ciudad: "))
    if poblacion <1:
        raise ValueError("No puede haber poblacion menor a 1")
    else:
        if poblacion <=10000:
            print("Ciudad pequena")
        elif poblacion <=100000 and poblacion >10000:
            print("Ciudad mediana")
        elif poblacion >100000:
            print("Ciudad grande")

try:        
    categoriaCiudad()
except ValueError as poblacionNegativo:
    print("El numero digitado debe ser mayor a 0")
print("Programa terminado")