# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:53:30 2023

@author: alex
"""

import numpy as np
import pandas as pd
db=pd.read_csv("C:/Users/alex/Desktop/INF354/PARCIAL1/PREGUNTA1B/games.csv", encoding='latin')
db=db.replace(np.nan,0)
print(db)

print("********CUARTILES********")
print(np.quantile(db["Rating"],[0.25]))
print(np.quantile(db["Plays"],[0.25]))
print(np.quantile(db["Playing"],[0.25]))
print(np.quantile(db["Backlogs"],[0.25]))
print(np.quantile(db["Wishlist"],[0.25]))

print("********PERCENTILES*********")
print(np.percentile(db["Rating"],[50]))
print(np.percentile(db["Plays"],[50]))
print(np.percentile(db["Playing"],[50]))
print(np.percentile(db["Backlogs"],[50]))
print(np.percentile(db["Wishlist"],[50]))
