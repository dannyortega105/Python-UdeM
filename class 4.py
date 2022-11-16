# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:57:47 2022

@author: Danny Ortega
"""

def division(D,d):
    R=D
    C=0
    while R>=d:
        R=R-d
        C+=1
    return R,C

print("Division por restas sucesivas")
D=int(input("Ingrese dividendo"))
d=int(input("ingrese divisor"))
residuo, cociente=division(D,d)
print(cociente, residuo)