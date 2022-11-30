# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:51:18 2022

@author: Danny Ortega
"""

import numpy as np
import pandas as pd

lista=['Armamento', 'Asesoria militar','Alimentos','Personal medico','Entrenamiento','Diplomatica', 'Migracion']
df=pd.DataFrame(np.random.random((15,7))*100,columns=lista)
print(df)
"""
#Para acceder a una posicion del dataframe
df.loc[1, 'Armamento']=np.NaN
print(df)

df.loc[2, 'Migracion']=np.NaN
print(df)

#Para ver solo los datos de una columna especifica
print(df['Alimentos'])

#Para ver las primeras 5 lineas
print(df.head(2))

#Para ver las ultimas 5 lineas
print(df.tail())

#para ver informacion estadistica del dataframe
print(df.describe())

#Para ver las lineas dentro de un rango
print(df.iloc[0:5])

#Para organiza rlos valores por columna
print(df.sort_values(by='Armamento')) #Ascendente
print(df.sort_values(by='Armamento',ascending=False)) #Descendente
"""
#Si deseo ver los paises con mayor asistencia de armamento sea de 50
print(df["Armamento"]>50)

#Si deseo ver los paises que cumplen esta condicion
#Mostrar los paises y las columnas
print(df[df.iloc[:,0]>50])

#Para guardar nuestro dataframe
#Asistencia=df.to_csv('C:\\Users\\Danny Ortega\\Desktop\pythonUdeM\Asistencia.csv')






