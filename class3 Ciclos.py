# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:21:30 2022

@author: Danny Ortega
"""
"""
Un programa que calcule el promedio de 10 numeros que ingresemos
"""
#Multiplicar desde 1 hasta que llegue al numero

def promedio():
    print("Estructura repetitiva FOR\n")
    suma = 0
    for i in range(0,10):
        num = int(input(f"Digite el numero {i + 1}: "))
        if num >= 0:
            suma += num
        else:
            break
    
    promedio = suma/(i + 1)
    print(f"El promedio de los numeros es: {promedio}\n")

def factorial():
    factorial = 1
    num = int(input("Ingrese el numero: "))
    if num == 0:
        print(f"El factorial de {num} es : 1")
    else:
        for i in range(1, num+1):
            factorial *= i
        print(f"El factorial de {num} es: {factorial}\n")
        


def inicio():
    
    opciones= 0
    while opciones != "S":
        print("BIENVENIDO, ESTA ES LA LISTA DE OPCIONES\n")
        print("[F] Factorial", "[P] Promedio", "[S] Salir")
        opciones = input("Elige una opcion: ")
        
        if opciones == "F":
            factorial()
        elif opciones == "P":
            promedio()
        elif opciones == "S":
            print("Gracias por participar")
            break
        
inicio()

"""i = 1
while i <= 20:
    print(i)
    i += 1
print("Termino el cliclo")"""