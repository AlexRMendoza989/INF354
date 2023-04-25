# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:27:39 2023

@author: alex
"""
archivo = 'games.csv'
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/alex/Desktop/INF354/PARCIAL1/PREGUNTA1/games.csv", encoding='latin')

data.head

def percentil(per,x):
    n=len(x)
    pos=int((per*n)/100)
    aux=np.sort(x)
    return aux[pos]

#1ra Rating
print("-------------1ra Rating")
print(percentil(25, data.Rating))
print(percentil(90, data.Rating))
print(percentil(95, data.Rating))
# 3ra Times Listed
print("-----------3ra Times Listed")
print(percentil(25, data['Times Listed']))
print(percentil(90, data['Times Listed']))
print(percentil(95, data['Times Listed']))

# 4ta Number of Reviews
print("-----------4ta Number of Reviews")
print(percentil(25, data['Number of Reviews']))
print(percentil(90, data['Number of Reviews']))
print(percentil(95, data['Number of Reviews']))
# 2da Backlogs
print("---------------2da Backlogs")
print(percentil(25, data.Backlogs))
print(percentil(90, data.Backlogs))
print(percentil(95, data.Backlogs))
# 2da Wishlist
print("---------------2da Wishlist")
print(percentil(25, data.Wishlist))
print(percentil(90, data.Wishlist))
print(percentil(95, data.Wishlist))
# 2da columna
print("---------------2da Playing")
print(percentil(25, data.Playing))
print(percentil(90, data.Playing))
print(percentil(95, data.Playing))


