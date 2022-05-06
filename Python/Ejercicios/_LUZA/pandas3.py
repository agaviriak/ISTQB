from cmath import nan
from itertools import count
import string
import pandas as pd # Librería que nos permitirá cargar los datos fácilmente
import numpy as np

data = pd.read_json('C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/_LUZA/cancer-data.json')  
perimetro=data["perimeter_mean"].unique()
mascara = (data["perimeter_mean"].isna())
data=data[~mascara]

for i in perimetro:
    if ((i<0) or (type(i) is string)):
        mascara1 = (data["perimeter_mean"] == i)
        data=data[~mascara1]

print(data["perimeter_mean"])
print(data["perimeter_mean"].count())
