import string
import pandas as pd # Librería que nos permitirá cargar los datos fácilmente
import numpy as np

data = pd.read_json('C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/_LUZA/cancer-data.json')  
radio=data["radius_mean"].unique()

for i in radio:
    if (type(i) != float) or (i<0):
        mascara1 = (data["radius_mean"] == i)
        data=data[~mascara1]

print(data["radius_mean"].unique())



