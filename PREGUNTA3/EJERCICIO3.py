# -*- coding: utf-8 -*-
"""


@author: alex
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
datos=pd.read_csv('dataR2.csv')
datos=datos.replace(np.nan,"0")
prepro = KBinsDiscretizer(n_bins=6, encode='ordinal', strategy='uniform')
datos1=prepro.fit_transform(datos)
print(datos1)

#de una columna
dato_columna = KBinsDiscretizer(n_bins=6, encode='ordinal',
                           strategy = "uniform".fit_transform(datos[['Age']])
print(dato_columna)

