# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:01:51 2022

@author: Danny Ortega
"""
import math 
import random
print("Area y Longitud de una circunferencia\n")

def circunferencia():
    radio = float(input("Ingresa medida del radio en cms: "))
    area = math.pi*radio**2
    longitud= 2*math.pi*radio
    return print(f"El area del circulo es: {area:.3f} y la longitud es: {longitud:.3f}")
    
def azar():
    lista_estudiante= ["Danny Ortega", "Alejandro Julio", "Andres Dario", "Carlos Arredondo", "Jhon Gonzalez"
                       ,"Juliana Montoya", "Paola Banquet", "Santiago Cordoba", "Andres Higuita", "Sebastian Marsiglia"
                       , "Santiago Metaute","Carlos Ochoa", "Juan Pineda", "Santiago Saldarriaga", "Carlos Sanchez", "Juan Pablo Villa"]
    aleatorio = random.choice(lista_estudiante)
    return print(f"El estudiante afortunado es: {aleatorio}")


def areaTriangulo():
    a = float(input("Escribe la medida del lado A: "))
    b = float(input("Escribe la medida del lado B: "))
    c = float(input("Escribe la medida del lado C: "))
    p = (a+b+c)/2
    if (p-a) > 0 and (p-b) > 0 and (p-c) >0:
        area = (p*(p-a)*(p-b)*(p-c))**0.5
        print(f"El area del triangulo es: {area:.2f}")
    else:
        print("El calculo da negativo, por ende no se puede calcular")
    
    
def revisarNumero():
    num = int(input("Escribe el numero: "))
    if num%5 == 0:
        print(f"El numero {num} termina en 0 o 5")
    else: 
        print("El numero que escribiste termina diferente de 0 o 5")
    

def rango():
    num = int(input("Escribe el numero: "))
    if num not in range(1, 26):
        print(f"El numero {num} no esta entre el rango permitido")
    else:
        print(f"Buena eleccion, tu numero es: {num}")
        
def intercambio():
    num1 = int(input("Escribe el primer numero: "))
    num2 = int(input("Escribe el segundo numero: "))
    print(f"El numero 1 es: {num1}")
    print(f"El numero 2 es: {num2}")
    temp = num1
    num1 = num2
    num2 = temp
    print(f"Despues del intercambio el numero 1 es: {num1}")
    print(f"Despues del intercambio el numero 2 es: {num2}")
          
#circunferencia()
azar()
#areaTriangulo()
#revisarNumero()   
#rango()
#intercambio()

