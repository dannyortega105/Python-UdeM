# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 21:01:22 2022

@author: Danny Ortega
"""

#PANDAS se complementa con Numpy
#El nucleo principal de data son los dataframe
#Enamorarse de numpy y pandas si quieres ser un data science

import numpy as np
import pandas as pd

#Vamos a generar nuestro primer dataFrame
#size es la cantidad de filas y columnas que quiero
listaF=['Categoria 1','Categoria 2','Categoria 3','Categoria 4']
listaC=['Carro', 'Moto', 'Bicicleta', 'Avion', 'Barco']
dataF=pd.DataFrame(np.random.randint(0,100,size=(4,5)),columns=listaC,index=listaF)
print(dataF)