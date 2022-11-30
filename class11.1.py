# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:58:37 2022

@author: Danny Ortega
"""
#from class 11 import 

import pandas as pd
import numpy as np

#Aqui creamos un data frame
df=pd.DataFrame(np.random.randint(0,100,size=(4,5)),columns=list('ABCDE'),index=list('1234'))
print("El dataframe creado es: ")
print(df,'\n')

#Para acceder a una fila especifica por etiqueta
print(df.loc['3'])

#Para acceder a una fila especifica por indice
print(df.iloc[2])

#Maximo de cada columna
print(df.max())

#Acceder a una columna
print(df['B'])

#Para acceder al maximo de una columna en especifico
print(df[['B','D','C']].max())

#Para acceder a la posicion del mayor de cada columna utilizamos idxmax()
print(df.idxmax())

#Para acceder a la posicion del mayor de cada fila utilizamos idxmax()
print(df.idxmax(axis=1))

#Maximo de todo el dataframe
print(df.max().max())

#Añadir una fila nueva al dataframe

nueva_fila = {'A':5, 'B':87, 'C':92, 'D':97, 'C':50}
 
#remplazar un valor del dataframe
#df.replace()
