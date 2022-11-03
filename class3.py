# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:44:48 2022

@author: Danny Ortega
"""

"""Un programa para un cajero electronico que entregue al cliente
la menor cantidad de billetes de acuerdo con el saldo disponible
y el monton solicitado suponer las denominaciones de 100, 50, 20 y 10
"""

"""print("BIENVENIDO AL CAJERO U DE M")

saldo = 500000
cant100=0
cant50=0
cant20=0
cant10=0


print(f"Hola, tu saldo actual es: {saldo}")
monto = int(input("Escribe cuanto dinero quieres retirar: "))
if saldo > monto:
   if monto%100000==0:
       pendiente=monto
       cant100=pendiente//100000
       pendiente =pendiente-cant100*100000
       cant50=pendiente//50000
       pendiente=pendiente -cant50*50000
       cant20=pendiente//20000
       pendiente=pendiente-cant20*20000
       cant10=pendiente//10000
            
            
else:
    print("Saldo insuficiente")
print(f"La cantidad de billetes de 100 es: {cant100}")
print(f"La cantidad de billetes de 100 es: {cant50}")
print(f"La cantidad de billetes de 100 es: {cant20}")
print(f"La cantidad de billetes de 100 es: {cant10}")
"""
    
print("Condicione multiple")
notaAlfa= input("Digite nota alfabetica: ")
if notaAlfa == 'A':
    print("Calificaciones numerica: 3.0")
elif notaAlfa == "B":
    print("Calificacion numerica: 4.0")
elif notaAlfa == "C":
    print("Calificacion numero: 5.0")
elif notaAlfa == "D":
    print("Calificacion numero: 2.0")
elif notaAlfa == "E":
    print("Calificacion numero: 1.0")
else:
    print("Nota no valida")