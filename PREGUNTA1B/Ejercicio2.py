# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:38:14 2023

@author: alex
"""

archivo = 'games.csv'
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/alex/Desktop/INF354/PARCIAL1/PREGUNTA2/games.csv", encoding='latin')


x = data.Rating.quantile([0.25,0.9,0.95])
#data.columns

print("---------------1ra columna")
print(x)


