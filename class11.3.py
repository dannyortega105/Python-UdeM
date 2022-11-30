# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:08:21 2022

@author: Danny Ortega
"""
import pandas as pd

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
c=pd.read_csv(url)

print(c.tail)