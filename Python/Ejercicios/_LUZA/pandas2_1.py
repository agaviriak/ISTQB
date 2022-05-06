import string
import pandas as pd # Librería que nos permitirá cargar los datos fácilmente
import numpy as np

data = pd.read_json('C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/_LUZA/cancer-data.json')  
mascara3 = (data["radius_mean"] == "desconocido")
data=data[~mascara3]
data["radius_mean"] = data["radius_mean"].astype("float64")
mascara4 = (data["radius_mean"] <= 0)
mascara5 = (data["radius_mean"] > 28.11)
mascara6 = (data["radius_mean"].isna())
data=data[~mascara4]
data=data[~mascara5]
data=data[~mascara6]
print(data["radius_mean"].unique())