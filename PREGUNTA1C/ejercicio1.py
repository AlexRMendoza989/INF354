# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 02:06:23 2023

@author: alex
"""

archivo = 'games.csv'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("C:/Users/alex/Desktop/INF354/PARCIAL1/PREGUNTA1C/games.csv", encoding='latin')

data.head
w_installs = data['Rating']
x_price = data['Times Listed']
y_rating = data['Number of Reviews']
z_count = data['Genres']

plt.title('Grafica Installs')
plt.plot(w_installs)
#plt.title('Grafica Price')
#plt.plot(x_price)
#plt.title('Grafica Rating')
#plt.plot(y_rating)
#plt.title('Grafica Count Rating')
#plt.plot(z_count)
plt.grid()
plt.show()
