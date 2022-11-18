# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 20:46:26 2022

@author: Danny Ortega
"""

import random

diccionario = {}
def crearDiccionario():
    continuar = "Si"
    while continuar=="Si":
        ciudad=input("Ingrese el nombre de la ciudad: ")
        ventas =[[random.randint(1,1000) for i in range(3)]for j in range(4)]
        diccionario.update({ciudad:ventas})
        continuar=input("Digite 'Si' para continuar agregando producto o 'No' para salir: ")
    return diccionario


def consultar():
    ciudad = input("Digite la ciudad que desea consultar: ")
    matrizVenta= diccionario[ciudad]
    for i in matrizVenta:
        print(i)
        
def maximo(matriz):
    maximo = matriz[1][1]
    for i in range(4):
        for j in range (3):
            if matriz[i][j]>maximo:
                maximo=matriz[i][j]
    
    print(f"El maximo es: {maximo}")

def inicio():
    
    opciones= 0
    while opciones != "S":
        print("BIENVENIDO, ESTA ES LA LISTA DE OPCIONES\n")                                                           
        print("[A] Agregar", "[C] Consultar", "[M] Maximo y Minimo", "[S] Salir")
        opciones = input("Elige una opcion: ")
        
        if opciones == "A":
            opciones2= 0
            while opciones2 != "S":
                print("[A] Agregar almacen", "[P] Agregar Producto", "[S] Salir")
                opciones2 = input("Elige una opcion: ")
                if opciones2 == "A":
                    print(crearDiccionario())
                elif opciones2 == "P":
                    print("Pronto estara disponible esta opcion")
                elif opciones2 == "S":
                    break
        elif opciones == "C":
            print(consultar())
        elif opciones == "M":
            ciudad = input("Digite la ciudad que desea ver el maximo: ")
            matriz = diccionario[ciudad]                          
            for i in matriz:
                print(i)
            maximo(matriz)
        elif opciones == "S":
            print("Gracias por participar")
            break
        
inicio()
#consultar()