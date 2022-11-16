# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:47:27 2022

@author: Danny Ortega
"""

def division(n1, n2):
    try:
        div = n1/n2
    except ZeroDivisionError:
        print("No se puede dividir un numero por cero (0)")
    else:
        return div
    
def suma(n1, n2):
    s=n1+n2
    return s

def modulo(n1, n2):
    try:
        mod=n1%n2
    except ZeroDivisionError:
        print("No se puede obtener el modulo de una division por cero")
    else:
        return mod
def divEntera(n1, n2):
    try:
        d=n1//n2
    except ZeroDivisionError:
        print("No se puede dividir un numero por cero")
    else:
        return d
    
while True:
    try:   
        n1 = int(input("Digite el primero numero: "))
        break
    except ValueError:
        print("Solo es permitido numeros enteros, por favor escribir un valor correcto")
        
while True:
    try:   
        n2 = int(input("Digite el segundo numero: "))
        break
    except ValueError:
        print("Solo es permitido numeros enteros, por favor escribir un valor correcto")

#print("El resultado de la division es:", division(n1,n2))
#print("El resultado de la suma es:", suma(n1,n2))
#print("El modulo de la division es:", modulo(n1,n2))
#print("El resultado de la division entera es:", divEntera(n1,n2))

"""
Un diccionario que tenga nombre de sucursales de cualquier almacen y que la clave sea el nombre del almacen, el valor sea una matriz
que tenga productos en la matriz y tiendas en diferentes ciudades

"""
import random
def crearDiccionario():
    diccionario = {}
    continuar = "Si"
    while continuar=="Si":
        almacen=input("Ingrese el nombre de la ciudad: ")
        ventas =[[random.randint(1,100) for i in range(11)]for j in range(6)]
        diccionario.update({almacen:ventas})
        continuar=input("Digite 'Si' para continuar")
    return diccionario

print(crearDiccionario())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
